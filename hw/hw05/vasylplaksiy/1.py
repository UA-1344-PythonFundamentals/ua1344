# task 1
intList = [0,2,55,6,7]
print("integer: ", intList)
for i,el in enumerate(intList):
    intList[i] = float(el)
print("float: ", intList)

# task 1
printToN = int(input("print fibonacci numbers up to: "))
fNBefore, fCurrent = 0, 0
fList = []

if printToN < 0:
    print("Number can't be negative")
else:
    while fCurrent <= printToN:
        if fCurrent==0:
            fList.append(fCurrent)
            fCurrent = 1
        elif fCurrent==1 and fNBefore == 0:
            fList.append(fCurrent)
            fList.append(fCurrent)
            fNBefore = 1
        else:
            fNBefore, fCurrent = fCurrent, fNBefore + fCurrent
            if fCurrent>printToN:
                break
            fList.append(fCurrent)
print(f"Fibonacci numbers <= {printToN}:", fList)

# task 3
inputFactorial = abs(int(input("calc factorial of(>=0): ")))
factCount = 0
factSum = 1
while factCount <= inputFactorial:
    if factCount == 0:
        factSum = 1
        factCount+=1
    else:
        factSum *= factCount
        factCount += 1
print(f"result {inputFactorial}!={factSum}")
