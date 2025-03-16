def process_input(idx):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    try:
        if idx > 7 or idx < 1:
            raise ValueError('Day index must be from 1 to 7')
        
        print(f'Day under the index {idx} is {days[idx - 1]}')
    except ValueError as err:
        print(err)

try:
    idx = int(input("Enter weekday index: "))
    process_input(idx)
except ValueError:
    print("Please enter a valid integer for index")