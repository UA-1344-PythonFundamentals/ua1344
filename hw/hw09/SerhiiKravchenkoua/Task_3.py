import tkinter as tk
from tkinter import font
from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
    city = entry_field.get()
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        status = w.detailed_status
        temperature = w.temperature('celsius')
        wind = w.wind()
        humidity = w.humidity
        rain = w.rain
        heat_index = w.heat_index
        clouds = w.clouds

        weather_info = (f"Weather in {city}:\n"
                        f"Status: {status}\n"
                        f"Temperature: {temperature['temp']}°C "
                        f"(Min: {temperature['temp_min']}°C, Max: {temperature['temp_max']}°C)\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind: {wind['speed']} m/s, Direction: {wind.get('deg', 'N/A')}°\n"
                        f"Rain: {rain if rain else 'No rain'}\n"
                        f"Heat Index: {heat_index if heat_index else 'N/A'}\n"
                        f"Clouds: {clouds}%")
    except Exception as e:
        weather_info = "Invalid city name. Try again."

    label.config(text=weather_info)

HEIGHT = 400
WIDTH = 550

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


frame = tk.Frame(root, bg="green", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="black", fg="red",
                   font=('Courier', 12),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

