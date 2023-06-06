from rest_framework.response import Response
from rest_framework.decorators import APIView
from ..models import *
from rest_framework import status, generics
from rest_framework.decorators import api_view
from .serializers import *
from .utils import *

#* Navbar
class Navbar_View(APIView):
    def post(self,request):
        try:
            signup = NavbarSerializer(data=request.data)
            if signup.is_valid():
                Domain = Create_Domain(signup["HotelName"].value)
                navbar_check = Menu.objects.filter(Hotel_name=signup["HotelName"].value).count()
                if navbar_check==0:
                    navbar_add = Menu.objects.create(
                        Domain = Domain,
                        Hotel_name = signup["HotelName"].value,
                        Number = signup["HotelNumber"].value
                    ).save()
                    return Response({"Status":True,"Domain":Domain})
                else:
                    return Response({"Status":False,"Message":"Hotel Name Exists"})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Status":False,"Message":"Some Problem Occured"}
                )
        

#* About
class About_View(APIView):
    def post(self,request):
        try:
            signup = AboutSerializer(data=request.data)
            if signup.is_valid():
                Hotelname = signup["HotelName"].value
                Heading = "About "+Hotelname
                Text="At "+Hotelname+", we are dedicated to providing our guests with exceptional service, luxurious accommodations, and an unforgettable experience. Our commitment to excellence is evident in every aspect of our hotel, from our beautifully designed guest rooms to our top-notch amenities and personalized services.Our hotel offers convenient access to the area's top attractions. Whether you are traveling for business or leisure, our hotel is the perfect destination for your stay.Our team of highly trained professionals is here to ensure that your stay is as comfortable and enjoyable as possible. From our friendly front desk staff to our housekeeping team, everyone at "+Hotelname+" is dedicated to making your stay a memorable one.We offer a wide range of amenities to our guests. Our goal is to provide our guests with everything they need to have a comfortable and relaxing stay.At "+Hotelname+", we are committed to sustainability and minimizing our impact on the environment. We have implemented a number of environmentally friendly practices throughout our hotel, including energy-efficient lighting, recycling, reducing water usage.Thank you for considering "+Hotelname+" for your next stay. We look forward to welcoming you and providing you with an exceptional hotel experience."
                
                about_add = About.objects.create(
                    Domain = signup["Domain"].value,
                    Heading = Heading,
                    Text = Text
                ).save()
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Status":False,"Message":"Some Problem Occured"}
                )
        
#* Banner
class Banner_View(APIView):
    def post(self,request):
        try:
            signup = BannerSerializer(data=request.data)
            if signup.is_valid():
                Images = [
                    {"Heading":"Your Best Memories are here",
                    "Image":"https://www.new-delhi-hotels.com/blog/wp-content/uploads/2012/09/delhi-luxury-hotels.jpg"
                    },
                    {"Heading":"Best view from Room",
                    "Image":"https://www.lux-review.com/wp-content/uploads/2020/04/6-Factors-Luxury-Hotels-Have-in-Common-and-Why.jpg"
                    },
                    {"Heading":"Amazing Stay Place",
                    "Image":"https://www.kayak.co.in/rimg/himg/38/95/99/leonardo-1283859-Rooftop_Revere_Private_Deck_O-871946.jpg?width=1366&height=768&crop=true"
                    }
                ]
                banner_add = Banner.objects.create(
                    Domain = signup["Domain"].value,
                    Category = "Banner",
                    Images = Images
                ).save()
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
#* Nearby
class Nearby_View(APIView):
    def post(self,request):
        try:
            signup = NearbySerializer(data=request.data)
            if signup.is_valid():
                Images = [
                    {"Heading":"Peak of mountain",
                    "Image":"https://img.traveltriangle.com/blog/wp-content/uploads/2020/02/Cover-image-of-Hotels-Near-Gangotri.jpg"
                    },
                    {"Heading":"Taj Mahal",
                    "Image":"https://static.toiimg.com/photo/67896140.cms"
                    },
                    {"Heading":"Bridge",
                    "Image":"https://img.traveltriangle.com/blog/wp-content/uploads/2020/02/Cover-image-of-12-Hotels-Near-Mumbai.jpg"
                    },
                    {"Heading":"Green Environment",
                    "Image":"https://www.fabhotels.com/blog/wp-content/uploads/2019/07/Places-to-Visit-in-Lonavala_600.jpg"
                    }
                ]
                nearby_add = Nearby_places.objects.create(
                    Domain = signup["Domain"].value,
                    Category = "Nearby",
                    Images = Images
                ).save()
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
#* Images
class Images_View(APIView):
    def post(self,request):
        try:
            signup = ImagesSerializer(data=request.data)
            if signup.is_valid():
                Images = [
                    {"Image":"https://www.liveabout.com/thmb/NqnDvmY2gq9gPw94L78_xei2J7k=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/hotel_room-627892060-5a7a30d1642dca00370179e6.jpg"},
                    {"Image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCj8r0Jy4tWGLqCSMs8xVKd8ydY8tiIjr7jSMLwfR4kw&usqp=CAU&ec=48665699"},
                    {"Image":"https://decortips.com/wp-content/uploads/2020/07/The-common-areas-of-Hotel-Alhambra-in-Granada.-e1594124451973.jpg"},
                    {"Image":"https://im.rediff.com/getahead/2013/dec/23travel7.jpg?w=670&h=900"}
                ]
                images_add = Body_Image.objects.create(
                    Domain = signup["Domain"].value,
                    Category = "Images",
                    Images = Images
                ).save()
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
#* Footer
class Footer_View(APIView):
    def post(self,request):
        try:
            signup = FooterSerializer(data=request.data)
            if signup.is_valid():
                nearby_add = Footer.objects.create(
                    Domain = signup["Domain"].value,
                    Start_date = signup["Start_date"].value,
                    Address = signup["Address"].value,
                    State = signup["State"].value,
                    City = signup["City"].value,
                    Email = signup["Email"].value
                ).save()
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
#* Services
class Services_View(APIView):
    def post(self,request):
        try:
            signup = ServicesSerializer(data=request.data)
            if signup.is_valid():
                service_add = Services.objects.create(
                    Domain = signup["Domain"].value,
                ).save()
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
#* Social Links
class Links_View(APIView):
    def post(self,request):
        try:
            signup = LinksSerializer(data=request.data)
            if signup.is_valid():
                service_add = Social_Links.objects.create(
                    Domain = signup["Domain"].value,
                    Facebook = "https://facebook.com/"+signup["Domain"].value,
                    Instagram = "https://instagram.com/"+signup["Domain"].value,
                    Linkedin = "https://linkedin.com/"+signup["Domain"].value,
                    Tripadvisor = "https://tripadvisor.com/"+signup["Domain"].value,
                    Twitter = "https://twitter.com/"+signup["Domain"].value
                ).save()
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
#* Gallery
class Gallery_View(APIView):
    def post(self,request):
        try:
            signup = GallerySerializer(data=request.data)
            if signup.is_valid():
                categories = ["Events","Restaurants","Hotels","Nearby","View","Rooms","Lobby","Bar","Playzone"]
                Images = [
                    {"Image":"https://www.fielmente.com/wp-content/uploads/2022/05/1.jpg"},
                ]
                for i in categories:

                    images_add = Gallery.objects.create(Domain = signup["Domain"].value,Category =i,Images = Images ).save()
                
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
class Addpop_View(APIView):
    def post(self,request):
        try:
            signup = PopupSerializer(data=request.data)
            if signup.is_valid():
                domain = signup["Domain"].value
                inf_popup = [
                    {"Heading":"Your Informational Popup","Text":"Add your Custom Popup for Information here"}
                ]
                promotional_popup = [
                    {"Heading":"Your Promotional Popup","Text":"Add your Promotional Popup for Information here"}
                ]
                inf_popups = Popups.objects.create(Domain=domain,Category="Information",Ads=inf_popup).save()
                pro_popups = Popups.objects.create(Domain=domain,Category="Promotional",Ads=promotional_popup).save()
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
#! EDIT VIEWS

#*:- About View
class EDIT_aboutView(APIView):
    def post(self,request):
        try:
            signup = About_edit_Serializer(data=request.data)
            if signup.is_valid():
                domain = signup["Domain"].value
                Heading = signup["Heading"].value
                Image = signup["Image"].value
                Text = signup["Text"].value

                user = About.objects.get(Domain=domain)
                user.Heading = Heading
                user.Image = Image
                user.Text = Text
                user.save()
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        

class EDIT_Gallery_enable_disable_View(APIView):
    def post(self,request):
        try:
            signup = Gallery_edit_Serializer(data=request.data)
            if signup.is_valid():
                domain = signup["Domain"].value
                Category = signup["Category"].value
                action = signup["action"].value

                gallery = Gallery.objects.get(Domain=domain,Category=Category)
                if action == "enable":
                    gallery.active=True
                else:
                    gallery.active=False

                gallery.save()
                
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        

class EDIT_Gallery_append_delete_View(APIView):
    def post(self,request):
        try:
            signup = Gallery_edit_append_Serializer(data=request.data)
            if signup.is_valid():
                domain = signup["Domain"].value
                Method=signup["Method"].value
                Category = signup["Category"].value
                Image = signup["Image"].value
                
                gallery = Gallery.objects.get(Domain=domain,Category=Category)
                if Method == "append":
                    processed_image = [{"Image":Image}]
                    images_list = gallery.Images
                    images_list=images_list+processed_image
                    gallery.Images=images_list
                else:
                    processed_image = {"Image":Image}
                    images_list=gallery.Images
                    images_list.remove(processed_image)
                    gallery.Images=images_list
                gallery.save()
                
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        

class EDIT_Nearby_Banner_append_delete_View(APIView):
    def post(self,request):
        try:
            signup = Nearby_Banner_edit_append_Serializer(data=request.data)
            if signup.is_valid():
                domain = signup["Domain"].value
                Method=signup["Method"].value
                Category = signup["Category"].value
                Heading = signup["Heading"].value
                Image = signup["Image"].value
                
                if Method == "append":
                    list_to_add = [{"Heading":Heading,"Image":Image}]
                    if Category=="Banner":
                        banner = Banner.objects.get(Domain=domain)
                        banner.Images = banner.Images+list_to_add
                        banner.save()
                    else:
                        nearby = Nearby_places.objects.get(Domain=domain)
                        nearby.Images = nearby.Images+list_to_add
                        nearby.save()
                else:
                    dict_to_remove = {"Heading":Heading,"Image":Image}
                    if Category=="Banner":
                        banner = Banner.objects.get(Domain=domain)
                        list_of_banner = banner.Images
                        list_of_banner.remove(dict_to_remove)
                        banner.save()
                    else:
                        nearby = Nearby_places.objects.get(Domain=domain)
                        list_of_nearby = nearby.Images
                        list_of_nearby.remove(dict_to_remove)
                        nearby.save()
                
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

class EDIT_Social_Links_View(APIView):
    def post(self,request):
        try:
            signup = Social_Links_Edit_Serializers(data=request.data)
            if signup.is_valid():
                domain = signup["Domain"].value
                facebook=signup["facebook"].value
                instagram = signup["instagram"].value
                linkedin = signup["linkedin"].value
                tripadvisor = signup["tripadvisor"].value
                twitter = signup["twitter"].value
                
                social_links = Social_Links.objects.get(Domain=domain)
                social_links.Facebook=facebook
                social_links.Instagram = instagram
                social_links.Tripadvisor = tripadvisor
                social_links.Twitter = twitter
                social_links.Linkedin = linkedin
                social_links.save()
                
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
class EDIT_Images_View(APIView):
    def post(self,request):
        try:
            signup = Images_edit_append_Serializer(data=request.data)
            if signup.is_valid():
                domain = signup["Domain"].value
                Method = signup["Method"].value
                Image = signup["Image"].value

                gallery = Body_Image.objects.get(Domain=domain)
                if Method == "append":
                    processed_image = [{"Image":Image}]
                    gallery.Images=gallery.Images+processed_image
                else:
                    processed_image = {"Image":Image}
                    images_list=gallery.Images
                    images_list.remove(processed_image)
                    gallery.Images=images_list
                gallery.save()
                
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
class EDIT_Menu_View(APIView):
    def post(self,request):
        try:
            signup = Menu_Management_Serializers(data=request.data)
            if signup.is_valid():
                domain = signup["Domain"].value
                key = signup["key"].value
                value = signup["value"].value=="true"
                data={
                    "domain":domain,
                    "key":key,
                    "value":value
                }

                Mongocmd_Edit_menu(data)
                

                
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )


class EDIT_Services_View(APIView):
    def post(self,request):
        try:
            signup = Services_Management_Serializers(data=request.data)
            if signup.is_valid():
                domain = signup["Domain"].value
                key = signup["key"].value
                value = signup["value"].value=="true"
                
                data={
                    "domain":domain,
                    "key":key,
                    "value":value
                }
                Mongocmd_Edit_services(data)
                
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )



class EDIT_Popups_View(APIView):
    def post(self,request):
        try:
            signup = EDIT_Popup_Serializers(data=request.data)
            if signup.is_valid():
                domain = signup["Domain"].value
                Category = signup["Category"].value
                Method = signup["Method"].value
                Heading = signup["Heading"].value
                Text = signup["Text"].value

                Popup_get = Popups.objects.get(Domain=domain,Category=Category)
                if Method=="append":
                    append = [{"Heading":Heading,"Text":Text}]
                    Popup_get.Ads=Popup_get.Ads+append
                else:
                    pop = {"Heading":Heading,"Text":Text}
                    ads = Popup_get.Ads
                    ads.remove(pop)
                    Popup_get.Ads = ads
                    
                Popup_get.save()
                
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )


class EDIT_Popup_State(APIView):
    def post(self,request):
        try:
            signup = EDIT_Popup_State_Serializers(data=request.data)
            if signup.is_valid():
                domain = signup["Domain"].value
                Category = signup["Category"].value
                Action = signup["Action"].value


                Popup_get = Popups.objects.get(Domain=domain,Category=Category)
                if Action=="true":
                    Popup_get.Required=True
                else:
                    Popup_get.Required=False
                    
                Popup_get.save()
                
                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )


class Add_Engine_View(APIView):
    def post(self,request):
        try:
            signup = Add_Engine_Serializer(data=request.data)
            if signup.is_valid():
                
                Domain = signup["Domain"].value
                Link = signup["Link"].value

                link = Booking_Engine_Links.objects.create(
                    Domain = Domain,
                    EngineLink = Link
                ).save()

                return Response({"Status":True})
            else:
                return Response({"Status":False})

        except:
            return Response(
                    {"Message": "Some problem Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )