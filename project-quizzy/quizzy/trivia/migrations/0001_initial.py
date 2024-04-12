# Generated by Django 5.0 on 2024-01-09 21:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=30, verbose_name='Pregunta')),
                ('correct_answer', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=15)),
                ('type_trivia', models.CharField(choices=[('NO', 'Normal'), ('TO', 'Time Out'), ('YN', 'Yes No')], default='NO', max_length=2)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choise_text', models.CharField(max_length=10)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='trivia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.trivia'),
        ),
    ]
