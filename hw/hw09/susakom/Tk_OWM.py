# HW09 Susak Oleksandr task 03
import tkinter as tk

from tkinter import font

from pyowm import OWM

def get_weather():

    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()


    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place('London,GB')
    w = observation.weather

    label.config(text=(f"Location: 'London,GB'\n"
                         f"Detailed status: {w.detailed_status}\n"
                         f"Wind: {w.wind()}\n" 
                         f"Humidity: {w.humidity}\n" 
                         f"Temperature: {w.temperature('celsius')['temp']} C\n"
                            f"(Min: {w.temperature('celsius')['temp_min']} C,  "
                            f"Max: {w.temperature('celsius')['temp_max']} C)\n"
                         f"Rain: {w.rain}\n"
                         f"Heat index: {w.heat_index}\n"
                         f"Clouds: {w.clouds}"))


HEIGHT = 400
WIDTH = 600


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)
entry_field.insert(0, 'London,GB')


button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)
#result_wether = get_weather()


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.7, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

