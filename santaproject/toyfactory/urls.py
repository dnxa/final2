from django.urls import path
from .views import toy_list_view, get_toy_by_id_view, toy_create_view, give_toy_view

urlpatterns = [
    path('', toy_list_view, name="toy_list_view"),
    path('<int:toy_id>', get_toy_by_id_view, name="get_toy_by_id_view"),
    path('create', toy_create_view, name="toy_create_view"),
    path('give_toys', give_toy_view, name="give_toy_view"),
]

