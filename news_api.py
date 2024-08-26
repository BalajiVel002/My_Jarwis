import requests
import sys
import pyttsx3

def get_news(api_key, country='in'):
    base_url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': country,
        'apiKey': api_key
    }
    sys.stdout.reconfigure(encoding='utf-8')


    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            articles = data.get('articles', [])

            if articles:
                for idx, article in enumerate(articles, start=1):
                    title = article.get('title', 'No Title')
                    print(f"{idx}.{title}")
                    Speak(f"{idx}. {title}")
            else:
                Speak("No articles found.")
        else:
            Speak(f"Error: {data.get('message', 'Unknown error')}")
    except Exception as e:
        Speak(f"An error occurred: {str(e)}")

# Replace 'YOUR_API_KEY' with your actual News API key
def Speak(text):
    rate = 100  # Sets the default rate of speech
    engine = pyttsx3.init() # Initialize the speech engine 
    voices = engine.getProperty('voices')  # sets the properties for speech
    engine.setProperty('voice', voices[0].id)  # Gender and type of voice
    engine.setProperty('rate', rate + 10)  # Adjusts the rate of speech
    engine.say(text)  # tells Python to speak variable 'text'
    engine.runAndWait()  # waits for speech to finish and then continues with the program

api_key = '2eb5fbc3cb5b493cbb125f71297c6237'
get_news(api_key)