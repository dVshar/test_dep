from django.shortcuts import render
from django.shortcuts import redirect
from .util import *
from Mahabir.settings import RAZORPAY_API_KEY,RAZORPAY_SECRET_KEY
import razorpay
from .models import *
from django.http import HttpResponse,JsonResponse
import json
from django.contrib.sites.shortcuts import get_current_site

client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_SECRET_KEY))

# Create your views here.
def landing(request):
    # try:
        full_url = ''.join(get_current_site(request).domain)
        print(full_url) #eazotel.com
        hit_domain=returnDomain(full_url)
        domain = getDomain(hit_domain)
        
        menu = Menu.objects.get(Domain=domain)
        banner = Banner.objects.get(Domain=domain)
        body_image = Body_Image.objects.get(Domain=domain)
        about = About.objects.get(Domain=domain)
        places= Nearby_places.objects.get(Domain=domain)
        services= Services.objects.get(Domain=domain)
        footer= Footer.objects.get(Domain=domain)
        social_links= Social_Links.objects.get(Domain=domain)
        Inf_Popup = Popups.objects.get(Domain=domain,Category="Information")
        prom_Popup = Popups.objects.get(Domain=domain,Category="Promotional")
        engine_link = Booking_Engine_Links.objects.get(Domain=domain)



        context={
            'Menu':menu,
            'Banner':banner,
            'Body_Images':body_image,
            'About':about,
            'Places':places,
            'Services':services,
            'Footer':footer,
            'Social_Links':social_links,
            'Promotional_popup':prom_Popup,
            'Notice_popup':Inf_Popup,
            'Engine':engine_link
        }
        print("yes")
        return render(request,"Ttrail/index.html",context)
    # except:
    #     return HttpResponse("404")



def About1(request): #hotelname.domain
    full_url = ''.join(get_current_site(request).domain)
    print(full_url)
    hit_domain=returnDomain(full_url)
    domain = getDomain(hit_domain)


    menu = Menu.objects.get(Domain=domain)
    banner = Banner.objects.get(Domain=domain)
    body_image = Body_Image.objects.get(Domain=domain)
    about = About.objects.get(Domain=domain)
    places= Nearby_places.objects.get(Domain=domain)
    services= Services.objects.get(Domain=domain)
    footer= Footer.objects.get(Domain=domain)
    social_links= Social_Links.objects.get(Domain=domain)

    context={
        'Menu':menu,
        'Banner':banner,
        'Body_Images':body_image,
        'Places':places,
        'Services':services,
        'About':about,
        'Footer':footer,
        'Social_Links':social_links
    }
    return render(request,"Ttrail/about.html",context)



#* ON CLICK OF BOOK NOW
def Booking(request):
    if request.method=="POST":
        room_type = request.POST['room']
        checkin = request.POST['form_book_checkin']
        checkout = request.POST['form_book_checkout']
        child = request.POST['kid']
        adult = request.POST['adult']
        room_type = room_type.split("_")

        data = {
            'Room':room_type[0],
            'Price':room_type[1],
            'Checkin':checkin,
            'Checkout':checkout,
            'Child':child,
            'Adult':adult

        }
        print(data)
        code = encrypt_data(data)

        return redirect('checkout/'+code)
    return render(request,"Ttrail/booking.html")       #booking

def BookingPost(request,data):
    detail = decrypt_data(data)
    if request.method=="POST":
        room_type = request.POST['room']
        if(room_type=="delux_1500"):
            type=1
        if(room_type=="superdelux_2000"):
            type=2
        if(room_type=="premium_2500"):
            type=3
        if(room_type=="suite_3500"):
            type=4

        room = Rooms.objects.get(Type=type)

        if(room.Available):
            context={
            'checkin':request.POST['form_book_checkin'],
            'checkout':request.POST['form_book_checkout'],
            'child':request.POST['child'],
            'adult':request.POST['adult'],
            "Available":True,
            "rooms":room,
            "Available_room":True

            }
        else:
            context={
            'checkin':request.POST['form_book_checkin'],
            'checkout':request.POST['form_book_checkout'],
            'child':request.POST['child'],
            'adult':request.POST['adult'],
            "Available":False,
            }
        return render(request,"Ttrail/bookingPost.html",context)

    room = Rooms.objects.get(Type=1)
    if (room.Available):
        context={
                'checkin':detail['checkin'],
                'checkout':detail['checkout'],
                'child':detail['child'],
                'adult':detail['adult'],
                "type":"delux_1500",
                "rooms":room,
                "Available":True,
                "Available_room":True

            }
    else:
         context={
                'checkin':detail['checkin'],
                'checkout':detail['checkout'],
                'child':detail['child'],
                'adult':detail['adult'],
                "type":"delux_1500",
                "Available":False

            }
    return render(request,"Ttrail/bookingPost.html",context)

def Room_Checkout(request):
    token = request.GET.get('token')
    try:
        data = decrypt_data(token) 
        print(data['Price'])
        amount_s=float(data['Price'])*100
        print(amount_s)
        DATA = {
        "amount": amount_s,
        "currency": "INR",
        "receipt": "receipt#1",
        "payment_capture":'1'
        }
        # print(DATA)
        payment=client.order.create(data=DATA)
        # print(payment)
        context={
            "amount":amount_s,
            "price":data['Price'],
            "payment":payment,
            "checkin":data['Checkin'],
            "checkout":data['Checkout'],
            'Child':data['Kid'],
            'Adult':data['Adult'],
            'Type':data['type']
        }
        
        Order = Order_create.objects.create(order_id=payment['id'],amount=data['Price'],adults=data['Adult'],kids=data['Kid'],checkin_date=data['Checkin'],checkout_date=data['Checkout'],Type =data['type']).save()
        return render(request,"Ttrail/Checkout.html",context)
    except:
        return HttpResponse('Something weird happen try again pls')
    

def Encode_Fetch(request):
    #FROM USER DISABLE AND ENABLE IN BASE_dash.html
    #COMING DATA FROM FETCH API
    data=json.loads(request.body)
    Price = data['Price']
    Checkin = data['Checkin']
    Checkout = data['Checkout']
    Adult = data['Adult']
    Kid = data['Kid']
    Type = data['type']

    token = encrypt_data(data)
    

    return JsonResponse({"message":token})


def Contact(request):
    full_url = ''.join(get_current_site(request).domain)
    print(full_url)
    hit_domain=returnDomain(full_url)
    domain = getDomain(hit_domain)

    menu = Menu.objects.get(Domain=domain)
    banner = Banner.objects.get(Domain=domain)
    body_image = Body_Image.objects.get(Domain=domain)
    about = About.objects.get(Domain=domain)
    places= Nearby_places.objects.get(Domain=domain)
    services= Services.objects.get(Domain=domain)
    footer= Footer.objects.get(Domain=domain)
    social_links= Social_Links.objects.get(Domain=domain)

    context={
        'Menu':menu,
        'Banner':banner,
        'Footer':footer,
        'Social_Links':social_links
    }
    return render(request,"Ttrail/contact.html",context)


def Checkout(request,token):
    try:
        data = decrypt_data(token) 
        print(data['Price'])
        amount_s=float(data['Price'])*100
        print(amount_s)
        DATA = {
        "amount": amount_s,
        "currency": "INR",
        "receipt": "receipt#1",
        "payment_capture":'1'
        }
        # print(DATA)
        payment=client.order.create(data=DATA)
        # print(payment)
        context={
            "amount":amount_s,
            "price":data['Price'],
            "payment":payment,
            "checkin":data['Checkin'],
            "checkout":data['Checkout'],
            'Child':data['Child'],
            'Adult':data['Adult']
        }
        Order = Order_create.objects.create(order_id=payment['id'],amount=data['Price'],adults=data['Adult'],kids=data['Child'],checkin_date=data['Checkin'],checkout_date=data['Checkout']).save()
        return render(request,"Ttrail/Checkout.html",context)
    except:
        return HttpResponse('Something weird happen try again pls')


def Success_Payment(request):
    razorpay_payment_id = request.GET.get('razorpay_payment_id')
    razorpay_order_id = request.GET.get('razorpay_order_id')
    razorpay_signature = request.GET.get('razorpay_signature')
    name = request.GET.get('name')
    email = request.GET.get('email')
    number = request.GET.get('phone')


    try:
        order = Order_create.objects.get(order_id=razorpay_order_id)
        order.Name=name
        order.email=email
        order.number=number
        order.payment_id=razorpay_payment_id
        order.signature=razorpay_signature
        order.is_paid=True
        orderid = str(razorpay_order_id)
        paymentid = str(razorpay_payment_id)
        checkin = str(order.checkin_date)
        checkout = str(order.checkout_date)
        adult = str(order.adults)
        kid = str(order.kids)
        amount = str(order.amount)

        order.save()
        sendMAIL(
            name=name,
            email_to=email,
            paymentid=paymentid,
            number=number,
            date=checkin,
            dateout=checkout,
            adult=adult,
            kid=kid,
            amount=amount,
            order_id=orderid

        )
        get_ord = Order_create.objects.get(order_id=razorpay_order_id)
        context = {
            'order':get_ord
        }
        return render(request,"Ttrail/afterPayment/Success.html",context)

        
    except:
        return HttpResponse('something weird happen')

def Fail_Payment(request):
    razorpay_order_id = request.GET.get('razorpay_order_id')
    try:
        # order = Order_create.objects.get(order_id=razorpay_order_id)

        # order.delete()

        # return render(request,"Ttrail/Users/Failed.html")
        return HttpResponse('failed')
        
    except:
        return HttpResponse('something weird happen')

def Gallery1(request):
    full_url = ''.join(get_current_site(request).domain)
    print(full_url)
    hit_domain=returnDomain(full_url)
    domain = getDomain(hit_domain)

    menu = Menu.objects.get(Domain=domain)
    banner = Banner.objects.get(Domain=domain)
    footer= Footer.objects.get(Domain=domain)
    social_links= Social_Links.objects.get(Domain=domain)
    gallery = Gallery.objects.filter(Domain=domain)

    context={
        'Menu':menu,
        'Banner':banner,
        'Footer':footer,
        'Social_Links':social_links,
        'Gallery':gallery
    }
    return render(request,"Ttrail/gallery.html",context)


def Events(request):
    full_url = ''.join(get_current_site(request).domain)
    print(full_url)
    hit_domain=returnDomain(full_url)
    domain = getDomain(hit_domain)

    menu = Menu.objects.get(Domain=domain)
    banner = Banner.objects.get(Domain=domain)
    body_image = Body_Image.objects.get(Domain=domain)
    about = About.objects.get(Domain=domain)
    places= Nearby_places.objects.get(Domain=domain)
    services= Services.objects.get(Domain=domain)
    footer= Footer.objects.get(Domain=domain)
    social_links= Social_Links.objects.get(Domain=domain)

    context={
        'Menu':menu,
        'Banner':banner,
        'Body_Images':body_image,
        'About':about,
        'Places':places,
        'Services':services,
        'Footer':footer,
        'Social_Links':social_links
    }
    return render(request,"Ttrail/events.html",context)


def Rooms_Hotel(request):
    full_url = ''.join(get_current_site(request).domain)
    print(full_url)
    hit_domain=returnDomain(full_url)
    domain = getDomain(hit_domain)
    menu = Menu.objects.get(Domain=domain)
    banner = Banner.objects.get(Domain=domain)
    body_image = Body_Image.objects.get(Domain=domain)
    about = About.objects.get(Domain=domain)
    places= Nearby_places.objects.get(Domain=domain)
    services= Services.objects.get(Domain=domain)
    footer= Footer.objects.get(Domain=domain)
    social_links= Social_Links.objects.get(Domain=domain)

    context={
        'Menu':menu,
        'Banner':banner,
        'Body_Images':body_image,
        'About':about,
        'Places':places,
        'Services':services,
        'Footer':footer,
        'Social_Links':social_links
    }
    return render(request,"Ttrail/rooms.html",context)


def Restaurants(request):
    full_url = ''.join(get_current_site(request).domain)
    print(full_url)
    hit_domain=returnDomain(full_url)
    domain = getDomain(hit_domain)

    menu = Menu.objects.get(Domain=domain)
    banner = Banner.objects.get(Domain=domain)
    body_image = Body_Image.objects.get(Domain=domain)
    about = About.objects.get(Domain=domain)
    places= Nearby_places.objects.get(Domain=domain)
    services= Services.objects.get(Domain=domain)
    footer= Footer.objects.get(Domain=domain)
    social_links= Social_Links.objects.get(Domain=domain)

    context={
        'Menu':menu,
        'Banner':banner,
        'Body_Images':body_image,
        'About':about,
        'Places':places,
        'Services':services,
        'Footer':footer,
        'Social_Links':social_links
    }
    return render(request,"Ttrail/restaurant.html",context)


def Locations(request):
    full_url = ''.join(get_current_site(request).domain)
    print(full_url)
    hit_domain=returnDomain(full_url)
    domain = getDomain(hit_domain)

    menu = Menu.objects.get(Domain=domain)
    banner = Banner.objects.get(Domain=domain)
    body_image = Body_Image.objects.get(Domain=domain)
    places= Nearby_places.objects.get(Domain=domain)
    services= Services.objects.get(Domain=domain)
    footer= Footer.objects.get(Domain=domain)
    social_links= Social_Links.objects.get(Domain=domain)

    context={
        'Menu':menu,
        'Banner':banner,
        'Body_Images':body_image,
        'Places':places,
        'Footer':footer,
        'Services':services,
        'Social_Links':social_links
    }
    return render(request,"Ttrail/location.html",context)


def Services1(request):
    full_url = ''.join(get_current_site(request).domain)
    print(full_url)
    hit_domain=returnDomain(full_url)
    domain = getDomain(hit_domain)

    menu = Menu.objects.get(Domain=domain)
    banner = Banner.objects.get(Domain=domain)
    body_image = Body_Image.objects.get(Domain=domain)
    about = About.objects.get(Domain=domain)
    places= Nearby_places.objects.get(Domain=domain)
    services= Services.objects.get(Domain=domain)
    footer= Footer.objects.get(Domain=domain)
    social_links= Social_Links.objects.get(Domain=domain)

    context={
        'Menu':menu,
        'Banner':banner,
        'Footer':footer,
        'Services':services,
        'Social_Links':social_links
    }
    return render(request,"Ttrail/services.html",context)

def Recreation(request):
    full_url = ''.join(get_current_site(request).domain)
    print(full_url)
    hit_domain=returnDomain(full_url)
    domain = getDomain(hit_domain)
    
    menu = Menu.objects.get(Domain=domain)
    banner = Banner.objects.get(Domain=domain)
    body_image = Body_Image.objects.get(Domain=domain)
    about = About.objects.get(Domain=domain)
    places= Nearby_places.objects.get(Domain=domain)
    services= Services.objects.get(Domain=domain)
    footer= Footer.objects.get(Domain=domain)
    social_links= Social_Links.objects.get(Domain=domain)

    context={
        'Menu':menu,
        'Banner':banner,
        'Body_Images':body_image,
        'Footer':footer,
        'Social_Links':social_links
    }
    return render(request,"Ttrail/recreation.html",context)

