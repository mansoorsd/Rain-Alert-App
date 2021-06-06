import requests
import os
from twilio.rest import Client

API_KEY = ""
account_sid = ''
auth_token = ''

MY_LAT = 15.828374
MY_LONG = 80.194435

# MY_LAT = -1.292066
# MY_LONG = 36.821945

# Getting weather data from API
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
data_hour1 = data["hourly"][0]["weather"][0]["id"]

data_hour = list(data["hourly"][:12])
will_rain = False
for hour in data_hour:
    if hour["weather"][0]["id"] < 700:
        will_rain = True

# Sending SMS if it rains today
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain, Remember to bring an ☔️",
        from_='+14437920004',
        to='+918297736859'
    )
    print(message.status)
