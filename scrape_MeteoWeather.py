import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=12.9716&longitude=77.5946&current_weather=true"

response = requests.get(url)
data = response.json()

current = data["current_weather"]

print("Temperature:", current["temperature"], "°C")
print("Wind Speed:", current["windspeed"], "km/h")
print("Weather Code:", current["weathercode"])
print("Time:", current["time"])
