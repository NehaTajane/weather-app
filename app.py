import requests
import streamlit as st 
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

st.set_page_config(
    page_title="Weather App",
    page_icon="🌦️"
)

st.title("Weather App🌦️")
st.write("Enter the City name and click the button to fetch the weather data")

city = st.text_input("Enter the City Name")


API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

if st.button("Fetch Weather Data"):
    response = requests.get(API_URL)
    if response.status_code == 200:
        st.success("Weather data Fetched Successfully!")
        
        data = response.json()
        name = data["name"]
        country = data["sys"]["country"]
        
        st.subheader(f"{name},{country}")
        
        temperature = data["main"]["temp"]
        speed = data["wind"]["speed"]
        weather = data["weather"][0]["main"]
        humidity = data["main"]["humidity"]
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Temperature", f"🌡️{temperature}°C ")
        col2.metric("Wind Speed", f"💨{speed} m/s")
        col3.metric("Weather",  f"⛈️{weather}")
        col4.metric("Humidity", f"💧{humidity}%")
    else:
        st.error("Please enter a valid city name")
