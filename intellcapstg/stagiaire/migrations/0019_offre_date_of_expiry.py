# Generated by Django 4.2.1 on 2023-09-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stagiaire', '0018_alter_offre_count_alter_offre_valable'),
    ]

    operations = [
        migrations.AddField(
            model_name='offre',
            name='date_of_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]