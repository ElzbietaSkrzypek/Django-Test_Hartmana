# Generated by Django 4.2 on 2023-05-08 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_choice_variable_remove_choice_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='vote',
        ),
    ]
