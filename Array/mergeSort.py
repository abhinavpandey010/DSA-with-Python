
class Sorting:
    def mergeSort(self,arr,start,end):
        
        if start >= end:
            return [arr[start]]
        
        mid = (start + end) // 2 
        left = self.mergeSort(arr,start,mid)
        right = self.mergeSort(arr,mid+1,end)
        
        return self.merge(left,right)
    
    def merge(self,left,right):
        
        result = []
        i = 0
        j = 0
    
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            
        
        while i < len(left):
            
            result.append(left[i])
            i += 1
            
        
        while j < len(right):
            result.append(right[j])
            j += 1
            
        
        return result

sort = Sorting()
arr = [15,8,12,0,10]
afterSorting = sort.mergeSort(arr,0,len(arr) - 1)
print(afterSorting)