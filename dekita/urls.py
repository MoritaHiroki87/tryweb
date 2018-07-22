from django.urls import path
from . import views

app_name = "dekita"
urlpatterns = [
    path('', views.index, name='index'),
    path("add/", views.add, name="add"),
    path("<int:todo_id>/edit/", views.edit, name="edit"),
    path("<int:todo_id>/done/", views.done, name="done"),
    path("add_category/", views.add_category, name="add_category"),
    path("<int:cate_id>/edit_category/", views.edit_category, name="edit_category"),
    path("<int:do_id>/add_do/", views.add_do, name="add_do"),
]