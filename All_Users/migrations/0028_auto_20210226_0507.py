# Generated by Django 3.1.5 on 2021-02-25 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('All_Users', '0027_auto_20210226_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.FloatField(default=1614296258.7555327),
        ),
    ]