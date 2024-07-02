import datetime
import smtplib
import random

def vijay():
    
    voter=input("enter your email id..")
    receiver_mail=f"{voter}"
    otp_number=random.randint(0000,9999)
    print(receiver_mail,otp_number)
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("shobipriyashobipriya7@gmail.com","fqld djpc kxme pafq")
    message=f"your otp number is {otp_number} do not share with anyone.."
    message=f"your vote will be placed successfully.."
    s.sendmail("shobipriyashobipriya7@gmail.com",receiver_mail,message)
    s.quit()
    person=input("enter your otp number:")
    print(f" {person} is accepted..")
    print("your vote placed sucessfully..")
    x=datetime.datetime.now()
    f=open("vote.txt","a")
    f.write(f"vote of vijay is generated on {x}")
    print(f"your vote placed successfully on {x}")
    
def suriya():
    voter=input("enter your email id..")
    receiver_mail=f"{voter}"
    otp_number=random.randint(0000,9999)
    print(receiver_mail,otp_number)
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("shobipriyashobipriya7@gmail.com","fqld djpc kxme pafq")
    message=f"your otp number is {otp_number} do not share with anyone.."
    message=f"your vote will be placed successfully.."
    s.sendmail("shobipriyashobipriya7@gmail.com",receiver_mail,message)
    s.quit()
    person=input("enter your otp number:")
    print(f" {person} is accepted..")
    print("your vote placed sucessfully..")
    x=datetime.datetime.now()
    f=open("vote.txt","a")
    f.write(f"vote of suriya is generated on {x}")
    print(f"your vote placed successfully on {x}")
    
def ajith():
    voter=input("enter your email id..")
    receiver_mail=f"{voter}"
    otp_number=random.randint(0000,9999)
    print(receiver_mail,otp_number)
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("shobipriyashobipriya7@gmail.com","fqld djpc kxme pafq")
    message=f"your otp number is {otp_number} do not share with anyone.."
    message=f"your vote will be placed successfully.."
    s.sendmail("shobipriyashobipriya7@gmail.com",receiver_mail,message)
    s.quit()
    person=input("enter your otp number:")
    print(f" {person} is accepted..")
    print("your vote placed sucessfully..")
    x=datetime.datetime.now()
    f=open("vote.txt","a")
    f.write(f"vote of ajith is generated on {x}")
    print(f"your vote placed successfully on {x}")
    
def adharva():
    voter=input("enter your email id..")
    receiver_mail=f"{voter}"
    otp_number=random.randint(0000,9999)
    print(receiver_mail,otp_number)
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("shobipriyashobipriya7@gmail.com","fqld djpc kxme pafq")
    message=f"your otp number is {otp_number} do not share with anyone.."
    message=f"your vote will be placed successfully.."
    s.sendmail("shobipriyashobipriya7@gmail.com",receiver_mail,message)
    s.quit()
    person=input("enter your otp number:")
    print(f" {person} is accepted..")
    print("your vote placed sucessfully..")
    x=datetime.datetime.now()
    f=open("vote.txt","a")
    f.write(f"vote of adharva is generated on {x}")
    print(f"your vote placed successfully on {x}")
    
def siva_karthikeyan():
    voter=input("enter your email id..")
    receiver_mail=f"{voter}"
    otp_number=random.randint(0000,9999)
    print(receiver_mail,otp_number)
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("shobipriyashobipriya7@gmail.com","fqld djpc kxme pafq")
    message=f"your otp number is {otp_number} do not share with anyone.."
    message=f"your vote will be placed successfully.."
    s.sendmail("shobipriyashobipriya7@gmail.com",receiver_mail,message)
    s.quit()
    person=input("enter your otp number:")
    print(f" {person} is accepted..")
    print("your vote placed sucessfully..")
    x=datetime.datetime.now()
    f=open("vote.txt","a")
    f.write(f"vote of siva karthikeyan is generated on {x}")
    print(f"your vote placed successfully on {x}")
    
    
    
    
        

    
            
    
    

    