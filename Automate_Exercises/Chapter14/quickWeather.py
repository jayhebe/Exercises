import json, requests, sys

str_appid = "b2d8bfdf84b708c4954e8d6190467e36"

if len(sys.argv) < 2:
    print("Usage: quickWeather.py [location]")
    sys.exit(1)
    
location = " ".join(sys.argv[1:])
url = "http://api.openweathermap.org/data/2.5/weather?q=%s&appid=b2d8bfdf84b708c4954e8d6190467e36&cnt=3" % (location)
weather_res = requests.get(url)
weather_res.raise_for_status()

weather_data = json.loads(weather_res.text)
# pprint.pprint(weather_data)

print("Current weather in %s: " % (location))
print("Temperature: " + str(weather_data["main"]["temp"]))
print(weather_data["weather"][0]["main"] + " - " + weather_data["weather"][0]["description"])