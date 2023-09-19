# mottoapp/urls.py
from django.urls import path
from .views import MottoListView, Example

urlpatterns = [
    path('', MottoListView.as_view(), name='motto_list'),
    path('example/', Example, name='example'),
]