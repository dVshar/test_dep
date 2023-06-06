# Generated by Django 3.1.12 on 2023-04-03 07:39

import Ttrail.models
from django.db import migrations, models
import django_enumfield.db.fields
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(default='banner', max_length=2500)),
                ('Images', djongo.models.fields.ArrayField(default=[], model_container=Ttrail.models.Images)),
            ],
        ),
        migrations.CreateModel(
            name='Booked_Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', django_enumfield.db.fields.EnumField(default=1, enum=Ttrail.models.Booked_Room.Types)),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Rooms', models.CharField(max_length=100, null=True)),
                ('Checkin', models.CharField(max_length=100, null=True)),
                ('Checkout', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Booked_id', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hotel_name', models.CharField(default='Hotel Name', max_length=20)),
                ('Home', models.BooleanField(default=False)),
                ('Rooms', models.BooleanField(default=False)),
                ('About_Us', models.BooleanField(default=False)),
                ('Restaurant', models.BooleanField(default=False)),
                ('Meeting', models.BooleanField(default=False)),
                ('Recreation', models.BooleanField(default=False)),
                ('Facilities', models.BooleanField(default=False)),
                ('Nearby_Attraction', models.BooleanField(default=False)),
                ('Gallery', models.BooleanField(default=False)),
                ('Contact', models.BooleanField(default=False)),
                ('Number', models.CharField(default='Number', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order_create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('number', models.CharField(max_length=100, null=True)),
                ('adults', models.CharField(default=0, max_length=10)),
                ('kids', models.CharField(default=0, max_length=10)),
                ('order_id', models.CharField(max_length=1000)),
                ('payment_id', models.CharField(max_length=1000, null=True)),
                ('signature', models.CharField(max_length=1000, null=True)),
                ('checkin_date', models.CharField(max_length=1000, null=True)),
                ('checkout_date', models.CharField(max_length=1000, null=True)),
                ('amount', models.CharField(max_length=100, null=True)),
                ('Type', models.CharField(max_length=100, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', django_enumfield.db.fields.EnumField(default=1, enum=Ttrail.models.Rooms.Types)),
                ('Total', models.IntegerField(default=0)),
                ('Available', models.IntegerField(default=0)),
                ('Price', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]