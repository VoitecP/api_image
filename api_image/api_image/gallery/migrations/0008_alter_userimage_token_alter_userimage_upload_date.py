# Generated by Django 4.0 on 2023-02-18 06:33

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_userimage_thumb_1_link_userimage_thumb_2_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='token',
            field=models.UUIDField(default=uuid.UUID('033539cc-5901-481b-908a-23bf2ff3d897'), editable=False),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 7, 33, 7, 196065), editable=False),
        ),
    ]
