import base64
import ast
import smtplib
from email.message import EmailMessage

EMAIL_HOST_USER = "github21git00@gmail.com"
EMAIL_HOST_PASSWORD = "phispisebkntmxpf"

def encrypt_data(data):
    sample_string=str(data)
    print(sample_string)
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    final = base64_bytes.decode("ascii")

    return final


def decrypt_data(data):
    base64_bytes = data.encode("ascii")
  
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    

    sample_string = ast.literal_eval(sample_string)
    
    return sample_string


def sendMAIL(name,paymentid,number,date,dateout,adult,kid,amount,order_id,email_to):
    msg = EmailMessage()
    msg['Subject'] = 'Booking Confirmation '+name+' - '+date
    msg['To'] = email_to
    msg['From'] = "github21git00@gmail.com"
    msg.set_content('<!DOCTYPE html><html><body><div style="background-color:rgb(73, 73, 255);padding:10px 20px;"><img src="https://media.licdn.com/dms/image/C4E03AQG3pp-WmN0aIg/profile-displayphoto-shrink_400_400/0/1658167340169?e=1680739200&v=beta&t=gqO6pSHS7-nT_e503gSHLoUm6lohrVZE0gfSBb_u_58" style="height: 100px;background-color:rgb(250, 249, 249);"><h2 style="font-family:Georgia,Times, serif;color:white;">Rangotsav</h2></div><div style="padding:20px 0px"><div style="height: 500px;width:400px"><p>Hello <strong>'+name+'</strong></p><p>Thankyou for booking with us, below are your details.</p> <div><table style="border-collapse: collapse;width:120%;height: 70px;"><tr><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;"><strong>Booking ID</strong></td><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;">'+ order_id +'</td></tr><tr><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;"><strong>Name</strong></td><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;">'+name+'</td></tr><tr><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;"><strong>Phone Number</strong></td><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;">'+number+'</td></tr><tr><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;"><strong>Email</strong></td><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;">'+email_to+'</td></tr><tr><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;"><strong>Check-in</strong></td><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;">'+date+'</td></tr><tr><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;"><strong>Check-out</strong></td><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;">'+dateout+'</td></tr><tr><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;"><strong>Adults</strong></td><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;">'+adult+'</td></tr><tr><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;"><strong>Kids</strong></td><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;">'+kid+'</td></tr><tr><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;"><strong>Total Payment</strong></td><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;">₹'+amount+'</td></tr><tr><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;"><strong>Payment ID</strong></td><td style="border: 1px solid rgb(14, 13, 13); padding: 8px;">'+paymentid+'</td></tr></table></div><div><p style="font-size: 13px;">Things to Carry</p><ul style="font-size: 11px;"><li>Swimwear / Nylon Clothes for the pool</li><li>A pair of flip-flops to roam around in the campsite</li><li>Personal Medications</li><li>Odomos (may not need but good to carry)</li><li>Personal Snacks and Beverages</li><li>Towels</li><li>A Campers Attitude</li></ul></div><hr style="border:1px solid black"><div><p style="font-size: 13px;"><strong>Cancellation Policy</strong></p><ul style="font-size: 11px;"><li>100% refund if cancelled 15 days before the date of the trip</li><li>Reschedule to an alternate date OR50% refund if cancelled 72 hours before the date of the trip</li><li>No refund if cancelled within 72 hours of the date of the trip</li></ul></div><hr style="border:1px solid black"><div style="text-align:center;font-size: 9px;"><p>Tents N’ Trails, Adoshi Dam, Khopoli, Maharashtra 410203 (Hyper link to google maps)</p><p><a href="mailto:info@tentsntrails.com">info@tentsntrails.com</a> | 87664 73243 | 93567 25673</p><p>Reg. Office: #M-6, 26th Main JP Nagar 1st Phase, Bangalore -560078</p></div></div></div></body></html>  ', subtype='html')
    
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD) 
        smtp.send_message(msg)


def getDomain(link):
    list_link = link.split('.')
    return list_link[0]



def returnDomain(full_url):
    if(full_url=="eazotel.com" or full_url=="127.0.0.1:8000" or full_url=="13.55.119.144"):
        domain = "metrostudio.eazotel.com"
        return domain
    else:
        return full_url