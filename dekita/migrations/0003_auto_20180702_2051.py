# Generated by Django 2.0.6 on 2018-07-02 11:51

import dekita.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dekita', '0002_auto_20180627_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='category',
            field=models.ForeignKey(default=dekita.models.default_category, on_delete=django.db.models.deletion.CASCADE, to='dekita.Category'),
        ),
    ]
