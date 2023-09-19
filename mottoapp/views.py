# mottoapp/views.py
from .models import Motto
from django.views.generic import ListView
# Create your views here.

class MottoListView(ListView):
    model = Motto
    template_name = 'motto_list.html'
    context_object_name = 'mottos'

class Example():
    template_name = 'example.html'