class Node:                                   
    def __init__(self, data , next = None):
        self.data = data
        self.next = next
        
class CSLL:
    def __init__(self, head = None):
        self.head = head
        
    def append(self, data):
        temp = Node(data)
        if(self.head == None):
            self.head = temp
            temp.next = self.head
            return
        else:
            t1 = self.head
            while(t1.next != self.head):
                t1 = t1.next
            t1.next = temp
            temp.next = self.head
            
    def prints(self):
        temp = self.head
        while(True):
            print(temp.data , end=' -> ')
            temp = temp.next
            if(temp == self.head):
                break
        print("HEAD")

obj = CSLL()
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.append(5)
obj.prints()