from djongo import models
from django_enumfield import enum

# Create your models here.
class Order_create(models.Model):
    Name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    number = models.CharField(max_length=100,null=True)
    adults = models.CharField(max_length=10,default=0)
    kids = models.CharField(max_length=10,default=0)
    order_id = models.CharField(max_length=1000,null=False)
    payment_id = models.CharField(max_length=1000,null=True)
    signature = models.CharField(max_length=1000,null=True)
    checkin_date = models.CharField(max_length=1000,null=True)
    checkout_date = models.CharField(max_length=1000,null=True)
    amount = models.CharField(max_length=100,null=True)
    Type = models.CharField(max_length=100,null=True)
    is_paid = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        if (self.Name):
            return self.Name+"("+self.checkin_date+")"
        else:
            return self.order_id
        

class Rooms(models.Model):
    class Types(enum.Enum):
        Delux = 1
        Super = 2
        Premium = 3
        Suite = 4

    Type = enum.EnumField(Types, default=1)
    Total = models.IntegerField(default=0)
    Available = models.IntegerField(default=0)
    Price = models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.Type)
    

class Booked_Room(models.Model):
    class Types(enum.Enum):
        Delux = 1
        Super = 2
        Premium = 3
        Suite = 4

    Type = enum.EnumField(Types, default=1)
    Name = models.CharField(max_length=100,null=True)
    Rooms = models.CharField(max_length=100,null=True)
    Checkin = models.CharField(max_length=100,null=True)
    Checkout = models.CharField(max_length=100,null=True)

class Checkout(models.Model):
        Name = models.CharField(max_length=100,null=True)
        Booked_id = models.CharField(max_length=100,null=True)

        def save():
            print("hi")

#* Menu
class Menu(models.Model):
    Domain = models.CharField(max_length=100,default='Domain')
    Hotel_name = models.CharField(max_length=20,default='Hotel Name')
    Home = models.BooleanField(default=True)
    Rooms = models.BooleanField(default=True)
    About_Us = models.BooleanField(default=True)
    Restaurant = models.BooleanField(default=True)
    Meeting = models.BooleanField(default=True)
    Recreation = models.BooleanField(default=True)
    Facilities = models.BooleanField(default=True)
    Nearby_Attraction = models.BooleanField(default=True)
    Gallery = models.BooleanField(default=True)
    Contact = models.BooleanField(default=True)
    Number = models.CharField(max_length=50,default='Number')
    

#? Abstract(Banner)
class Images(models.Model):
    Heading = models.CharField(max_length=250, default= "tittle")
    Image = models.CharField(max_length=2500, default= "image")

    class Meta:
        abstract = True

class Banner(models.Model):
    Domain = models.CharField(max_length=100,default='Domain')
    Category = models.CharField(default='banner', max_length=2500)
    Images = models.ArrayField(model_container= Images,default=[])

#? Abstract(Body image)
class Body_Img(models.Model):
    Image = models.CharField(max_length=2500, default= "image")

    class Meta:
        abstract = True

class Body_Image(models.Model):
    Domain = models.CharField(max_length=100,default='Domain')
    Category = models.CharField(default='image', max_length=2500)
    Images = models.ArrayField(model_container= Body_Img,default=[])

#* About
class About(models.Model):
    Domain = models.CharField(max_length=100,default='Domain')
    Heading = models.CharField(max_length=250, default= "tittle")
    Text = models.TextField(default='text')
    Image = models.CharField(max_length=2500, default= "https://img.freepik.com/free-vector/hotel-building-concept-illustration_114360-14039.jpg")

#? Abstract(Nearby Places)
class Places(models.Model):
    Heading = models.CharField(default='image', max_length=2500)
    Image = models.CharField(max_length=2500, default= "image")

    class Meta:
        abstract = True

class Nearby_places(models.Model):
    Domain = models.CharField(max_length=100,default='Domain')
    Category = models.CharField(default='image', max_length=2500)
    Images = models.ArrayField(model_container= Places,default=[])

class Services(models.Model):
    Domain = models.CharField(max_length=100,default='Domain')
    FrontDesk = models.BooleanField(default=True)
    Wifi = models.BooleanField(default=True)
    Board = models.BooleanField(default=True)
    Rooftop_Cafe = models.BooleanField(default=True)
    Health_Club = models.BooleanField(default=True)
    Express_checks = models.BooleanField(default=True)
    Wave_Bar = models.BooleanField(default=True)
    Conference_Hall = models.BooleanField(default=True)
    Alchemy = models.BooleanField(default=True)
    Suncafe = models.BooleanField(default=True)
    Doctor = models.BooleanField(default=True)
    Spa = models.BooleanField(default=True)
    Babysitting = models.BooleanField(default=True)
    Electricity = models.BooleanField(default=True)
    Concierge = models.BooleanField(default=True)
    Conditinoer = models.BooleanField(default=True)
    Security = models.BooleanField(default=True)
    TravelTour = models.BooleanField(default=True)
    Currency_Exchange = models.BooleanField(default=True)
    Laundry = models.BooleanField(default=True)
    Casino = models.BooleanField(default=True)
    Parking = models.BooleanField(default=True)
    Elevator = models.BooleanField(default=True)
    Jacuzzi = models.BooleanField(default=True)
    Room_Service = models.BooleanField(default=True)
    Accept_Cards = models.BooleanField(default=True)


#? Abstract(Banner)
class Room_Detail(models.Model):
    RoomType= models.CharField(max_length=250, default= "tittle")
    Price= models.CharField(max_length=250, default= "tittle")
    BookingLink= models.CharField(max_length=250, default= "tittle")
    Image= models.CharField(max_length=250, default= "tittle")

    class Meta:
        abstract = True

class Hotel_Rooms(models.Model):
    Domain = models.CharField(max_length=100,default='Domain')
    RequiredLanding = models.BooleanField(default=True)
    Text = models.CharField(default='banner', max_length=25000000)
    Room = models.ArrayField(model_container= Room_Detail,default=[])


class Footer(models.Model):
    Domain = models.CharField(max_length=100,default='Domain')
    Start_date = models.CharField(max_length=20,default='Since')
    Address = models.CharField(max_length=20,default='Address')
    State = models.CharField(max_length=20,default='State Name')
    City = models.CharField(max_length=20,default='City Name')
    Newsletter = models.BooleanField(default=True)
    Logo = models.CharField(max_length=2000, default='logo')
    Email = models.CharField(max_length=2000, default='email')


class Social_Links(models.Model):
    Domain = models.CharField(max_length=100,default='Domain')
    Facebook = models.CharField(max_length=2000, default='facebook')
    Instagram = models.CharField(max_length=2000, default='tlnstagram')
    Linkedin = models.CharField(max_length=2000, default='linkedin')
    Tripadvisor = models.CharField(max_length=2000, default='tripadvisor')
    Twitter = models.CharField(max_length=2000, default='twitter')


#? Abstract(Gallery)
class Gallery_Image(models.Model):
    Image= models.CharField(max_length=25000000, default= "tittle")

    class Meta:
        abstract = True

class Gallery(models.Model):
    Domain = models.CharField(max_length=100,default='Domain')
    Category = models.CharField(max_length=2000, default='category')#events,Restaurants,Hotels,Nearby,View,Rooms,Lobby,Bar,Playzone
    Images = models.ArrayField(model_container= Gallery_Image,default=[])
    active = models.BooleanField(default=True)


class advertisement(models.Model):
    Heading= models.CharField(max_length=25000000, default= "tittle")
    Text= models.CharField(max_length=25000000, default= "tittle")

    class Meta:
        abstract = True

class Popups(models.Model):
    Domain = models.CharField(max_length=100,default='Domain')
    Required = models.BooleanField(default=True)
    Category = models.CharField(max_length=2000, default='category')    #Information,Promotional
    Ads = models.ArrayField(model_container= advertisement,default=[])


class Booking_Engine_Links(models.Model):
    Domain = models.CharField(max_length=100,default='Domain')
    EngineLink = models.CharField(max_length=1000,default='Domain')
