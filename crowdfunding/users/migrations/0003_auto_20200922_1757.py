# Generated by Django 3.0.8 on 2020-09-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200919_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio_pic',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='project_owner',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_bio',
            field=models.TextField(),
        ),
    ]