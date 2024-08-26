import requests

api_key ='d28825c2da4be3a4e1a7febee8335cbb'
city_name = 'chennai'  # Replace with the desired city name

# Make the API request
base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
response = requests.get(base_url)

# Check for successful response (HTTP status code 200)
if response.status_code == 200:
    weather_data = response.json()

    # Extract information you need from the response
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    # Print or use the information as needed
    print(f"The current weather in {city_name} is {description} with a temperature of {temperature} Kelvin.")
    print(f"The humidity is {humidity}% and wind speed is {wind_speed} m/s.")
else:
    print(f'Error: {response.status_code}, {response.text}')
