class Sorting:
    def heapSort(self,arr,n):
        
        if n > 1:
            self.heapify(arr,n)
            
            for i in range(n-1,1,-1):
                arr[0],arr[i] = arr[i],arr[0]
                self.heapSort(arr,i)
    
    def heapify(self,arr,n):
        
        for i in range(0,n,1):
            left = 2*i + 1
            right = 2*i + 2
            if left < n:
                if arr[i] < arr[left]:
                    arr[left],arr[i] = arr[i],arr[left]
            if right < n:
                if arr[i] < arr[right]:
                    arr[right],arr[i] = arr[i],arr[right]
                    
arr = [4,10,3,5,1]
print(arr)

sort = Sorting()
sort.heapSort(arr,len(arr))

print(arr)