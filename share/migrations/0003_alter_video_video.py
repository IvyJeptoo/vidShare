# Generated by Django 4.0.5 on 2022-06-22 20:23

import cloudinary_storage.storage
from django.db import migrations, models
import share.validators


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='', validators=[share.validators.file_size], verbose_name='video'),
        ),
    ]
