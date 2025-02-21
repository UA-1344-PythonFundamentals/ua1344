#A four-digit natural number is specified:
#- find the product of the digits of this number
#- write the number in reverse order
#- in ascending order, you need to sort the numbers included in the given number

#A four-digit natural number is specified:
a = 7652
print("number =", a)

converted = str(a)

#- find the product of the digits of this number
prod = 1
for x in converted:
    prod = int(x)*prod

print("prod =", prod)

#- write the number in reverse order
revers = converted [::-1]
print("revers =", revers)


#- in ascending order, you need to sort the numbers included in the given number
sorted = sorted(converted)
print("sorted =", sorted)