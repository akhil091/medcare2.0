# Generated by Django 3.1.5 on 2021-03-01 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('All_Users', '0037_auto_20210301_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.FloatField(default=1614623206.0023265),
        ),
    ]