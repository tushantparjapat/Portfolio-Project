# Generated by Django 4.1.5 on 2023-02-12 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0005_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
