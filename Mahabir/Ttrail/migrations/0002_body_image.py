# Generated by Django 3.1.12 on 2023-04-03 07:58

import Ttrail.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Ttrail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(default='image', max_length=2500)),
                ('Images', djongo.models.fields.ArrayField(default=[], model_container=Ttrail.models.Body_Img)),
            ],
        ),
    ]