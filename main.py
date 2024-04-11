import requests
from twilio.rest import Client

api_key = " paste your own api key"
OWN_endpoint = "https://api.weatherapi.com/v1/forecast.json?key={api_key}&q=Aligarh&days=1&aqi=no&alerts=no"

account_sid = "paste your own account sid from twilio"
auth_token = "paste your own auth token from twilio"

response = requests.get(OWN_endpoint)
weather_data = response.json()

weather_slice = weather_data["forecast"]["forecastday"][0]["hour"][:19]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["condition"]["code"]
    if 1240 <= int(condition_code) <= 1252 or 1180 <= int(condition_code) <= 1201:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = ''' ALERT!!!
                 It will rain today so ,  don't forget to carry umbrella ☂️''',
        from_= "mobile number provide by twilio",
        to = "+91 your mobile number",
    )
    print(message.status)

else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = ''' Have a good day''',
        from_= "mobile number provide by twilio",
        to = "+91 your mobile number",
    )
    print(message.status)
