from django.db import models
from django.utils import timezone

# Create your models here.
class DoDone(models.Model):
    do_text = models.CharField(max_length=200)
    done_text = models.CharField(max_length=200)
    do_date = models.DateTimeField('do_date')

class ToDoList(models.Model):
    todolist = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.todolist

class DoneList(models.Model):
    done_text = models.CharField(max_length=30)