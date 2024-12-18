from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Toy, Coal
from .forms import ToyForm
from santalist.models import Kid, SantasList


def toy_list_view(request):
    if request.method == "GET":
        toys = Toy.objects.all()

        # Single line loop to create the list that will be displayed.
        toy_list = [f"{toy.toy_type}" for toy in toys]

        return render(request, "toylist.html", context={'toys':toy_list})

    return HttpResponse("Bad Request.", status=400)


def get_toy_by_id_view(request, toy_id):
    if request.method == "GET":
        # Make sure we toy with that id
        try:
            toy = Toy.objects.get(id=toy_id)
        except ObjectDoesNotExist:
            return HttpResponse("No toy with that id in the list.", status=400)

        return HttpResponse(f"{toy.toy_type}", status=200)

    return HttpResponse("Bad Request.", status=400)

def toy_create_view(request):
    if request.method == "GET":
        toy_form = ToyForm()

        return render(request, "toycreateform.html", context={'form': toy_form})
    elif request.method == "POST":
        toy_form = ToyForm(request.POST)

        # Validate the form we filled
        if toy_form.is_valid():
            toy_form.save()
            return redirect("/toy_factory/")
        else:
            return HttpResponse("Please enter a toy kids want.", status=400)

    return HttpResponse("Bad Request.", status=400)

def give_toy_view(request):
    if request.method == "GET":
        # Render the give toys button
        return render(request, "givetoys.html")
    elif request.method == "POST":

        # Get the current Santa's list then nice and naughty kids
        nice_kids = SantasList.objects.last().nice_list.all()
        naughty_kids = SantasList.objects.last().naughty_list.all()

        for nice_kid in nice_kids:
            gift_needed = nice_kid.gift

            # Get the firs toy that is not already owned and is the correct type
            toy = Toy.objects.filter(toy_type=gift_needed, owner__isnull=True).first()

            # If we got the toy make the toy owner the current kid
            if toy is not None:
                toy.owner = nice_kid
                toy.save()

        for naughty_kid in naughty_kids:
            # Create coal with naughty kid as owner
            coal = Coal.objects.create(owner=naughty_kid)
            coal.save()

        return redirect("/santa_list/")

    return HttpResponse("Bad Request.", status=400)