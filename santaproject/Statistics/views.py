from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from santalist.models import Kid, SantasList
from toyfactory.models import Toy

TIME_TO_BRING_ONE_TOY = 150

# /statistics/
@login_required(login_url='/login/')
def list_statistics_view(request):
    if request.method == "GET":
        # Get the latest list we created
        santas_list = SantasList.objects.last()

        # extract the lists from santa list model
        naughty_list = santas_list.naughty_list
        nice_list = santas_list.nice_list

        context = {'naughty_kid_count': naughty_list.count, 'nice_kid_count': nice_list.count}

        return render(request, "liststatistics.html", context=context)

    return HttpResponse("Bad Request.", status=400)

# /statistics/toys/
@login_required(login_url='/login/')
def toy_statistics_view(request):
    if request.method == "GET":
        kids_owners = Kid.objects.all()

        # In this dict we store toy types as keys and count as values
        toys_dict = {}

        for kid in kids_owners:
            # Get the toy kid wants as string
            toy_type = str(kid.gift)

            # If we already have a key in the dict we add one to value otherwise we add it with value 1
            if toy_type in toys_dict:
                toys_dict[str(toy_type)] += 1
            else:
                toys_dict[str(toy_type)] = 1


        context = {'toys': [toy_instance for toy_instance in toys_dict.items()]}

        return render(request, "toycount.html", context=context)

    return HttpResponse("Bad Request.", status=400)

# /statistics/time_to_make/
@login_required(login_url='/login/')
def time_to_make_view(request):
    if request.method == "GET":
        toys = Toy.objects.all()

        # In this list we store tuples of toy name and time to make
        toys_list = []

        total_time = 0

        for toy in toys:
            # Get the toy kid wants as string
            toy_type = str(toy.toy_type)

            # Append the set with type and time to make
            toys_list.append((toy_type, toy.time_to_make))

            # Add this toy make time to sum
            total_time += toy.time_to_make

        context = {'toys': toys_list, 'total_time':total_time}

        return render(request, "toytimetomake.html", context=context)

    return HttpResponse("Bad Request.", status=400)

# /statistics/time_to_bring/
@login_required(login_url='/login/')
def time_to_bring_view(request):
    if request.method == "GET":
        toys = Toy.objects.all()

        total_time = 0

        # Sum making time
        for toy in toys:
            total_time += toy.time_to_make


        # Time to bring is time to bring all toys plus time to make all toys
        time_to_bring = toys.count() * TIME_TO_BRING_ONE_TOY + total_time

        context = {'time_to_bring': time_to_bring}

        return render(request, "timetobringtoys.html", context=context)

    return HttpResponse("Bad Request.", status=400)