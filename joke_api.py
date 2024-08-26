import requests
import pyttsx3

def get_joke():
    api_url = "https://v2.jokeapi.dev/joke/Any"

    try:
        response = requests.get(api_url)
        joke_data = response.json()

        if joke_data['type'] == 'twopart':
            joke = f"{joke_data['setup']} {joke_data['delivery']}"
        else:
            joke = joke_data['joke']

        return joke
    except Exception as e:
        return f"Error: {e}"
def Speak(text):
    rate = 100  # Sets the default rate of speech
    engine = pyttsx3.init() # Initialize the speech engine 
    voices = engine.getProperty('voices')  # sets the properties for speech
    engine.setProperty('voice', voices[1].id)  # Gender and type of voice
    engine.setProperty('rate', rate + 20)  # Adjusts the rate of speech
    engine.say(text)  # tells Python to speak variable 'text'
    engine.runAndWait()  # waits for speech to finish and then continues with the program

if __name__ == "__main__":
    joke = get_joke()
    print(joke)
    Speak(joke)