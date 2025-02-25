def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump

print(zero_fuel(40, 28, 4))
print(zero_fuel(200, 15, 8))
print(zero_fuel(66, 23, 6))
