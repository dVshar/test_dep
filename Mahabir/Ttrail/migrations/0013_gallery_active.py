# Generated by Django 3.1.12 on 2023-04-06 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ttrail', '0012_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
