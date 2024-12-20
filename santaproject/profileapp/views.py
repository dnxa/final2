from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Use pre-made view for login
class CustomLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/'