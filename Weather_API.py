import requests

API_KEY = "YOUR_API_KEY"

city = input("Enter City Name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print("\n===== WEATHER REPORT =====")
        print("City:", data["name"])
        print("Country:", data["sys"]["country"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Pressure:", data["main"]["pressure"], "hPa")
        print("Weather:", data["weather"][0]["main"])
        print("Description:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")

    else:
        print("❌ City not found or Invalid API Key!")

except requests.exceptions.RequestException:
    print("❌ Network Error! Please check your internet connection.")
