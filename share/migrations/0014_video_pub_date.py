# Generated by Django 4.0.5 on 2022-06-23 11:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0013_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
