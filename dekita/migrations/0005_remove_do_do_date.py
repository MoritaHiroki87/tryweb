# Generated by Django 2.0.6 on 2018-07-22 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dekita', '0004_auto_20180722_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='do',
            name='do_date',
        ),
    ]