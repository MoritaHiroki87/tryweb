# Generated by Django 2.0.6 on 2018-07-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dekita', '0003_auto_20180702_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Do',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('do_text', models.CharField(max_length=200)),
                ('do_date', models.DateTimeField(verbose_name='do_date')),
            ],
        ),
        migrations.DeleteModel(
            name='DoDone',
        ),
    ]
