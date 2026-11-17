class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # 1. Enqueue
    def enqueue(self, data):
        temp = Node(data)

        if self.rear is None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp

    # 2. Dequeue
    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            print("Dequeued Element:", temp.data)

            self.front = self.front.next

            if self.front is None:
                self.rear = None

    # 3. Display
    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Queue Contains...")

            temp = self.front

            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")
    
    def reverse_queue(self):
        stack = []
        temp = self.front

        while temp:
            stack.append(temp.data)
            temp = temp.next

        self.front = self.rear = None

        while stack:
            self.enqueue(stack.pop())
    
    def merge_queue(self, q2):
        temp = q2.front

        while temp:
            self.enqueue(temp.data)
            temp = temp.next
            
    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False

            temp1 = temp1.next
            temp2 = temp2.next

        return temp1 is None and temp2 is None

q1 = Queue()
q2 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

print("\nCheck Identical Queues:")
if q1.identical(q2):
    print("Queues are Identical")
else:
    print("Queues are Not Identical")