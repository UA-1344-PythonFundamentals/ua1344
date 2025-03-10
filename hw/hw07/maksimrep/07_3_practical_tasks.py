# I. Jenny's secret message
def приветствие(имя):
    if имя == "Johnny":
        return "Привет, моя любовь!"
    return "Привет, {имя}!".format(имя=имя)


# II. Find The Distance Between Two Points
def расстояние(x1, y1, x2, y2):
    return round(((x2-x1)**2+(y2-y1)**2)** .5, 2)


# III. No yelling!
def фильтровать_слова(строка):
    строка_с_заглавной = строка.capitalize()
    return " ".join(строка_с_заглавной.split())


# IV. Convert a Number to a String
def число_в_строку(число):
    число_в_строку = число
    return str(число_в_строку)


# V. Reversing Words in a String
def перевернуть(строка):
    результат = []
    оригинальный_порядок = строка.split()
    for типо_и in range(len(оригинальный_порядок), 0, -1):
        print(типо_и)
        результат.append(оригинальный_порядок[типо_и-1])
    return " ".join(результат)


# VI. Reverse List Order
def перевернуть_список(строка):
    результат = []
    for типо_и in range(len(строка), 0, -1):
        результат.append(строка[типо_и-1])
    return результат
    

# VII. Multiples of 3 or 5
def перевернуть_список(строка):
    return строка[::-1]


# VIII. Will you make it?
def решение(число):
    результат = 0
    типо_и = 0
    while типо_и<число:
        if (типо_и%3 == 0 or типо_и%5 == 0):
            if( типо_и<число):
                результат += типо_и
            else:
                break
        типо_и += 1 

    return результат


# VIII. Will you make it?
def топливо_ноль(расстояние_до_заправки, скорость, остаток_топлива):
    return остаток_топлива >= расстояние_до_заправки  / скорость


# IX. Are You Playing Banjo?
def играешь_ли_на_банджо(имя):
    if(имя[0] == 'Р' or имя[0] == 'р'):
        return имя + " играет на банджо" 
    else:
        return имя + " не играет на банджо"


# X. Convert boolean values to strings 'Yes' or 'No’
def boolean_to_string(b):
    return "True" if b else "False"


# XI. Counting sheep
def считать_овец(овцы):
    результат = 0
    for типо_и in овцы:
        if типо_и:
            результат +=1
            
    return результат


# XII. Is this my tail?
def правильный_хвост(тело, хвост):
    return тело[-1] == хвост
