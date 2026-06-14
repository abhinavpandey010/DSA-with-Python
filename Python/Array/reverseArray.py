array = [1,2,3,4,5]
print(f'before : {array} ')
for i in range(len(array)//2):
    temp = array[i]
    array[i] = array[len(array) - 1 - i]
    array[len(array) - 1 - i] = temp
    
    
print(f'after : {array} ')