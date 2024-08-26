import os
from twilio.rest import Client
import pyttsx3

message='sir! someone is hacking your system'

def Speak(text):
    rate = 100 #Sets the default rate of speech
    engine = pyttsx3.init() #Initialises the speech engine
    voices = engine.getProperty('voices') #sets the properties for speech
    engine.setProperty('voice', voices[0].id) #Gender and type of voice
    engine.setProperty('rate', rate+50) #Adjusts the rate of speech
    engine.say(text) #tells Python to speak variable 'text'
    engine.runAndWait() #waits for speech to finish and then continues with program

#TWILIO_ACCOUNT_SID = os.environ.get('Account SID')
#TWILIO_AUTH_TOKEN = os.environ.get('Auth Token')
#TWILIO_PHONE_NUMBER = os.environ.get('+13158341226')
#YOUR_PHONE_NUMBER = os.environ.get('YOUR_PHONE_NUMBER')

TWILIO_ACCOUNT_SID='ACeaabcac2b6a092356d8c9acb5ee95464'
TWILIO_AUTH_TOKEN='feff271abc318b2076f26259b7b2ebf4'
TWILIO_PHONE_NUMBER='+13158341226'
YOUR_PHONE_NUMBER='+917397013168'


def send_sms(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        to=YOUR_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        body=message
    )

def send_alert(message):
    Speak(f"Alert: {message}")
    send_sms(message)

send_alert(message)
