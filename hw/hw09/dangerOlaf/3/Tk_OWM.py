from pyowm import OWM
import tkinter as tk
from tkinter import font

def get_weather():
    city = entry_field.get().strip() 
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        wind = w.wind()
        temp = w.temperature('celsius')

        multiline_text = (
            f"City: {city.capitalize()}\n"
            f"Weather: {w.detailed_status}\n"
            f"Wind Speed: {wind['speed']} km/h\n"
            f"Humidity: {w.humidity}%\n"
            f"Max temperature: {temp['temp_max']}°C\n"
            f"Min temperature: {temp['temp_min']}°C\n"
            f"Feels like: {temp['feels_like']}°C\n"
            f"Rain: {w.rain if w.rain else 0} mm\n"
            f"Heat Index: {w.heat_index if w.heat_index else 0}°C\n"
            f"Clouds: {w.clouds}%\n"
        )

        text.set(multiline_text)
    except Exception as e:
        text.set(f"Error: {e}")

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 550
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.075, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.75, anchor='n')

text = tk.StringVar()
message = tk.Message(lower_frame, textvariable=text, font=('Courier', 12))
message.place(relx=0, rely=0, relwidth=1, relheight=1)
text.set("Please enter a city name and Press on Get Weather")

root.mainloop()