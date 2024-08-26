import requests
import pyttsx3

def Speak(text):
    rate = 100 #Sets the default rate of speech
    engine = pyttsx3.init() #Initialises the speech engine
    voices = engine.getProperty('voices') #sets the properties for speech
    engine.setProperty('voice', voices[0].id) #Gender and type of voice
    engine.setProperty('rate', rate+50) #Adjusts the rate of speech
    engine.say(text) #tells Python to speak variable 'text'
    engine.runAndWait() #waits for speech to finish and then continues with program

api_key = 'd8a96f5da7d70b3dc4d7bc0bfc84256e'
city_name = 'chennai'  # Replace with the desired city name

# Make the API request with additional parameters for detailed information
base_url = f'http://api.weatherstack.com/current?access_key={api_key}&query={city_name}&units=m&extra=hourly'
response = requests.get(base_url)

# Check for successful response (HTTP status code 200)
if response.status_code == 200:
    weather_data = response.json()

    # Extract detailed information
    temperature = weather_data['current']['temperature']
    description = weather_data['current']['weather_descriptions'][0]
    humidity = weather_data['current']['humidity']
    wind_speed = weather_data['current']['wind_speed']
    visibility = weather_data['current']['visibility']

    # Create a sentence-like output
    output_sentence = f"The current weather in {city_name} is {description.lower()} with a temperature of {temperature} degrees Celsius. "
    output_sentence += f"The humidity is {humidity}%, wind speed is {wind_speed} meters per second, and visibility is {visibility} meters."

    Speak(output_sentence)
else:
    Speak(f'Error: {response.status_code}, {response.text}')
