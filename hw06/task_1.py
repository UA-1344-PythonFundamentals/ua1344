# Initialize the range from 1 to 10
for num in range(1, 11):
    # Check if the number is even and divisible by 2
    if num % 2 == 0:
        print(f"{num} is an even number divisible by 2.")
    
    # Check if the number is odd and divisible by 3
    if num % 2 != 0 and num % 3 == 0:
        print(f"{num} is an odd number divisible by 3.")
    
    # Check if the number is not divisible by 2 or 3
    if num % 2 != 0 and num % 3 != 0:
        print(f"{num} is not divisible by 2 or 3.")