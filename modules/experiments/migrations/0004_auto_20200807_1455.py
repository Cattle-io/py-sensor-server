# Generated by Django 3.0.8 on 2020-08-07 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0003_auto_20200807_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='duration_hrs',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='finished_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='started_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
