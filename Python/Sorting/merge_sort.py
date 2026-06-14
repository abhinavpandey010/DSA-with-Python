import ctypes

import ctypes
class MeraList:
    def __init__(self):
        self.size = 5
        self.n = 0
        self.A = self.__make_array(self.size)
        
    def __make_array(self,capacity):
        return (capacity * ctypes.py_object)()
    
    def input(self):
        for i in range(self.size):
            self.A[i] = int(input(f"enter value at index {i} : "))
            self.n += 1
    def mergeSort(self):
        
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
l1 = MeraList()
l1.input()
print(l1)          
l2 = MeraList()          
l2.input()
print(l2)          
class MergeArrays:
    def __init__(self,l1,l2):
        self.A = l1
        self.B = l2
        self.size = self.A.n + self.B.n
        self.n = 0
        self.C = self.__make_array(self.size)
    def __make_array(self,capacity):
        return (capacity * ctypes.py_object)()
    def merge(self):
        
        for i in range(self.size):
            if(i < self.A.n):
                self.C[i] = self.A.A[i]
                self.n += 1
            else:
                self.C[i] = self.B.A[i-self.A.n]
                self.n += 1
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.C[i]) + ','
        return '[' + result[:-1] + ']'   
l3 = MergeArrays(l1,l2)
l3.merge()    
print(l3)
        
    