from django.urls import path, include
from .views import CustomLoginView

urlpatterns = [
    path('', CustomLoginView.as_view()),
]
