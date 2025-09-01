import ctypes

class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0 
        
        # create ctype array with size = self.size
        self.A = self.__make_array(self.size)
        
    def __make_array(self,capacity):
        # craete a C type array(static,referential) with size capacity
        return (capacity*ctypes.py_object)()  
      
    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
        
        self.A[pos] = item
        self.n = self.n + 1 
    
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
            

    def __resize(self,new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B
        
    def __len__(self):
        return self.n   
        
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'

L = MeraList()
L.insert(0,6)
L.insert(1,9)
L.insert(2,2)
L.insert(3,6)
L.insert(4,9)
L.insert(5,2)
print(L)
L.selection_sort()
print(L)