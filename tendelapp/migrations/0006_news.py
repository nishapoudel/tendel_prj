# Generated by Django 3.2.16 on 2023-05-04 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendelapp', '0005_alter_branch_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-news_id'],
            },
        ),
    ]
