# Generated by Django 3.1.5 on 2021-02-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('All_Users', '0005_auto_20210212_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.FloatField(default=1613318363.7866619),
        ),
    ]