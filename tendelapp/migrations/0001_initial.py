# Generated by Django 4.2 on 2023-05-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='post/')),
                ('publish', models.BooleanField()),
                ('views', models.ManyToManyField(blank=True, related_name='post_views', to='tendelapp.ipmodel')),
            ],
            options={
                'ordering': ['-item_id'],
            },
        ),
    ]