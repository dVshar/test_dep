from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Rooms)
admin.site.register(Booked_Room)
admin.site.register(Checkout)