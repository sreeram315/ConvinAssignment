# Generated by Django 2.0.6 on 2020-02-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.IntegerField(choices=[(1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3'), (3, 'Type 4')]),
        ),
        migrations.AlterField(
            model_name='tasktracker',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
