from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = Task
        fields = "__all__"

class MenuForm(forms.ModelForm):
    cantidad = forms.IntegerField(min_value=0)
    
    class Meta:
        model = Solicita
        fields = "__all__"