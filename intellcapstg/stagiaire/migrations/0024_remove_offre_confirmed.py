# Generated by Django 4.2.1 on 2023-09-22 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stagiaire', '0023_remove_stagiaire_date_limite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offre',
            name='confirmed',
        ),
    ]
