# Generated by Django 4.2.1 on 2023-08-30 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stagiaire', '0003_alter_offre_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisor',
            name='supervisor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
