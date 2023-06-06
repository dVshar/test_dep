# Generated by Django 3.1.12 on 2023-04-03 08:46

import Ttrail.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Ttrail', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nearby_places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(default='image', max_length=2500)),
                ('Images', djongo.models.fields.ArrayField(default=[], model_container=Ttrail.models.Places)),
            ],
        ),
    ]