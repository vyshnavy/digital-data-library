'''
Created by Gotham on 14-07-2018.
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]