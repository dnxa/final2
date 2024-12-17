from django.urls import path
from .views import (
    get_list_view,
    create_list_view,
    create_kid_view,
    delete_kid_view,
    get_kids_view,
    get_kid_by_id_view
)

urlpatterns = [
    path('', get_list_view),
    path('create', create_list_view),
    path('create_kid', create_kid_view),
    path('delete_kid', delete_kid_view),
    path('kids', get_kids_view),
    path('kids/<int:kid_id>', get_kid_by_id_view),
]