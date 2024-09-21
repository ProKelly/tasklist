from .models import Todo
from django import forms

class TodoCreationForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'image']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ['username', 'password']