import geometry

def main_calculates():
    print("Введіть фігуру для розрахунку площі:")
    print("1 - Прямокутник")
    print("2 - Трикутник")
    print("3 - Коло")

    choice = input("Введіть номер фігури: ")

    if choice == "1":
        a = float(input("Введіть довжину (см): "))
        b = float(input("Введіть ширину (см): "))
        print("Площа прямокутника (см²):", geometry.rectangle_area(a, b))

    elif choice == "2":
        h = float(input("Введіть высоту (см): "))
        a = float(input("Введіть основу (см): "))
        print("Площа трикутника (см²):", geometry.triangle_area(h, a))

    elif choice == "3":
        r = float(input("Введіть радіус (см): "))
        print("Площа кола (см²):", geometry.circle_area(r))

    else:
        print("Некоректний вибір!")

if __name__ == "__main__":
    main_calculates()