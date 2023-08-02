#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pywhatkit
from twilio.rest import Client
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 110)  # Speed of speech. Default is 200.
engine.setProperty('volume', 0.8)  # Volume level. Range is from 0.0 to 1.0.
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')  # Voice selection.

engine.say("please enter your value press one for whatsapp message press two for text message press three for email ")
engine.runAndWait()

print("welcome to message device")
print("please choose one service:")

print('''1.whatsapp
2.text
3.email
    ''')

x=int(input("enter what do you want:"))
if x == 1:
    print('''welcome to whatsapp service
    Note:- Please make sure the your whatsapp is login in webbrowser''')
    engine.say('''welcome to whatsapp service
               Note:- Please make sure the your whatsapp is login in webbrowser''')
    engine.runAndWait()
    
    engine.say('please enter mobile number to send the message and please start with country')
    engine.runAndWait()
    mob_no = str(input("please enter mobile number to send the message and please start with country: "))
    engine.say('please write your message:')
    engine.runAndWait()
    w_message= str(input("please write your message:"))
    engine.say('please enter hour')
    engine.runAndWait()
    hour= int(input("please enter hour:"))
    engine.say('please enter minutes ')
    engine.runAndWait()
    minutes =int(input("please enter minutes :"))
    
    pywhatkit.sendwhatmsg(mob_no, w_message, hour,minutes)
    print("sent message succesfully")
    engine.say('sent message succesfully ')
    engine.runAndWait()

    
elif x == 2:
    print('''welcome to text service''')
    engine.say('''welcome to text service
               Note:- Sign up for a Twilio account at Twilio web site and obtain your Account SID and Auth Token.
               Note:- if you send the any message to the number  you need to verification the number in twilio
    then message get sent''')
    engine.runAndWait()
    print('''Note:- Sign up for a Twilio account at https://www.twilio.com/ and obtain your Account SID and Auth Token.
   ''')
    
    print('''Note:- if you send the any message to the number  you need to verification the number in twilio
    then message get sent''')
    
    # Twilio account credentials
    engine.say('please enter Account SID ')
    engine.runAndWait()
    account_sid = input("please enter Account SID: ")
    
    engine.say('please enter Auth Token ')
    engine.runAndWait()
    auth_token = input("please enter Auth Token: ")
    
    
    # Create a Twilio client
    client = Client(account_sid, auth_token)
    
    engine.say('please enter your message ')
    engine.runAndWait()
    Massage = str(input("please enter your message:"))
    
    engine.say('please enter your Twilio Number start with plus sign')
    engine.runAndWait()
    Twilio_No = str(input("please enter your Twilio No : "))
    
    engine.say('please enter mobile number to send the message and please start with country code ')
    engine.runAndWait()
    receiver_No = str(input("please enter mobile number to send the message and please start with country code: "))
    
    message = client.messages.create(
        body= Massage,
        from_= Twilio_No,
        to= receiver_No
    )

    # Print the message SID
    print('Message SID:', message.sid)
    print("sent message succesfully")
    engine.say('sent message succesfully ')
    engine.runAndWait()
    
elif x == 3:
    
    print('''welcome to email service''')
    print('''Note:- two step verification on need to check up in email settings''')
    engine.say('''welcome to email service
               Note:- two step verification on need to check up in email settings''')
    engine.runAndWait()
    
    
    engine.say('please enter sender email ID ')
    engine.runAndWait()
    sender_email = str(input("please enter sender email ID :"))
    
    engine.say('please enter receiver_email ID ')
    engine.runAndWait()
    receiver_email = str(input("please enter receiver_email ID :"))
    
    engine.say('please enter your subject')
    engine.runAndWait()
    subject = str(input("please enter your subject: "))
    
    engine.say('please enter your message')
    engine.runAndWait()
    message = str(input("please enter your message:"))


    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    
    engine.say('please enter sender email ID')
    engine.runAndWait()
    username = str(input("please enter sender email ID :"))
    
    print('''after two step verification email give you secret key ''')
    engine.say('after two step verification email give you secret key')
    engine.runAndWait()
    
    engine.say('please enter secret key')
    engine.runAndWait()
    password = str(input("please enter secret key: "))

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as smtp:
            smtp.login(username, password)

            # Send the email
            smtp.send_message(msg)
            print('Email sent successfully.')
            engine.say('sent message succesfully ')
            engine.runAndWait()

    except Exception as e:
        print(f'Error: {e}')


# In[ ]:





# In[ ]:




