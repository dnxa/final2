from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Kid, SantasList
from .forms import KidForm, KidDeleteForm


PASSING_NICENESS_COEFFICIENT = 0.5

# /santa_list/
@login_required(login_url='/login/')
def get_list_view(request):
    if request.method == "GET":
        '''
        I get the first list here. technically you could have more than one so
        it Might make more sense to loop through all of them using all()
        but we probably wont have more than one santa list at a time so I'll live it like this. 
        '''
        santas_list = SantasList.objects.last()

        # loop through all nice and naughty kids and fil the lists
        naughty_list = []
        nice_list = []

        # Append to the lists we will display
        for kid in santas_list.nice_list.all():
            nice_list.append(f"{kid.first_name} {kid.last_name} Niceness:{kid.niceness_coefficient}, Toy:{kid.toys.first()}")

        for kid in santas_list.naughty_list.all():
            naughty_list.append(f"{kid.first_name} {kid.last_name} Niceness:{kid.niceness_coefficient}, coal:{kid.coals.first()}")


        # Pass our list to list template
        return render(request,  "list.html", context={'naughty_list':naughty_list, 'nice_list':nice_list})

    return HttpResponse("Bad Request.", status=400)

# /santa_list/create
@login_required(login_url='/login/')
def create_list_view(request):
    if request.method == "GET":
        return render(request, "listform.html")
    elif request.method == "POST":
        # Get the current kids to designate them to right lists.
        kids = Kid.objects.all()

        # Create a new santa list
        new_santas_list = SantasList.objects.create()

        for kid in kids:
            # Sort the kids
            if float(kid.niceness_coefficient) > PASSING_NICENESS_COEFFICIENT:
                new_santas_list.nice_list.add(kid)
            else:
                new_santas_list.naughty_list.add(kid)

        new_santas_list.save()

        # Since santa list view picks the last list to display it will display the one we just created.
        return redirect("/santa_list/")

    return HttpResponse("Bad Request.", status=400)

# /santa_list/create_kid
@login_required(login_url='/login/')
def create_kid_view(request):
    if request.method == "GET":
        kid_form = KidForm()

        return render(request, "kidcreateform.html", context={'form': kid_form})
    elif request.method == "POST":
        kid_form = KidForm(request.POST)

        # Validate the form we just created
        if kid_form.is_valid():
            kid_form.save()
            return redirect("/santa_list/kids")

    return HttpResponse("Bad Request.", status=400)

# /santa_list/delete_kid
@login_required(login_url='/login/')
def delete_kid_from_list_view(request):
    if request.method == "GET":
        kid_delete_form = KidDeleteForm()

        return render(request, "kiddeleteform.html", context={'form': kid_delete_form})
    elif request.method == "POST":
        kid_delete_form = KidDeleteForm(request.POST)

        if kid_delete_form.is_valid():
            # Get the kid id from the form
            kid_id = kid_delete_form.cleaned_data['kid_id']

            # try to get the kid with the user provided id
            try:
                kid_to_delete = Kid.objects.get(id=kid_id)
            except ObjectDoesNotExist:
                return HttpResponse("No such kid in list.", status=400)

            # Get our santa's list
            santas_list = SantasList.objects.last()

            # If we have the kid in any of our lists we remove them
            if kid_to_delete in santas_list.nice_list.all():
                santas_list.nice_list.remove(kid_to_delete)
            elif kid_to_delete in santas_list.naughty_list.all():
                santas_list.naughty_list.remove(kid_to_delete)
            else:
                return HttpResponse("No such kid in list.", status=400)

            # Save the list.
            santas_list.save()

            return redirect("/santa_list/")

    return HttpResponse("Bad Request.", status=400)

# /santa_list/kids
@login_required(login_url='/login/')
def get_kids_view(request):
    if request.method == "GET":
        kids = Kid.objects.all()

        kid_name_list = [f"{kid.first_name} {kid.last_name}" for kid in kids]

        return render(request, "kidlist.html", context={'kids': kid_name_list})

    return HttpResponse("Bad Request.", status=400)

# /santa_list/kids/(kid_id)
@login_required(login_url='/login/')
def get_kid_by_id_view(request, kid_id):
    if request.method == "GET":
        # Make sure kid with that id exists
        try:
            kid = Kid.objects.get(id=kid_id)
        except ObjectDoesNotExist:
            return HttpResponse("No kid with that id in the list.", status=400)

        return HttpResponse(f"{kid.first_name} {kid.last_name}", status=200)

    return HttpResponse("Bad Request.", status=400)