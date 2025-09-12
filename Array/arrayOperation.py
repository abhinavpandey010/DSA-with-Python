import ctypes

class MeraList:
    
    def __init__(self):
        self.size = 0
        self.n = 0

    def __make_array(self,capacity):
        return (capacity * ctypes.py_object)()
    
    def __resize(self,new_capacity):
        # create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B
        
    def input(self):
        if self.size == 0:
            self.size = int(input("enter size of an array: "))
            self.n = 0
            self.A = self.__make_array(self.size)
        if self.size == self.n:
            print("Array is full so resize your array\n")
            while True:
                newSize = int(input("enter increased size of an array: "))
                if newSize < self.size:
                    print("Please enter increased size")
                    continue
                self.__resize(newSize)
                break
        while self.n < self.size:
            Value = int(input(f"enter value at index {self.n} in array: "))
            self.A[self.n] = Value
            self.n += 1
      
    def insert(self):
        if self.size == 0:
            self.n = 0
            self.size = int(input("enter size of an array before choosing options: "))
            self.A = self.__make_array(self.size)
        if self.size == self.n:
            self.__resize(self.size+1)
            
        while self.n < self.size:    
            values = input("enter position and its value to store in array: ").split()
            if len(values) != 2:
                print("please enter exactly two values")
                continue
            try:
                pos, item = map(int, values)
            except Exception as e:
                print("Error:", e)    
            
            if pos > self.n:
                pos = self.n
            for i in range(self.n, pos, -1):
                self.A[i] = self.A[i-1]
                
            self.A[pos] = item
            self.n += 1
        
    def __len__(self):
        return self.n 
    
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'


# ---------------- MENU (Switch-Case Style) ----------------

L = MeraList()
while True:
    print("\nChoose an operation:")
    print("1. Input elements")
    print("2. Display elements")
    print("3. Insert element")
    print("4. Exit")
  
    choice = int(input("Enter choice: "))

    match choice:   # switch-case alternative in Python 3.10+
        case 1:
            L.input()
        case 2:
            print(L)
        case 3:
            L.insert()
        case 4:
            print("Exiting...")
            break
        case _:
            print("Invalid choice! Try again.")
