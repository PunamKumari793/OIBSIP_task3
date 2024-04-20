import requests

a = 'f88052ab074f2f74587f2ebf3f418836'

b = input("Enter city:")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={b}&units=imperial&APPID={a}")

if weather_data.json()['cod'] == '404':
    print("NO CITY FOUND")
else:    
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    humidity = weather_data.json()['main']['humidity']

print(f"The weather in {b} is: {weather}")
print(f"The temperature in {b} is: {temp}°F")
print(f"The humidity in {b} is: {humidity} g/m³")
