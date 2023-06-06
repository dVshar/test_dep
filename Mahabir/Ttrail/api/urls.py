from django.urls import path,include
from .views import *

urlpatterns = [
    path('navbarView',Navbar_View.as_view(),name="Navbar_url"),            #* Navbar
    path('aboutView',About_View.as_view(),name="About_url"),               #* About
    path('bannerView',Banner_View.as_view(),name="Banner_url"),            #* Banner
    path('nearbyView',Nearby_View.as_view(),name="Nearby_url"),            #* Nearby
    path('imagesView',Images_View.as_view(),name="Images_url"),            #* Images
    path('footerView',Footer_View.as_view(),name="Footer_url"),            #* Footer
    path('servicesView',Services_View.as_view(),name="Services_url"),      #* Services
    path('linksView',Links_View.as_view(),name="Links_url"),               #* Links
    path('galleryView',Gallery_View.as_view(),name="Gallery_url"),         #* Gallery
    path('popupView',Addpop_View.as_view(),name="Popup_url"),              #* Popups
    path('navbarView/edit',EDIT_Menu_View.as_view(),name="Navbar_url"),                                         #*:- Navbar 
    path('aboutView/edit',EDIT_aboutView.as_view(),name="About_url"),                                           #* About Data edit
    path('bannerView/edit',EDIT_Nearby_Banner_append_delete_View.as_view(),name="Banner_url"),                  #*:- Banner,Nearby
    path('imagesView/edit',EDIT_Images_View.as_view(),name="Images_url"),                                       #*:- Images
    path('footerView/edit',Footer_View.as_view(),name="Footer_url"),                                            #todo:- Footer
    path('servicesView/edit',EDIT_Services_View.as_view(),name="Services_url"),                                      #*:- Services
    path('linksView/edit',EDIT_Social_Links_View.as_view(),name="Links_url"),                                   #*:- Links
    path('galleryView/edit/ed',EDIT_Gallery_enable_disable_View.as_view(),name="Gallery_url"),                  #* Gallery edit state
    path('galleryView/edit/append_remove',EDIT_Gallery_append_delete_View.as_view(),name="Gallery_url"),        #* Gallery Apped and remove
    path('popupView/edit',EDIT_Popups_View.as_view(),name="popup_url"),                                         #*:- Popup EDIT
    path('popupView/edit/state',EDIT_Popup_State.as_view(),name="popup_state"),  
    path('add_booking_engine',Add_Engine_View.as_view(),name="booking_engine_add"),  
]