import ctypes

class MeraList:
    def __init__(self):
        self.size = 0
        self.n = 0 
        
        
    def __make_array(self,capacity):
        # craete a C type array(static,referential) with size capacity
        return (capacity*ctypes.py_object)()  
      
    def input(self):
        if self.size == 0:
            self.size = int(input("enter size of an array: "))
            self.A = self.__make_array(self.size)
        while self.n < self.size:
            Value = int(input(f"enter value at index {self.n} in array: "))
            self.A[self.n] = Value
            self.n += 1
        
    def selection_sort(self):
        for i in range(0,self.n - 1,1):
            min = self.A[i]
            self.index = i
            for j in range(i+1,self.n,1):
                if min > self.A[j]:
                    min = self.A[j]
                    self.index = j
            self.temp = self.A[i]
            self.A[i] = min
            self.A[self.index] = self.temp
            
    def __len__(self):
        return self.n   
        
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'

L = MeraList()
L.input()
print(L)
L.selection_sort()
print(L)