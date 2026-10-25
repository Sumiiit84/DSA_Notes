# a queue is a linear data structure
# enqueue() insert (add) an iteam to the queue
# dequeue() remove (access) an iteam from the queue.
# front refered by element first
# rear refered by last element
# (rear + 1) % size use this formula for adding new element in circular queue

#Linear Queue using lincked list
class Node:
    def __init__(self, data , next = None):
        self.data = data
        self.next = next

class LQueue:
    def __init__(self):
        self.front = self.rear = None
    def enqueue(self, data):
        if self.rear:
            self.rear.next = data
            self.rear = data
        else:
            self.front = self.rear=data 
    def dequeue(self):
        temp = self.front
        print('delete node : ' , temp.data)
        self.front = self.front.next
        if(self.front == None):
            print('Queue is Empty Now')
            self.rear = None
        temp = None
        
    def print(self):
        if(self.front == None):
            print('Queue is Empty Now')
        else:
            temp = self.front
            while(temp):
                print(temp.data , end=' -> ')
                temp = temp.next
            print('NULL')
obj = LQueue()

obj.print()