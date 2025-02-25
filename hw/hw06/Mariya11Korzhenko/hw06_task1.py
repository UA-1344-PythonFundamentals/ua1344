def check_divide(range):
    divided_by_2 = []
    divided_by_3 = []
    not_divided_by_2_and_3 = []

    for i in range:
        if i%2 == 0:
            divided_by_2.append(i)
        if i%3 == 0:
            divided_by_3.append(i)
        if i%2>0 and i%3>0:
            not_divided_by_2_and_3.append(i)

    print(f"Divided by 2: {divided_by_2}")
    print(f"Divided by 3: {divided_by_3}")
    print(f"Not divided by 2 and 3: {not_divided_by_2_and_3}")

check_divide(range = [1,2,3,33,5,6,12,8,9,10])
