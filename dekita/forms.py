from django import forms
from .models import ToDoList, Category, Do


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


class AddDoForm(forms.ModelForm):
    class Meta:
        model = Do
        fields = ("do_text",)
