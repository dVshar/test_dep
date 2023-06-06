from rest_framework import serializers
from ..models import *
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
import os
import hashlib



#* Navbar
class NavbarSerializer(serializers.Serializer):
    HotelName = serializers.CharField(max_length=100,default="Fielmente.com")
    HotelNumber = serializers.CharField(max_length=100,default="9119059286")

#* About
class AboutSerializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    HotelName = serializers.CharField(max_length=100000,default="Heading")

#* Banner
class BannerSerializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")

#*Nearby
class NearbySerializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")

#* Images
class ImagesSerializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")

#* Footer
class FooterSerializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    Start_date = serializers.CharField(max_length=100000,default="Domain")
    Address = serializers.CharField(max_length=100000,default="Domain")
    State = serializers.CharField(max_length=100000,default="Domain")
    City = serializers.CharField(max_length=100000,default="Domain")
    Email = serializers.CharField(max_length=100000,default="email")

#* Services
class ServicesSerializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")

#* Social Links
class LinksSerializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")

#* Gallery
class GallerySerializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")

class PopupSerializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")




#! EDIT APIS

#*:- About EDIT
class About_edit_Serializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    Heading = serializers.CharField(max_length=100000,default="Heading")
    Image = serializers.CharField(max_length=100000,default="image")
    Text = serializers.CharField(max_length=100000,default="text")


#*:- Enable/Disable Gallery EDIT
class Gallery_edit_Serializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    Category = serializers.CharField(max_length=100,default="key")
    action = serializers.CharField(max_length=10,default="true")


#*:- Add/Pop gallery EDIT
class Gallery_edit_append_Serializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    Method = serializers.CharField(max_length=100,default="append")
    Category = serializers.CharField(max_length=100,default="key")
    Image = serializers.CharField(max_length=1000,default="img")


#*:- Add/Pop nearby,/banner EDIT
class Nearby_Banner_edit_append_Serializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    Method = serializers.CharField(max_length=100,default="append")
    Category = serializers.CharField(max_length=100,default="key")  #banner,nearby
    Heading = serializers.CharField(max_length=100,default="key")
    Image = serializers.CharField(max_length=1000,default="img")

#*:-Images EDIT
class Images_edit_append_Serializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    Method = serializers.CharField(max_length=100,default="append")
    Image = serializers.CharField(max_length=1000,default="img")


#*:- Social Links EDIT
class Social_Links_Edit_Serializers(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    facebook = serializers.CharField(max_length=10000,default="append")
    instagram = serializers.CharField(max_length=10000,default="key")  #banner,nearby
    linkedin = serializers.CharField(max_length=10000,default="key")
    tripadvisor = serializers.CharField(max_length=10000,default="img")
    twitter = serializers.CharField(max_length=10000,default="img")


#*:- Menu Management EDIT
class Menu_Management_Serializers(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    key = serializers.CharField(max_length=100,default="append")
    value = serializers.CharField(max_length=10000,default="key")


#*:- Add/Remove Services EDIT
class Services_Management_Serializers(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    key = serializers.CharField(max_length=100,default="append")
    value = serializers.CharField(max_length=10000,default="key")


class EDIT_Popup_Serializers(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    Category = serializers.CharField(max_length=1000,default="Domain")
    Method = serializers.CharField(max_length=100,default="append")
    Heading = serializers.CharField(max_length=1000,default="Domain")
    Text = serializers.CharField(max_length=1000,default="Domain")

class EDIT_Popup_State_Serializers(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    Category = serializers.CharField(max_length=1000,default="Domain")
    Action =  serializers.CharField(max_length=1000,default="Domain")


class Add_Engine_Serializer(serializers.Serializer):
    Domain = serializers.CharField(max_length=100,default="Domain")
    Link = serializers.CharField(max_length=10000,default="Domain")

