from django import forms
from .models import ToDoList


class AddForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ("todolist",)
