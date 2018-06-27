# test.py
from django.test import TestCase
from .models import ToDoList, Category


class MyAppTest(TestCase):
    def test_create_model(self):
        # ToDoListを作ればCategoryも一緒に作られるはず・・・
        ToDoList.objects.create()
        self.assertTrue(Category.objects.all().count() > 0)
        category = Category.objects.all().first()
        self.assertEqual(category.category, 'default')