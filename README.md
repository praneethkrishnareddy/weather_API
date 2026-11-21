# Weather API Application

## 📌 Overview
The Weather API Application is a Python project that retrieves real-time weather information for any city using the OpenWeatherMap API. Users can enter a city name to view current weather conditions such as temperature, humidity, pressure, wind speed, and weather description.

---

## 🚀 Features
- Get real-time weather information
- Search weather by city name
- Displays:
  - Temperature
  - Feels Like Temperature
  - Humidity
  - Atmospheric Pressure
  - Wind Speed
  - Weather Condition
  - Country
- Handles invalid city names and API errors

---

## 🛠️ Technologies Used
- Python 3
- Requests Library
- OpenWeatherMap API

---

## 📂 Project Structure

```
Weather-API/
│── weather_api.py
│── requirements.txt
│── README.md
```

---

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Weather-API.git
```

### Navigate to the Project Folder

```bash
cd Weather-API
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the Python script:

```bash
python weather_api.py
```

Enter a city name when prompted.

Example:

```
Enter City Name: Tirupati
```

---

## 📷 Sample Output

```
===== WEATHER REPORT =====

City: Tirupati
Country: IN
Temperature: 30.4 °C
Feels Like: 33.1 °C
Humidity: 72 %
Pressure: 1008 hPa
Weather: Clouds
Description: broken clouds
Wind Speed: 4.2 m/s
```

---

## 📚 Concepts Used
- Python Functions
- API Integration
- HTTP GET Requests
- JSON Data Handling
- Exception Handling
- User Input
- Conditional Statements

---

## 🎯 Learning Outcomes
- Working with REST APIs
- Fetching real-time data
- Parsing JSON responses
- Error handling in Python
- Using third-party libraries

---

## 🔮 Future Enhancements
- Build a GUI using Streamlit or Tkinter
- Display weather icons
- 5-day weather forecast
- Automatic location detection
- Save weather history to a file

---
