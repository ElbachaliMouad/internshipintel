# Generated by Django 4.2.1 on 2023-08-30 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stagiaire', '0008_alter_stagiaire_stagiaire_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisor',
            name='supervisor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]