from django.shortcuts import render
from django.http import HttpResponse
from .models import Kid, SantasList
from .forms import KidForm

# Create your views here.

def get_list_view(request):
    if request.method == "GET":
        santas_list = SantasList.objects.first()

        naughty_list = [kid.first_name for kid in santas_list.naughty_list.all()]
        nice_list = [kid.first_name for kid in santas_list.nice_list.all()]

        return render(request,  "list.html", context={'naughty_list':naughty_list, 'nice_list':nice_list})
    else:
        return HttpResponse("Bad Request.", status=400)


def create_list_view(request):
    pass
def create_kid_view(request):
    pass
def delete_kid_view(request):
    pass
def get_kids_view(request):
    pass
def get_kid_by_id_view(request, kid_id):
    pass