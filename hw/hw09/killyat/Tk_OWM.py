import tkinter as tk
from tkinter import font
import requests

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = entry_field.get()
    if not city:
        label.config(text="Please enter a city name!")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "en"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            label.config(text=f"Error: {data['message']}")
            return

        temp = data["main"]["temp"]
        status = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_info = (f"Weather in {city}:\n"
                       f"Status: {status.capitalize()}\n"
                       f"Temperature: {temp}°C\n"
                       f"Humidity: {humidity}%\n"
                       f"Wind Speed: {wind_speed} m/s")
        label.config(text=weather_info)

    except Exception:
        label.config(text="Connection error or invalid city name.")

HEIGHT = 400
WIDTH = 550

root = tk.Tk()
root.title("Weather App")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#e3f2fd")
canvas.pack()

frame = tk.Frame(root, bg="#90caf9", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Arial', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", bg="#42a5f5", fg="white",
                   font=('Arial', 12), command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#bbdefb", bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Arial', 14), justify="left")
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()