# Generated by Django 3.2 on 2021-12-10 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scheduler", "0005_auto_20211210_1427"),
    ]

    operations = [
        migrations.RemoveField(model_name="session", name="notes",),
        migrations.AlterField(
            model_name="session", name="date", field=models.DateField(),
        ),
    ]
