class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def isEmpty(self):
        return self.front and self.rear is None
        
    def enqueue(self):
        n = int(input("How many elements you want to insert:- "))
        for i in range(n):
            data = int(input("Enter a Elements:- "))
            temp = Node(data)
            if self.rear is not None:
                self.rear.next = temp
                self.rear = temp 
            else:
                self.front = self.rear = temp
                
    def dequeue(self):
        n = int(input("How many time wants delete elements:- "))
        for i in range(n):
            temp = self.front
            self.front = self.front.next
            if(self.front == None):
                self.rear = None
            temp = None
            
        
    def display(self):
        temp = self.front
        print("Queue Structure :- ")
        while(temp is not None):
            print(temp.data , end=' -> ')
            temp = temp.next
        print('NULL')
            
q = Queue()
q.enqueue()
q.dequeue()
q.display()
        