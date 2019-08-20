from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import get_object_or_404

from .forms import CustomUserCreationForm
from .models import CustomUser


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserListView(ListView):
    model = CustomUser
    template_name = 'user_list.html'


class UserDetailView(DetailView):
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'user_detail.html'

    def get_object(self):
        object = get_object_or_404(CustomUser, username=self.kwargs.get("username"))
        return object