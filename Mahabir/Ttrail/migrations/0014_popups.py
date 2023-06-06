# Generated by Django 3.1.12 on 2023-04-19 10:44

import Ttrail.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Ttrail', '0013_gallery_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Required', models.BooleanField(default=False)),
                ('Category', models.CharField(default='category', max_length=2000)),
                ('Ads', djongo.models.fields.ArrayField(default=[], model_container=Ttrail.models.Gallery_Image)),
            ],
        ),
    ]