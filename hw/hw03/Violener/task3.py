
# 1. 
text = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."

count_better = text.lower().count("better")

count_never = text.lower().count("never")

count_is = text.lower().count("is")

uppercase = text.upper()

replase_text = text.replace("i", "&")

print(f"'better': {count_better}, 'never': {count_never}, 'is': {count_is}")
print("uppercase", uppercase)
print("replase", replase_text)
# 2.
number = "7345"

digits = [int(number[0]) ,int(number[1]) ,int(number[2]) ,int(number[3])]

product = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])


reverse_number = int(number[::-1])


sorted_digits = sorted(digits)

print(product)
print(reverse_number)
print(sorted_digits)

# 3.
a = 5
b = 10

a, b = b, a  

print(f"a = {a}, b = {b}")

