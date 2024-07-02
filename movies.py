import datetime
import smtplib


def Maharaja():
    print("yes maharaja movie tickets are available!!")
    booker=int(input("how many tickets do you want?"))
    print(f"yes {booker} tickets are available.")
    one_ticket=160
    gst=30
    total=one_ticket*booker+gst
    print(f"your total bill is {total}")
    f=open("bill.txt","a")
    f.write(f"your total bill is {total}")
    print("you can pay through gpay or paytm")
    print("your ticket booking is confirmed..")
    x=datetime.datetime.now()
    print(f"your ticket is booked on {x}")
    person=input("enter your mail id..")
    receiver_mail=f"{person}"
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("shobipriyashobipriya7@gmail.com","zamt vnry vyol glbc")
    message="your maharaja movie ticket is confirmed"
    s.sendmail("shobipriyashobipriya7@gmail.com",receiver_mail,message)
    s.quit()
    print("email send successfully..")
    
    
def Aranmanai():
    print("yes aranmanai 4 movie tickets are available..")
    booker=int(input("how many tickets do you want?"))
    print(f"yes {booker} tickets are available.")
    one_ticket=160
    gst=30
    total=one_ticket*booker+gst
    print(f"your total bill is {total}")
    f=open("bill.txt","a")
    f.write(f"your total bill is {total}")
    print("you can pay through gpay or paytm")
    print("your ticket booking is confirmed..")
    x=datetime.datetime.now()
    print(f"your ticket is booked on {x}")
    person=input("enter your mail id..")
    receiver_mail=f"{person}"
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("shobipriyashobipriya7@gmail.com","zamt vnry vyol glbc")
    message="your Aranmanai 4  movie ticket is confirmed"
    s.sendmail("shobipriyashobipriya7@gmail.com",receiver_mail,message)
    s.quit()
    print("email send successfully..")
    
def Karudan():
    print("yes karudan movie tickets are available")
    booker=int(input("how many tickets do you want?"))
    print(f"yes {booker} tickets are available.")
    one_ticket=160
    gst=30
    total=one_ticket*booker+gst
    print(f"your total bill is {total}")
    f=open("bill.txt","a")
    f.write(f"your total bill is {total}")
    print("you can pay through gpay or paytm")
    print("your ticket booking is confirmed..")
    x=datetime.datetime.now()
    print(f"your ticket is booked on {x}")
    person=input("enter your mail id..")
    receiver_mail=f"{person}"
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("shobipriyashobipriya7@gmail.com","zamt vnry vyol glbc")
    message="your Karudan movie ticket is confirmed "
    s.sendmail("shobipriyashobipriya7@gmail.com",receiver_mail,message)
    s.quit()
    print("email send successfully..")
    
def Star():
    print("yes star movie tickets are available!")
    booker=int(input("how many tickets do you want?"))
    print(f"yes {booker} tickets are available.")
    one_ticket=160
    gst=30
    total=one_ticket*booker+gst
    print(f"your total bill is {total}")
    f=open("bill.txt","a")
    f.write(f"your total bill is {total}")
    print("you can pay through gpay or paytm")
    print("your ticket booking is confirmed..")
    x=datetime.datetime.now()
    print(f"your ticket is booked on {x}")
    person=input("enter your mail id..")
    receiver_mail=f"{person}"
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("shobipriyashobipriya7@gmail.com","zamt vnry vyol glbc")
    message="your Star movie ticket is confirmed"
    s.sendmail("shobipriyashobipriya7@gmail.com",receiver_mail,message)
    s.quit()
    print("email send successfully..")
    
    
    
    
