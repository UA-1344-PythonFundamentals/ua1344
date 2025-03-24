import tkinter as tk
from pyowm import OWM

# API KEY для OpenWeatherMap
API_KEY = 'ef2206ff5da67de63306d0b143e20872'

# Ініціалізація OWM
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Функція для отримання погодних даних
def get_weather():
    city = entry_field.get()  # Отримуємо місто з поля введення
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        weather_info = f"Weather in {city}:\n" \
                       f"Condition: {w.detailed_status}\n" \
                       f"Wind: {w.wind()}\n" \
                       f"Humidity: {w.humidity}%\n" \
                       f"Temperature: {w.temperature('celsius')['temp']}°C\n" \
                       f"Cloudiness: {w.clouds}%"
    except Exception as e:
        weather_info = f"Error: {str(e)}"

    label.config(text=weather_info)  # Виводимо отриману погоду в лейбл

# Створення головного вікна
HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

# Створення полотна для основного вікна
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Верхній фрейм для вводу міста
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Поле вводу міста
entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

# Кнопка для отримання погоди
button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

# Нижній фрейм для виведення результатів
lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# Лейбл для виведення погоди
label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

# Запуск головного циклу
root.mainloop()
