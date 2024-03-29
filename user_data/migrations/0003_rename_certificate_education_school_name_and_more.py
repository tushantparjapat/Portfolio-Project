# Generated by Django 4.1.5 on 2023-02-06 14:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_data', '0002_alter_education_user_alter_skill_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='certificate',
            new_name='school_name',
        ),
        migrations.AddField(
            model_name='education',
            name='Grade',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='education',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='education',
            name='end_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='education',
            name='start_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(default=datetime.date.today)),
                ('end_date', models.DateTimeField(default=datetime.date.today)),
                ('description', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Experience', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
