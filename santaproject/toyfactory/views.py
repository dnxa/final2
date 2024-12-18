from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Toy, Coal
from .forms import ToyForm

# Create your views here.
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

def give_toy_view(request):
    pass