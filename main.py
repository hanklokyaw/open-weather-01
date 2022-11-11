import requests
from twilio.rest import Client

account_sid= "AC8a8368ee4ec090be2997b742587f5f45"
auth_token= "1e9493b4680ea9891a6994e94a790e4f"

will_rain = False

parameter = {
    "lat" : 12.449229,
    "lon" : 98.627060,
    "appid" : "42b88a8f7a7e3785fb3f4590b34e53c0",
    "exclude" : "current,minutely,daily"
}

data = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameter)
# print(data.raise_for_status())
# print(data.json())

# for hour in range(0,13):
# print(data.json()["hourly"][0:13]["weather"][0]['id'])
weather_slice = data.json()["hourly"][:12]
# print(weather_slice)
weather_id = [id["weather"][0]['id'] for id in weather_slice]
# print(weather_id)
for id in weather_id:
    if id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to rain",
        from_="+17695532769",
         to = "+9592032611"
    )
    print("bring an umbrella!")
        # print(client.status)
