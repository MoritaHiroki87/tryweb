from django.urls import path
from . import views

app_name = "dekita"
urlpatterns = [
    path('', views.index, name='index'),
    path("add/", views.add, name="add"),
    path("<int:todo_id>/edit/", views.edit, name="edit"),
    path("<int:todo_id>", views.done, name="done"),
]