# Generated by Django 4.2.1 on 2023-09-14 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stagiaire', '0015_stagiaire_offre_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagiaire',
            name='niveau',
            field=models.CharField(blank=True, default='Bac+2', max_length=50),
        ),
    ]
