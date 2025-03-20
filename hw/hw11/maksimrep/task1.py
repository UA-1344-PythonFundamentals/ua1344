#Write a program that prompts the user to enter their age, and then displays a message indicating whether the age is even or odd. The program should provide the option to enter a negative number, and throw an exception in that case. The main code should call a function that processes the information entered.

def обработать_возраст():
    try:
        возраст = int(input("Введите свой возраст: "))
        
        if возраст < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        
        if возраст % 2 == 0:
            print(f"Ваш возраст {возраст} является четным.")
        else:
            print(f"Ваш возраст {возраст} является нечетным.")
    
    except ValueError as e:
        print(f"Ошибка: {e}")

# Главный код
обработать_возраст()
