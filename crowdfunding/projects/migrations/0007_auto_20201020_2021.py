# Generated by Django 3.0.8 on 2020-10-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200929_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='total_raised',
            field=models.IntegerField(default=0),
        ),
    ]