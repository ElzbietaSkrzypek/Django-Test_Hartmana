# Generated by Django 4.2 on 2023-04-28 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='variable',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
    ]