'''
Created by Gotham on 14-07-2018.
'''
from .models import data
from django import forms

# basic search form
class DataSearchForm(forms.Form):
    search_text = forms.CharField(
                    required=False,
                    label='Search by tag',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )