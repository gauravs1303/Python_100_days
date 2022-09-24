import requests
import datetime as dt
import pywhatkit
import

api_key = "eCYIsXVtGJTcgCqvVXx8WqHR4n2Kg1ab"
citi_endp = "https://dataservice.accuweather.com/locations/v1/cities/search"

city_params = {
    "q": 'Jodhpur',
    "apikey": api_key
}
cities = requests.get(citi_endp, params=city_params)
cities.raise_for_status()

city_code = cities.json()[0]['Key']

weather_endp = f"http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{city_code}"

weather_params = {
    "apikey": api_key,
    "details": True,
    "metric": True,
}

weather_data = requests.get(weather_endp, params=weather_params)
weather_data.raise_for_status()
weather = weather_data.json()

will_rain = False

hours_list = []
temp_list = []
weather_list = []
for hr in weather:
    temp_list.append(hr["Temperature"]["Value"])
    weather_list.append(hr['IconPhrase'])
    if hr['RainProbability'] >= 40:
        print(hr["DateTime"])
        hour1 = dt.datetime.fromisoformat(hr["DateTime"])
        hr2 = hour1.strptime("%H:%M")
        hours_list.append(str(hr2.strptime("%I:%M %p")))
        will_rain = True

timings = ', '.join(hours_list)
print(weather_list)

message = ""

if will_rain:
    message += f"Bring an Umbrella. Rain timings are : {timings}\n"

message += f"Maximum Temperature : {max(temp_list)}\nMinimum Temperature : {min(temp_list)}" \
           f"\nMostly Weather is gonna be {max(weather_list, key=weather_list.count)}"
pywhatkit.sendwhatmsg_instantly("+916377285859", f"{message}", tab_close=True)
