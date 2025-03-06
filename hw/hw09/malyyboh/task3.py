from pyowm import OWM, commons
import tkinter as tk
from tkinter import font


API_KEY = "ef2206ff5da67de63306d0b143e20872"
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather() -> str:
    city = entry_field.get()
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        status = w.detailed_status  # 'clouds'
        wind = w.wind()  # {'speed': 4.6, 'deg': 330}
        humidity = w.humidity  # 87
        temp = w.temperature(
            "celsius"
        )  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        rain = w.rain  # {}
        heat_index = w.heat_index  # None
        clouds = w.clouds  # 75

        city_weather = (
            f"{city} weather:\n"
            f"Status: {status}\n"
            f"Wind - speed: {wind['speed']}, deg: {wind['deg']}\n"
            f"Humidity: {humidity}\n"
            f"Temperature - {temp['temp']} Max: {temp['temp_max']} Min: {temp['temp_min']}\n"
            f"Rain: {rain.get('1h') if rain else 'No rain'}\n"
            f"Heat index: {heat_index if heat_index else '-'}\n"
            f"Clouds: {clouds if clouds else 0}"
        )
        text_var.set(city_weather)
    except commons.exceptions.NotFoundError:
        text_var.set(f"City - '{city}' not found! Try again.")


HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry_field = tk.Entry(frame, font=("Courier", 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


button = tk.Button(
    frame,
    text="Get Weather",
    bg="gray",
    fg="black",
    font=("Courier", 8),
    command=get_weather,
)


button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg="gold", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")


text_var = tk.StringVar()

label = tk.Label(lower_frame, font=("Courier", 14), textvariable=text_var)
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()
