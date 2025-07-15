import requests
from datetime import datetime
import pytz  # Make sure this is available in Replit

# ✅ Replace with your actual API key
API_KEY = "0b413f6251edb22b9fe8ea426cd5fba7"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# 📥 Input
city = input("Enter your city name (in English): ")

# API request
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}
response = requests.get(BASE_URL, params=params)
data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    condition = data["weather"][0]["description"].capitalize()
    icon_code = data["weather"][0]["icon"]
    country = data["sys"]["country"]

    # ✅ Convert UTC to IST
    utc_time = datetime.utcfromtimestamp(data["dt"])
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = utc_time.replace(tzinfo=pytz.utc).astimezone(ist)
    time_str = ist_time.strftime("%Y-%m-%d %I:%M:%S %p")

    # 🌐 Weather icon URL
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

    # ✅ Display
    print("\n📡 Weather Report")
    print(f"📍 Location: {city}, {country}")
    print(f"🕒 Date & Time (IST): {time_str}")
    print(f"🌡️ Temperature: {temp}°C (Feels like: {feels_like}°C)")
    print(f"☁️ Condition: {condition}")
    print(f"💧 Humidity: {humidity}%")
    print(f"💨 Wind Speed: {wind_speed} m/s")
    print(f"🌤️ Weather Icon: {icon_url}")
else:
    print("❌ City not found. Please check the name and try again.")
