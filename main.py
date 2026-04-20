import requests
import os
from twilio.rest import Client

# # Munich
# LAT = 48.135124
# LON = 11.581981

# Dresden
LAT = 51.050407
LON = 13.737262

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


params = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
weather_data = response.json()

# for i in range(4):
#     code = weather_data["list"][i]["weather"][0]["id"]
#     print(code)

weather_id = [weather_data["list"][i]["weather"][0]["id"] for i in range(4)]

will_it_rain = any([x < 700 for x in weather_id])
yes_no_list = [x < 700 for x in weather_id]
print(will_it_rain)
if will_it_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is goint to rain today, bring the umbrella!!!☔️",
        from_="+17755875397",
        to="+4915251724131",
    )

    print(message.status)
