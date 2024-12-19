from django.urls import path
from .views import list_statistics_view, toy_statistics_view, time_to_make_view, time_to_bring_view

urlpatterns = [
    path('', list_statistics_view),
    path('toys', toy_statistics_view),
    path('time_to_make', time_to_make_view),
    path('time_to_bring', time_to_bring_view),
]