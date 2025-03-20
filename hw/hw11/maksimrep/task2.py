# Write a program that analyzes the entered number and, depending on the number, returns the day of the week corresponding to this number (1 - Monday, 2 - Tuesday, etc.). Take into account cases of entering numbers of 8 or more, as well as cases of entering non-numeric data.

def анализировать_день_недели():
    try:
        день = int(input("Введите число от 1 до 7: "))
        
        if день < 1 or день > 7:
            raise ValueError("Число должно быть от 1 до 7!")
        
        if день == 1:
            print("Понедельник")
        elif день == 2:
            print("Вторник")
        elif день == 3:
            print("Среда")
        elif день == 4:
            print("Четверг")
        elif день == 5:
            print("Пятница")
        elif день == 6:
            print("Суббота")
        elif день == 7:
            print("Воскресенье")
    
    except ValueError as e:
        print(f"Ошибка: {e}")

анализировать_день_недели()
