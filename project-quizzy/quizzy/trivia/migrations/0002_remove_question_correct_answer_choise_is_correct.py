# Generated by Django 5.0 on 2024-01-09 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct_answer',
        ),
        migrations.AddField(
            model_name='choise',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
