from pyowm import OWM
import tkinter as tk
from tkinter import font, StringVar

HEIGHT = 600
WIDTH = 500

root = tk.Tk()


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

label_text = StringVar()

def get_weather(place = 'London,GB'):
    observation = mgr.weather_at_place(place)
    w = observation.weather

    weather_info = (
        f"{place}\n"
        f"Status: {w.detailed_status}\n"
        f"Wind speed: {w.wind()['speed']} m/sec\n"
        f"Wind deg: {w.wind()['deg']}\n"
        f"Humidity: {w.humidity}%\n"
        f"Temperature: {w.temperature('celsius')['temp']}°C\n"
        f"Temp. max: {w.temperature('celsius')['temp_max']}°C\n"
        f"Temp. min: {w.temperature('celsius')['temp_min']}°C\n"
        f"Temp. feels like: {w.temperature('celsius')['feels_like']}°C\n"
        f"Rain: {w.rain}\n"
        f"Heat Index: {w.heat_index}\n"
        f"Clouds: {w.clouds}"
    )

    label_text.set(weather_info)


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather() if len(entry_field.get()) == 0 else get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14), textvariable = label_text, anchor='nw', justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()

