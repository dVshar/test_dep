from django.urls import path,include
from .views import *

urlpatterns = [
    path('',landing,name="landing"),
    path('about/',About1,name="About"),
    path('booking/',Booking,name="Booking"),


    path('booking/<str:data>',BookingPost,name="BookingPost"),
    path('booking/Check/',Room_Checkout,name="BookingCheck"),
    path('Encode/',Encode_Fetch,name="encode"),


    path('contact/',Contact,name="Contact"),
    path('events/',Events,name="events"),
    path('gallery/',Gallery1,name="gallery"),
    path('location/',Locations,name="location"),
    path('services/',Services1,name="services"),
    path('rooms/',Rooms_Hotel,name="rooms"),
    path('restaurant/',Restaurants,name="restaurant"),
    path('recreation/',Recreation,name="recreation"),


    path('booking/checkout/<str:token>',Checkout,name="checkout"),
    path('booking/checkout/success/',Success_Payment,name="success"),

    path('booking/Check/success/',Success_Payment,name="Bookingsuccess"),
    path('booking/Check/failed/',Room_Checkout,name="Bookingsuccess"),


    path('booking/checkout/failed/',Fail_Payment,name="fail"),

    

]



