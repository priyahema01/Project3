# Generated by Django 4.0.7 on 2023-09-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_rename_dateofbirth_register_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='DOB',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='register',
            name='Date',
            field=models.IntegerField(max_length=20),
        ),
    ]
