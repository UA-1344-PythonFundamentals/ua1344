from pyowm import OWM
import tkinter as tk
from tkinter import messagebox



API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather():
    city = entry_field.get().strip()
    print(city)
    if not city or len(city) < 3:
        label.config(text="")
        messagebox.showwarning("City?", "Enter city name")
        return
    else:
        try:
            observation = mgr.weather_at_place(city)
            w = observation.weather
            label.config(text = f"{city}\n{w.detailed_status}\nHumidity:{w.humidity}\nTemp: {w.temperature('celsius')["temp"]}°C\nWind: {round((w.wind().get("speed", 0)*3.6), 2)}, km/h\nClouds: {w.clouds}",wraplength=330)
        except Exception as e:
            label.config(text="")
            messagebox.showerror("Error", "Can't find data")

HEIGHT = 350
WIDTH = 450


root = tk.Tk()


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
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()