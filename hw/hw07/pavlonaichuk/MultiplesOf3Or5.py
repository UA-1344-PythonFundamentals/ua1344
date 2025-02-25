def solution(number):
    if number < 0:
        return 0 
    return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0)

print(solution(40))  
print(solution(20))  
print(solution(1))   
print(solution(-15))  
print(solution(22))
