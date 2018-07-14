'''
Created by Gotham on 14-07-2018.
'''
from django.urls import path
from datasets.views import DataSearchList
from . import views

urlpatterns = [
    path('', DataSearchList.as_view())
]