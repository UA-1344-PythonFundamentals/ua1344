def process_age():
    try:
        # Запитуємо вік користувача
        age = int(input("Enter your age: "))
        
        # Перевірка на від'ємне значення
        if age < 0:
            raise ValueError("Age cannot be negative!")
        
        # Перевірка чи вік парний або непарний
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")
    
    except ValueError as e:
        # Виводимо повідомлення про помилку, якщо введено неправильне значення
        print(f"Error: {e}")

# Викликаємо функцію для обробки віку
process_age()
