# Generated by Django 3.2.16 on 2023-06-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendelapp', '0022_auto_20230531_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modal',
            name='body',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='modal',
            name='image',
            field=models.ImageField(default=True, upload_to='notice/'),
        ),
        migrations.AlterField(
            model_name='modal',
            name='title',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
