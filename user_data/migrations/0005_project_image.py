# Generated by Django 4.1.5 on 2023-02-12 08:05

from django.db import migrations, models
import user_data.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0004_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='G:\\Workshop\\django porjects\\portfolio2\\portfolio\\static\x07ssets\\imgs\\man.png', null=True, upload_to=user_data.models.Project.photo_path),
        ),
    ]