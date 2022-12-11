import requests
from datetime import datetime

MY_LAT = 37.485970
MY_LONG = 126.948247

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1])
print(sunset.split("T")[1])

time_now = datetime.now()
print(time_now)
