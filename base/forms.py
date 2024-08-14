from .models import Todo
from django import forms

class TodoCreationForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'image']