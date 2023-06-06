# Generated by Django 3.1.12 on 2023-04-05 10:57

import Ttrail.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Ttrail', '0011_auto_20230404_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(default='category', max_length=2000)),
                ('Images', djongo.models.fields.ArrayField(default=[], model_container=Ttrail.models.Gallery_Image)),
            ],
        ),
    ]
