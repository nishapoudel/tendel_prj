# Generated by Django 3.2.16 on 2023-05-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendelapp', '0007_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='embedded_map',
            field=models.TextField(blank=True),
        ),
    ]
