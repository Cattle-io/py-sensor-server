# Generated by Django 3.0.8 on 2020-08-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('image', models.FilePathField(path='/img')),
                ('description', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('place_name', models.CharField(max_length=200)),
                ('place_category', models.CharField(max_length=200)),
                ('place_lat', models.CharField(max_length=200)),
                ('place_lng', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]