import tkinter as tk
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather():
    city = entry_field.get().strip()  
    if not city:
        label.config(text="Please enter a city name!")
        return

    try:
        observation = mgr.weather_at_place(city)  
        w = observation.weather
        
        status = w.detailed_status
        wind_speed = w.wind().get('speed', 'N/A')
        wind_deg = w.wind().get('deg', 'N/A')
        humidity = w.humidity
        temperature = w.temperature('celsius')
        temp = temperature.get('temp', 'N/A')
        temp_min = temperature.get('temp_min', 'N/A')
        temp_max = temperature.get('temp_max', 'N/A')
        clouds = w.clouds
        rain = w.rain.get('1h', 'No rain')  

        result = (f"Weather in {city}:\n"
                  f"Status: {status}\n"
                  f"Temperature: {temp}°C (min: {temp_min}°C, max: {temp_max}°C)\n"
                  f"Humidity: {humidity}%\n"
                  f"Wind: {wind_speed} m/s, {wind_deg}°\n"
                  f"Clouds: {clouds}%\n"
                  f"Rain: {rain} mm")

    except Exception as e:
        result = "Invalid city name. Try again!"

    label.config(text=result)
    

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
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

    

