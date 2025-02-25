def correct_tail(body, tail):
    sub = body[-len(tail):] 
    if sub == tail:
        return True
    else:
        return False
    
print(correct_tail("Fox", "x")) 
print(correct_tail("Tiger", "r"))
print(correct_tail("Lion", "n")) 
print(correct_tail("Bear", "a"))