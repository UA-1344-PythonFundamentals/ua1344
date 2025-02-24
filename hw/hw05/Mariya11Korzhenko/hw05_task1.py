#from int to float

list = [1,2,3,"str"]
result = []

def int_to_float(int_list):
  for i in int_list:
    if(type(i) is int):
      result.append(float(i))
    else: 
      print('type of this element is not int :'+ i)
      return []

  return result

print (int_to_float(list))



