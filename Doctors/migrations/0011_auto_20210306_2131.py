# Generated by Django 3.1.5 on 2021-03-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0010_merge_20210302_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='allbooking',
            name='Age',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='allbooking',
            name='Allot_Time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='allbooking',
            name='Email',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='allbooking',
            name='First_Name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='allbooking',
            name='Last_Name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='allbooking',
            name='Phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='week_timing',
            field=models.CharField(default='', max_length=500),
        ),
    ]