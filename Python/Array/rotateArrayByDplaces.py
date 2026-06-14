def rotateArr(arr, d):
        n = len(arr)
        d = d % n   
        
        reverse(arr, 0, d-1)
        reverse(arr, d, n-1)
        reverse(arr, 0, n-1)

def reverse(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

arr = [1,2,3,4,5,6,7,8,9]
print(arr)
rotateArr(arr,2)

print(arr)