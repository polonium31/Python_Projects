API_KEY = "814e30871f2ec9b3f5b4d1e21d5cc05f"
account_sid = 'AC58fe293dd6690a2ac6da7d450e323d3c'
auth_token = 'd2feaee9be9d7b3110235ba6c25a4f44'



import requests as rt
import os
from twilio.rest import Client
response = rt.get(
    url=f"https://api.openweathermap.org/data/2.5/onecall?lat=23.058475&lon=72.661815&units=metric&exclude=current,minutely,daily&appid={API_KEY}")
response.raise_for_status()
weather_status = response.json()

weather_slice = weather_status['hourly'][:12]
is_summer = False
is_winter = False
is_monsoon = False
for hour_data in weather_slice:
    weather = hour_data['weather'][0]['id']
    temperature = hour_data["temp"]
    if weather >= 800 or temperature >= 35:
        is_summer = True
    elif weather <= 700:
        is_monsoon = True
    elif temperature <= 20:
        is_winter =  True

if is_summer:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Take a bottle of water with you and be hydrated",
        from_='+16302803315',
        to='+918200993004'
    )
    print(message.sid)
elif is_monsoon:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Take umbrella with you may be its rain today",
        from_='+16302803315',
        to='+918200993004'
    )
    print(message.sid)
elif is_winter:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Wear a Jacket or sweater",
        from_='+16302803315',
        to='+918200993004'
    )
    print(message.sid)
