import requests
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and configure labels and entry fields
city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Create a button to fetch weather data
fetch_button = tk.Button(root, text="Fetch Weather")
fetch_button.pack()

# Create a label to display weather information
weather_label = tk.Label(root, text="")
weather_label.pack()

# Define the function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    # Add your API key here
    api_key = "25bf337eabe54a469fe111648241506"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()
    temperature= data['current']['temp_c']
    city_name= data['location']['name']
    weather_label.config(text=f"Temperature: {temperature}°C\nCity: {city_name}")

fetch_button.config(command=fetch_weather)

# Start the GUI main loop
root.mainloop()