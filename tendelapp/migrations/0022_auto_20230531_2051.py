# Generated by Django 3.2.16 on 2023-05-31 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendelapp', '0021_modal'),
    ]

    operations = [
        migrations.AddField(
            model_name='modal',
            name='expiration_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='modal',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='notice/'),
        ),
    ]