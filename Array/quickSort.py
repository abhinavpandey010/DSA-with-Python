class Sorting:
    def quickSort(self,arr,low,high):
        
        if low < high:
            
            partition_index = self.partition(arr,low,high)
            self.quickSort(arr,low,partition_index-1)
            self.quickSort(arr,partition_index+1,high)
    
    def partition(self,arr,low,high):
        
        pivot = arr[high]
        i = low -1
        
        for j in range(low,high):
            
            if arr[j] < pivot:
                i+=1
                arr[j],arr[i] = arr[i],arr[j]
        
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1 
arr = [10,7,8,9,1,5]
print(f"Before :{arr}")
sort = Sorting()
sort.quickSort(arr,0,len(arr)-1)
print(f"After :{arr}")