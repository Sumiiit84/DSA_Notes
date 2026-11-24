class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = self.rear = None
        
    def enqueue(self, data):
        temp = Node(data)
        if self.rear is not None:
            self.rear.next = temp
            self.rear = temp
        else:
            self.front = self.rear = temp
        self.rear.next = self.front
    
    def dequeue(self):
        if self.rear!=None:
            temp=self.front
            print("Node deleted...", temp.data)
            if self.front==self.rear: #deleting last node in queue
                self.front=self.rear=None
            else:
                self.front=self.front.next
                self.rear.next=self.front
            del temp
            return
        else:
            print("Queue is empty...")
    
    def display(self):
        temp = self.front
        while temp:
            print(temp.data , end=' -> ')
            if temp.next == self.front:
                break
            temp = temp.next
        print(temp.next.data)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.display()

        
            
        