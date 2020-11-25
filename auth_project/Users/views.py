from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.

class SignUpView(CreateView):
    from_class = CustomUserCreationForm
    Success_url = reverse_lazy('login')
    template_name = 'signup.html'