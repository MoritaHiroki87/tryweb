from django import forms
from .models import ToDoList, Category


class AddForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ("category",
                  "todolist",
                  "wayoflearning",)


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("category",)


