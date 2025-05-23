# Generated by Django 5.2 on 2025-05-06 12:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_reserva_ambiente_professor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinar',
            name='professor',
            field=models.ForeignKey(blank=True, limit_choices_to={'tipo': 'P'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
