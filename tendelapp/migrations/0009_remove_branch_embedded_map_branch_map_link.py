# Generated by Django 4.2 on 2023-05-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendelapp', '0008_branch_embedded_map'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='embedded_map',
        ),
        migrations.AddField(
            model_name='branch',
            name='map_link',
            field=models.URLField(default='https://goo.gl/maps/Fi16xpcx8gFv4DND7'),
        ),
    ]
