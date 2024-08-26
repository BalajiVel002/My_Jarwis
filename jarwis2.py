import pyttsx3
import speech_recognition as sr
import time
import random
import datetime

"""variables"""
r = sr.Recognizer()
keywords = [("jarvis", 1), ("hey jarvis", 1)]  # setting up our 'wake' words
source = sr.Microphone()  # setting up which mic we are using

"""Lists"""
hello_list = ["hello", "hi", "hey"]
how_are_you = ["how are you", "how are you doing"]
time_commands = ["what is the time", "tell me the time", "current time"]
day_commands = ["what day is it", "tell me the day", "current day"]
joke_commands = ["tell me a joke", "say something funny", "joke time"]
thank_commands = ["thank you", "thanks", "appreciate it"]
goodbye_commands = ["goodbye", "bye", "see you later"]

reply_hello_list = ["Hello, sir!", "Hi there!", "Hey!"]
reply_how_are_you = ["I'm functioning well, thank you!", "Pretty good, sir!", "I'm doing fine, thanks!"]
reply_unknown = ["I'm sorry sir, I did not understand your request", "Could you please repeat that?"]
reply_time = ["The time is {str_time}", "It's currently {str_time}", "The current time is {str_time}"]
reply_day = ["Today is {day_of_the_week}", "It's {day_of_the_week} today", "The day is {day_of_the_week}"]
reply_joke = ["Why don't scientists trust atoms? Because they make up everything!", 
              "I told my wife she should embrace her mistakes. She gave me a hug.",
              "What do you call fake spaghetti? An impasta."]
reply_thank = ["You're welcome, sir!", "Anytime!", "It was my pleasure."]
reply_goodbye = ["Goodbye, sir!", "Until next time!", "See you later!"]

"""Functions"""
def Speak(text):
    rate = 100  # Sets the default rate of speech
    engine = pyttsx3.init()  # Initialises the speech engine
    voices = engine.getProperty('voices')  # sets the properties for speech
    engine.setProperty('voice', voices[0].id)  # Gender and type of voice
    engine.setProperty('rate', rate + 50)  # Adjusts the rate of speech
    engine.say(text)  # tells Python to speak variable 'text'
    engine.runAndWait()  # waits for speech to finish and then continues with the program
    print("Speak sir...")
def callback(recognizer, audio):
    try:
        recognize_main(audio)  # Runs the function recognize_main
    except sr.UnknownValueError:  # if there is nothing understood
        print("Oops! Didn't catch that")  # prints to the screen error message

def start_recognizer():
    # print("Waiting for a keyword...Jarvis or Hey Jarvis")  # Prints to the screen
    print("Jarvis ready to listen...")
    r.listen_in_background(source, callback)  # Sets off the recognition sequence
    time.sleep(100000)  # keeps loop running
    
def recognize_main(audio):
    # r = sr.Recognizer()  # sets r variable
    # with sr.Microphone() as source:  # sets microphone
    #     print("Say something!")  # prints to the screen
    #     audio = r.listen(source)  # sets variable 'audio'
    # data = ""  # assigns user voice entry to variable 'data'
    print("Sent to the internet ....")
    try:
        data = r.recognize_google(audio)  # now uses Google speech recognition
        data = data.lower()  # makes all voice entries show as lower case
        print("You said: " + data)  # shows what the user said and what was recognized

        # Greetings
        if data in hello_list:
            hour = datetime.datetime.now().hour
            if 0 <= hour < 12:
                Speak("Good morning, sir")
            elif 12 <= hour < 18:
                Speak("Good Afternoon, Sir")
            else:
                Speak("Good Evening, Sir")
            time.sleep(2)
        elif data in how_are_you:
            Speak(random.choice(reply_how_are_you))
            time.sleep(2)
        elif any(command in data for command in time_commands):
            str_time = datetime.datetime.now().strftime("%H:%M")
            Speak(random.choice(reply_time).format(str_time=str_time))
            time.sleep(2)
        elif any(command in data for command in day_commands):
            day = datetime.datetime.today().weekday() + 1
            day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                        4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                        7: 'Sunday'}
            if day in day_dict.keys():
                day_of_the_week = day_dict[day]
                print(day_of_the_week)
                Speak(random.choice(reply_day).format(day_of_the_week=day_of_the_week))
                time.sleep(2)
        elif any(command in data for command in joke_commands):
            Speak(random.choice(reply_joke))
            time.sleep(2)
        elif any(command in data for command in thank_commands):
            Speak(random.choice(reply_thank))
            time.sleep(2)
        elif any(command in data for command in goodbye_commands):
            Speak(random.choice(reply_goodbye))
            time.sleep(2)
        else:  # what happens if none of the if statements are true
            Speak(random.choice(reply_unknown))  # calls Speak function and says something
            time.sleep(2)
    except sr.UnknownValueError:  # whenever you have a try statement you have an exception rule
        print("Jarvis did not understand your request")
    except sr.RequestError as e:  # if you get a request error from Google speech engine
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
"""Main program"""
with sr.Microphone() as source:  # sets microphone
    data = ""
    while "jarvis" not in data.lower() or "hey jarvis" not in data.lower():
        print("Say something!")  # prints to the screen
        audio = r.listen(source)
        data = r.recognize_google(audio)  # now uses Google speech recognition
        data = data.lower()  # makes all voice entries show as lower case
        print(data)
  # prints what was said on the screen
# while "jarvis" not in data.lower() or "hey jarvis" not in data.lower():  # starter names
#     pass
Speak("Yes sir?")  # Calls 'Speak' and acknowledges the user
while 1:  # This starts a loop so the speech recognition is always listening to you
    start_recognizer()  # calls the first function 'start_recognizer'
