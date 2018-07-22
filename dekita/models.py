from django.db import models
from django.utils import timezone

# Create your models here.


class Do(models.Model):
    do_text = models.CharField(max_length=200)

    def __str__(self):
        return self.do_text

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


def default_category():
    category, _ = Category.objects.get_or_create(category='default')
    # idを返す
    return category.id


class ToDoList(models.Model):
    category = models.ForeignKey(
        Category, default=default_category, on_delete=models.CASCADE)
    todolist = models.CharField(max_length=200)
    wayoflearning = models.CharField(max_length=200, default="")
    created_at = models.DateTimeField(default=timezone.now)
    displayflag = models.BooleanField(default=True)


    def __str__(self):
        return self.todolist


class DoneList(models.Model):
    done_text = models.CharField(max_length=30)