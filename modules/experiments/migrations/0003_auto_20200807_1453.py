# Generated by Django 3.0.8 on 2020-08-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0002_auto_20200807_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
