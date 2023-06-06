# Generated by Django 3.1.12 on 2023-05-01 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ttrail', '0016_auto_20230501_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='Image',
            field=models.CharField(default='https://img.freepik.com/free-vector/hotel-building-concept-illustration_114360-14039.jpg', max_length=2500),
        ),
        migrations.AlterField(
            model_name='footer',
            name='Newsletter',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='hotel_rooms',
            name='RequiredLanding',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='About_Us',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Contact',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Facilities',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Gallery',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Home',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Meeting',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Nearby_Attraction',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Recreation',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Restaurant',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Rooms',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order_create',
            name='is_paid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='popups',
            name='Required',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Accept_Cards',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Alchemy',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Babysitting',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Board',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Casino',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Concierge',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Conditinoer',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Conference_Hall',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Currency_Exchange',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Doctor',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Electricity',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Elevator',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Express_checks',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='FrontDesk',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Health_Club',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Jacuzzi',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Laundry',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Parking',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Rooftop_Cafe',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Room_Service',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Security',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Spa',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Suncafe',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='TravelTour',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Wave_Bar',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='Wifi',
            field=models.BooleanField(default=True),
        ),
    ]
