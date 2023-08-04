from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreaitonForm

class SignUpView(CreateView):
    form_class= CustomUserCreaitonForm
    success_url=reverse_lazy('login')
    template_name='signup.html'

