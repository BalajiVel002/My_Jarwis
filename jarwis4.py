import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
import pyttsx3
import speech_recognition as sr
import time
import random
import datetime
import os
import webbrowser
import imaplib
import email
import pyautogui
from email.header import decode_header
from cryptography.fernet import Fernet
import spacy
import subprocess

"""Lists"""
greeting_commands = ["hello", "hi", "hey", "greetings"]
how_are_you = ["how are you", "how are you doing"]
weather_commands = ["weather today", "weather forecast", "tell me the weather"]
reminder_commands = ["set a reminder", "remind me to"]
news_commands = ["latest news", "news headlines", "tell me the news"]
calculator_commands = ["calculate", "what is", "solve"]
music_commands = ["play music", "play a song", "music time"]
stop_music_commands = ["stop music", "pause music", "end music", "stop the music"]
change_music_commands = ["change music", "next song", "play next", "skip song"]
location_commands = ["where am I", "current location", "tell me my location"]
joke_commands = ["tell me a joke", "say something funny", "joke time"]
thank_commands = ["thank you", "thanks", "appreciate it"]
goodbye_commands = ["goodbye", "bye", "see you later"]
time_commands = ["what is the time", "tell me the time", "current time"]
day_commands = ["what day is it", "tell me the day", "current day"]
introduction_commands = ["introduce yourself", "who are you", "tell me about yourself"]
help_commands = ["help", "what can you do", "guide me"]
calendar_commands = ["check my calendar", "calendar events", "upcoming appointments"]
email_commands = ["check my email", "unread emails", "new messages"]
social_media_commands = ["post on social media", "social updates", "latest posts"]
translate_commands = ["translate", "language translation", "translate to"]
health_commands = ["track my steps", "health status", "calories burned"]
meeting_commands = ["schedule a meeting", "upcoming meetings", "meeting reminders"]
security_commands = ["activate security", "security status", "monitor my space"]
learning_commands = ["learn something new", "educational facts", "interesting information"]
search_commands = ["search the internet", "look up", "search for", "find information about","search"]

# Add more command lists as needed

reply_greeting = ["Hello, sir!", "Hi there!", "Hey!", "Greetings!"]
reply_how_are_you = ["I'm functioning well, thank you!", "Pretty good, sir!", "I'm doing fine, thanks!"]
reply_weather = ["The weather is currently nice.", "I'm not a meteorologist, but it seems pleasant."]
reply_reminder = ["Reminder set!", "I'll remind you as requested."]
reply_news = ["Here are the latest news headlines.", "Let me update you on the news."]
reply_calculator = ["The result is {result}.", "Calculations complete: {result}."]
reply_music = ["Playing some tunes for you!", "Music is on, enjoy!"]
reply_stop_music = ["Stopping the music.", "Pausing the music.", "Ending the music."]
reply_change_music = ["Changing the music for you.", "Playing the next song."]
reply_location = ["You are currently at {location}.", "Your current location is {location}."]
reply_joke = ["Why don't scientists trust atoms? Because they make up everything!",
              "I told my wife she should embrace her mistakes. She gave me a hug.",
              "What do you call fake spaghetti? An impasta."]
reply_thank = ["You're welcome, sir!", "Anytime!", "It was my pleasure."]
reply_goodbye = ["Goodbye, sir!", "Until next time!", "See you later!"]
reply_time = ["The time is {str_time}", "It's currently {str_time}", "The current time is {str_time}"]
reply_day = ["Today is {day_of_the_week}", "It's {day_of_the_week} today", "The day is {day_of_the_week}"]
reply_introduction = ["I am Jarvis, your virtual assistant.", "Hello, I'm Jarvis, at your service."]
reply_help = ["I can assist you with weather updates, reminders, news, calculations, and more.",
              "Feel free to ask me about the weather, set reminders, get news updates, and more."]
reply_calendar = ["Checking your calendar for upcoming events.", "Here are your scheduled appointments."]
reply_email = ["Checking your email for new messages.", "You have {unread_count} unread emails."]
reply_social_media = ["Checking the latest posts on your social media accounts.", "Here are your recent social media updates."]
reply_translate = ["Translating the text for you.", "The translated text is: {translated_text}."]
reply_health = ["Tracking your health status.", "You've burned {calories_burned} calories so far."]
reply_meeting = ["Scheduling a meeting for you.", "Meeting scheduled successfully."]
reply_security = ["Activating security measures.", "Monitoring your space for security."]
reply_learning = ["Providing you with interesting information.", "Here's something new for you to learn."]
reply_search = ["Sure, searching the internet for you.", "Let me find that information for you."]


class JarvisGUI:
    def __init__(self, master):
        self.master = master
        master.title("Jarvis GUI")

        # Text widget for displaying Jarvis responses
        self.output_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=10)
        self.output_text.pack(pady=10)

        # Entry widget for user input
        self.input_entry = tk.Entry(master, width=50)
        self.input_entry.pack(pady=10)

        # Button to trigger Jarvis's recognition
        self.recognize_button = tk.Button(master, text="Recognize", command=self.start_recognizer_thread)
        self.recognize_button.pack(pady=10)

        # Create Jarvis instance
        self.jarvis_instance = Jarvis(self)

    def start_recognizer_thread(self):
        # Start the recognition in a separate thread to avoid freezing the GUI
        Thread(target=self.jarvis_instance.start_recognizer).start()


class Jarvis:
    def __init__(self, gui):
        # Initialize Jarvis-related variables and settings
        self.gui = gui
        self.r = sr.Recognizer()

        # ... (your existing initialization code)

    def Speak(self, text):
        rate = 100  # Sets the default rate of speech
        engine = pyttsx3.init() # Initialize the speech engine 
        voices = engine.getProperty('voices')  # sets the properties for speech
        engine.setProperty('voice', voices[0].id)  # Gender and type of voice
        engine.setProperty('rate', rate + 50)  # Adjusts the rate of speech
        engine.say(text)  # tells Python to speak variable 'text'
        engine.runAndWait()  # waits for speech to finish and then continues with the program
        pass
    def is_wifi_enabled():
        try:
            result = subprocess.check_output(['netsh', 'interface', 'show', 'interface'], stderr=subprocess.STDOUT, text=True)
            return 'Wi-Fi' in result and 'Connected' in result
        except subprocess.CalledProcessError as e:
            print(f"Error checking WiFi status: {e.output}")
            return False

    def is_hotspot_enabled():
        try:
            result = subprocess.check_output(['powershell', 'Get-Service -Name icssvc | Select-Object Status'], stderr=subprocess.STDOUT, text=True)
            return 'Running' in result
        except subprocess.CalledProcessError as e:
            print(f"Error checking hotspot status: {e.output}")
            return False
        print(result)
    def toggle_hotspot_keyboard_shortcut():
        pyautogui.hotkey('win','a')
        time.sleep(1)
        pyautogui.hotkey('right')
        time.sleep(1)
        pyautogui.hotkey('right')
        time.sleep(1)
        pyautogui.hotkey('right')
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(1)
        pyautogui.hotkey('win','a')
        time.sleep(1) 

    def toggle_wifi_keyboard_shortcut():
        pyautogui.hotkey('win','a')
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(1)
        pyautogui.hotkey('win','a')
        time.sleep(1)

    def toggle_bluetooth_keyboard_shortcut():
        pyautogui.hotkey('win','a')
        time.sleep(1)
        pyautogui.hotkey('right')
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(1)
        pyautogui.hotkey('win','a')
        time.sleep(1)
                                                #To shutdown the pc 
    def shutdown_pc():
        pyautogui.hotkey('alt','f4')
        time.sleep(1)
        pyautogui.hotkey('alt','f4')
        time.sleep(1)
        pyautogui.hotkey('alt','f4')
        time.sleep(1)
        pyautogui.hotkey('enter')
        time.sleep(1)

    def decrease_volume():
        pyautogui.hotkey('f2')
        time.sleep(1)
        pyautogui.hotkey('f2')
        time.sleep(1)
        pyautogui.hotkey('f2')
        time.sleep(1)
        pyautogui.hotkey('f2')
        time.sleep(1)
        pyautogui.hotkey('f2')
        time.sleep(1)

    def increase_volume():
        pyautogui.hotkey('f3')
        time.sleep(1)
        pyautogui.hotkey('f3')
        time.sleep(1)
        pyautogui.hotkey('f3')
        time.sleep(1)
        pyautogui.hotkey('f3')
        time.sleep(1)
        pyautogui.hotkey('f3')
        time.sleep(1)

    def decrease_brightness():
        pyautogui.hotkey('f5')
        time.sleep(1)
        pyautogui.hotkey('f5')
        time.sleep(1)
        pyautogui.hotkey('f5')
        time.sleep(1)
        pyautogui.hotkey('f5')
        time.sleep(1)
        pyautogui.hotkey('f5')
        time.sleep(1)

    def increase_brightness():
        pyautogui.hotkey('f6')
        time.sleep(1)
        pyautogui.hotkey('f6')
        time.sleep(1)
        pyautogui.hotkey('f6')
        time.sleep(1)
        pyautogui.hotkey('f6')
        time.sleep(1)
        pyautogui.hotkey('f6')
        time.sleep(1)

    def toggle_wifi(status):

        if status.lower() == "on":
            wifi_status=is_wifi_enabled()
            if wifi_status == 1:
                Speak("wifi is aldready turned ON")
            else:
                toggle_wifi_keyboard_shortcut()
                Speak("wifi turned on")
        elif status.lower() == "off":
            wifi_status=is_wifi_enabled()
            if wifi_status == 0:
                Speak("wifi is aldready turned off")
            else:
                toggle_wifi_keyboard_shortcut()
                Speak("wifi turned on")
        else:
            Speak("Invalid status. Please use 'on' or 'off.'")

    def toggle_hotspot(status):

        if status.lower() == "on":
                toggle_hotspot_keyboard_shortcut()
                Speak("hotspot turned on")
        elif status.lower() == "off":
                toggle_hotspot_keyboard_shortcut()
                Speak("hotspot turned OFF")
        else:
            Speak("Invalid status. Please use 'on' or 'off.'")

    def toggle_bluetooth(status):

        if status.lower() == "on":
                toggle_bluetooth_keyboard_shortcut()
                Speak("bluetooth turned on")
        elif status.lower() == "off":
                toggle_bluetooth_keyboard_shortcut()
                Speak("bluetooth turned OFF")
        else:
            Speak("Invalid status. Please use 'on' or 'off.'")

    def tokenize_text(text):
        doc = nlp(text)
        tokens = [token.text for token in doc]
        return tokens

    def pos_tagging(text):
        doc = nlp(text)
        pos_tags = [(token.text, token.pos_) for token in doc]
        return pos_tags

    def ner(text):
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def search_internet(query):
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)

    def encrypt_password(password):
        encrypted_password = cipher_suite.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(encrypted_password):
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
        return decrypted_password

    def check_email():
        try:
        # Update these with your email server details
            email_user = "balajivel002@gmail.com"
            encrypted_email_pass = b'gAAAAABlW2YvjFEaToQB8Ja8G97DzQ5OL7B3MwgSPIXoCFM3FovAaibS1_wL2_pzj9OloU1iIEeMHzr2kPa0vpv1vNJg3yFpDg=='
            email_pass = decrypt_password(encrypted_email_pass)
            mail = imaplib.IMAP4_SSL("www.gmail.com")
            mail.login(email_user, email_pass)

        # Select the mailbox you want to check (e.g., 'inbox')
            mail.select("inbox")

        # Search for all unseen emails
            status, messages = mail.search(None, "(UNSEEN)")
            if status == "OK":
              email_list = messages[0].split()
              num_unseen_emails = len(email_list)
              Speak(f"You have {num_unseen_emails} unread emails.")

            # Fetch details of each unseen email
            for num in email_list:
                    _, msg_data = mail.fetch(num, "(RFC822)")
                    for response_part in msg_data:
                      if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject, encoding = decode_header(msg["Subject"])[0]
                        sender, encoding = decode_header(msg.get("From"))[0]
                        sender = sender.decode("utf-8") if isinstance(sender, bytes) else sender
                        subject = subject.decode("utf-8") if isinstance(subject, bytes) else subject
                        Speak(f"Email from {sender}. Subject: {subject}")

        # Logout from the email server
            mail.logout()
        except Exception as e:
            print(f"Error: {e}")
            Speak("I encountered an error while checking email. Please check your credentials.")
    def change_music():
        # Stop the current music playback
        stop_music()
        # Play a new music file
        play_music()

    def stop_music():
        # Terminate the music playback process
        os.system("taskkill /f /im Microsoft.Media.Player.exe")

    def play_music():
        music_directory = "C:/Users/DELL/Music" # Provide the path to your music directory
        music_files = os.listdir(music_directory)# List all files in the directory
        
        if music_files:
            # Select a random music file
            selected_music = os.path.join(music_directory, random.choice(music_files))
            os.startfile(selected_music)
        else:
            Speak("Sorry, I couldn't find any music in your directory.")

    def callback(recognizer, audio):
        try:
            recognize_main(audio)  # Runs the function recognize_main
        except sr.UnknownValueError:  # if there is nothing understood
            print("Oops! Didn't catch that")  # prints to the screen error message

    def start_recognizer():
        print("Jarvis ready to listen...")
        r.listen_in_background(source, callback)  # Sets off the recognition sequence
        time.sleep(100000)  # keeps loop running     

    def start_recognizer(self):
        try:
            print("Jarvis ready to listen...")
            with sr.Microphone() as source:
                data = ""
                while "jarvis" not in data.lower() and "hey jarvis" not in data.lower():
                    print("Say something!")
                    audio = self.r.listen(source)
                    data = self.r.recognize_google(audio).lower()
                    print(data)
                    self.gui.output_text.insert(tk.END, "User: " + data + "\n")

                self.Speak("Welcome back, sir!")

                while True:
                    self.recognize_main()
        except sr.UnknownValueError:
            print("Jarvis didn't catch that.")

    def recognize_main(self):
        # Your existing recognize_main function with modifications for GUI
      try:
        data = self.r.recognize_google(self.r.listen(source))
        data = data.lower()
        print("You said: " + data)
               # Greetings
        if data in greeting_commands:
            Speak(random.choice(reply_greeting))
            time.sleep(2)
        # Weather
        elif any(command in data for command in weather_commands):
            Speak(random.choice(reply_weather))
            time.sleep(2)
        # how are you   
        elif data in how_are_you:
            Speak(random.choice(reply_how_are_you))
            time.sleep(2)
        # Reminders
        elif any(command in data for command in reminder_commands):
            Speak(random.choice(reply_reminder))
            time.sleep(2)
        # News
        elif any(command in data for command in news_commands):
            Speak(random.choice(reply_news))
            time.sleep(2)
        # Calculator
        elif any(command in data for command in calculator_commands):
            result = "42"  # Replace with actual calculation result
            Speak(random.choice(reply_calculator).format(result=result))
            time.sleep(2)
        # Music
        elif any(command in data for command in music_commands):
            Speak(random.choice(reply_music))
            play_music()
            time.sleep(2)
        elif any(command in data for command in stop_music_commands):
            Speak(random.choice(reply_stop_music))
            stop_music()
            time.sleep(2)
        elif any(command in data for command in change_music_commands):
            Speak(random.choice(reply_change_music))
            change_music()
            time.sleep(2)
        # Location
        elif any(command in data for command in location_commands):
            location = "somewhere"  # Replace with actual location
            Speak(random.choice(reply_location).format(location=location))
            time.sleep(2)
        # Jokes
        elif any(command in data for command in joke_commands):
            Speak(random.choice(reply_joke))
            time.sleep(2)
        # Thank you
        elif any(command in data for command in thank_commands):
            Speak(random.choice(reply_thank))
            time.sleep(2)
        # Goodbye
        elif any(command in data for command in goodbye_commands):
            Speak(random.choice(reply_goodbye))
            time.sleep(2)
        # Time
        elif any(command in data for command in time_commands):
            str_time = datetime.datetime.now().strftime("%H:%M")
            Speak(random.choice(reply_time).format(str_time=str_time))
            time.sleep(2)
        # Day
        elif any(command in data for command in day_commands):
            day = datetime.datetime.today().weekday() + 1
            day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                        4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                        7: 'Sunday'}
            if day in day_dict.keys():
                day_of_the_week = day_dict[day]
                Speak(random.choice(reply_day).format(day_of_the_week=day_of_the_week))
                time.sleep(2)
        # Introduction
        elif any(command in data for command in introduction_commands):
            Speak(random.choice(reply_introduction))
            time.sleep(2)
        # Help
        elif any(command in data for command in help_commands):
            Speak(random.choice(reply_help))
            time.sleep(2)
        # Calendar
        elif any(command in data for command in calendar_commands):
            Speak(random.choice(reply_calendar))
            time.sleep(2)
        # Email
        #elif any(command in data for command in email_commands):
        #    unread_count = "3"  # Replace with actual unread email count
        #   Speak(random.choice(reply_email).format(unread_count=unread_count))
        #   time.sleep(2)
        elif any(command in data for command in email_commands):
            Speak(random.choice(reply_email))
            check_email()
            time.sleep(2)
        # Social Media
        elif any(command in data for command in social_media_commands):
            Speak(random.choice(reply_social_media))
            time.sleep(2)
        # Translate
        elif any(command in data for command in translate_commands):
            translated_text = "Hello"  # Replace with actual translated text
            Speak(random.choice(reply_translate).format(translated_text=translated_text))
            time.sleep(2)
        # Health
        elif any(command in data for command in health_commands):
            calories_burned = "200"  # Replace with actual calories burned
            Speak(random.choice(reply_health).format(calories_burned=calories_burned))
            time.sleep(2)
        # Meeting
        elif any(command in data for command in meeting_commands):
            Speak(random.choice(reply_meeting))
            time.sleep(2)
        # Security
        elif any(command in data for command in security_commands):
            Speak(random.choice(reply_security))
            time.sleep(2)
         # Internet Search
        elif any(command in data for command in search_commands):
            Speak(random.choice(reply_search))
            query = data.replace("search the internet for", "").strip()  # Extract the search query
            search_internet(query)
            time.sleep(2)
        # Learning
        elif any(command in data for command in learning_commands):
            Speak(random.choice(reply_learning))
            time.sleep(2)
        # wifi
        elif "turn on wi-fi" in data:
            status = "on"
            toggle_wifi(status)
            time.sleep(2)
        elif "turn off wi-fi" in data:
            status ="off"
            toggle_wifi(status)
            time.sleep(2)
        #hotspot
        elif "turn on hotspot" in data:
            status = "on"
            toggle_hotspot(status)
            time.sleep(2)
        elif "turn off hotspot" in data:
            status = "off"
            toggle_hotspot(status)
            time.sleep(2)
        #bluetooth
        elif "turn on bluetooth" in data:
            status = "on"
            toggle_bluetooth(status)
            time.sleep(2)
        elif "turn off bluetooth" in data:
            status = "off"
            toggle_bluetooth(status)
            time.sleep(2)
        #shutdown
        elif "shutdown" in data:
            shutdown_pc()
            Speak("shutting down")
            time.sleep(2)
        
        #volume
        elif "decrease volume" in data:
            decrease_volume()
            Speak("decreasing volume")
            time.sleep(2)
        
        elif "increase volume" in data:
            increase_volume()
            Speak("increasing volume")
            time.sleep(2)
        
        #brightness
        elif "decrease brightness" in data:
            decrease_brightness()
            Speak("decreasing brightness")
            time.sleep(2)
        
        elif "increase brightness" in data:
            increase_brightness()
            Speak("increasing brightness")
            time.sleep(2)

        #tokenize
        elif "tokenize" in data:
            text_to_tokenize = "Natural Language Processing is fascinating!"
            tokens = tokenize_text(text_to_tokenize)
            Speak(f"Tokens: {tokens}")
        # POS Tagging
        elif "pos tagging" in data:
            text_to_tag = "The cat is sitting on the mat."
            pos_tags_result = pos_tagging(text_to_tag)
            Speak(f"POS Tags: {pos_tags_result}")
        # Named Entity Recognition (NER)
        elif "ner" in data:
            text_for_ner = "Apple Inc. was founded by Steve Jobs."
            ner_result = ner(text_for_ner)
            Speak(f"NER Result: {ner_result}")
        else:  # what happens if none of the if statements are true
            Speak("I'm sorry sir, I did not understand your request")  # calls Speak function and says something               

      except sr.UnknownValueError:
            print("Jarvis did not understand your request")
      except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisGUI(root)
    root.mainloop()