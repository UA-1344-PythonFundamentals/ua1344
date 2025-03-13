import tkinter as tk
from tkinter import font
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
    city = entry_field.get()
    if not city:
        label.config(text="Please enter a city name")
        return

    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        status = w.detailed_status
        temp = w.temperature('celsius')
        heat_index = w.heat_index
        wind_speed = w.wind()['speed']
        rain = w.rain.get('1h', None)
        weather_info = (f"Weather in {city}:\n"
                        f"Status: {status}\n"
                        f"Temperature: {temp['temp']}°C\n"
                        f"Max Temp: {temp['temp_max']}°C\n"
                        f"Min Temp: {temp['temp_min']}°C\n"
                        f"Heat Index: {heat_index if heat_index else 'No data'}\n"
                        f"Humidity: {w.humidity}%\n"
                        f"Wind: {wind_speed} m/s\n"
                        f"Clouds: {w.clouds}%\n"
                        f"Rain: {rain if rain else ''} {'mm' if rain else 'No rain'}")
        label.config(text=weather_info)
    except Exception as e:
        label.config(text="Error fetching weather data\nCheck city name")

HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="gray",
                   font=('Courier', 8),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12), anchor='nw', justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
