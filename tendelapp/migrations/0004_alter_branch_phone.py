# Generated by Django 3.2.16 on 2023-05-04 09:34

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('tendelapp', '0003_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
