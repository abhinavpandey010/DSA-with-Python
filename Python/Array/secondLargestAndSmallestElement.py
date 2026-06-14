array = list(map(int,input("enter elements:").split()))


print(f'Array: {array}')

for i in range(len(array)):
    minIndex = i
    
    for j in range(i + 1,len(array)):
        if array[minIndex] > array[j]:
            minIndex = j
    temp = array[i]
    array[i] = array[minIndex]
    array[minIndex] = temp
    
print(f'Second largest element in an Array: {array[len(array) - 2]}')
print(f'Second smallest element in an Array: {array[1]}')
