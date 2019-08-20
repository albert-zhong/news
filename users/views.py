from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from .forms import CustomUserCreationForm
from .models import CustomUser


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

