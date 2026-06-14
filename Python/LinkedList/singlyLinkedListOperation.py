class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
    
    def __len__(self):
        return self.n
    
    def input(self):
        self.n = int(input("Enter size of node: "))
        for i in range(1,self.n+1,1):
            nodeValue = int(input(f"enter value of {i} node: "))
            newNode  = Node(nodeValue)
            
            newNode.next = None
            if self.head == None: 
                self.head = newNode
                temp = self.head
                
            temp.next = newNode 
            temp = newNode
                       
            
            
    def insertAtBegining(self):
        if self.n == 0:
            self.input()
        newNodeValue = int(input(f"enter value of node: "))
        
        newNode = Node(newNodeValue)
        
        newNode.next = self.head
        
        self.head = newNode
         
    def __str__(self):
        curr = self.head
        result = ''
        while curr!= None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]        
            
L = LinkedList()
while True:
    print("\nChoose an operation:")
    print("1. Input nodes")
    print("2. Display Linked list values")
    print("3. Insert new node")
    print("4. Exit")
  
    choice = int(input("Enter choice: "))

    match choice:   # switch-case alternative in Python 3.10+
        case 1:
            L.input()
        case 2:
            print(L)
        case 3:
            L.insertAtBegining()
        case 4:
            print("Exiting...")
            break
        case _:
            print("Invalid choice! Try again.")
