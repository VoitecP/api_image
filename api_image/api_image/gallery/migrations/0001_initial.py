# Generated by Django 4.0 on 2023-02-16 13:52

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier_name', models.CharField(max_length=50)),
                ('thumb1_H', models.IntegerField(max_length=20)),
                ('thumb1_W', models.IntegerField(max_length=20)),
                ('thumb2_H', models.IntegerField(blank=True, default=None, editable=False, max_length=20)),
                ('thumb2_W', models.IntegerField(blank=True, default=None, editable=False, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('tier_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gallery.tier')),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images')),
                ('thumb_1', models.ImageField(editable=False, upload_to='thumbs')),
                ('thumb_2', models.ImageField(blank=True, editable=False, upload_to='thumbs')),
                ('img_link', models.URLField()),
                ('exp_time', models.IntegerField()),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2023, 2, 16, 14, 52, 27, 781658), editable=False)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gallery.user')),
            ],
        ),
    ]
