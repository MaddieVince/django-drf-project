# Generated by Django 3.0.8 on 2020-09-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200915_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='kudos',
            field=models.BooleanField(default=False),
        ),
    ]