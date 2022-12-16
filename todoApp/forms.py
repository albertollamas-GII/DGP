from django import forms
from django.forms import ModelForm

from .models import *

class MenuForm(ModelForm):
    class Meta:
        model = Solicita
        fields = "__all__"