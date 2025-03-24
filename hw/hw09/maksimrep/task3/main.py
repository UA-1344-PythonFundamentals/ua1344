import tkinter as tk
from tkinter import font
from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather

print(w.detailed_status)         # 'clouds'
print(w.wind())                  # {'speed': 4.6, 'deg': 330}
print(w.humidity)                # 87
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(w.rain)                    # {}
print(w.heat_index)              # None
print(w.clouds)                  # 75


def get_weather():
    
    try:
        observation = mgr.weather_at_place(entry_field.get())
        w = observation.weather
        weather_data = (
            f'detailed_status {w.detailed_status}\n'
            f'wind {w.wind()}\n'
            f'humidity {w.humidity}\n'
            f'temperature {w.temperature('celsius')}\n'
            f'rain {w.rain}\n'
            f'heat_index {w.heat_index}\n'
            f'clouds {w.clouds}\n'
        )
    except:
        weather_data = "Invalid city"

    label.config(text=weather_data)
    
    

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

