# Generated by Django 4.0.5 on 2022-06-23 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0012_video_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='share.profile')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='share.video')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
