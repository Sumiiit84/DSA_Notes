

class Node:                                   
    def __init__(self, data , next = None):
        self.data = data
        self.next = next
        
class SLL:
    def __init__(self, head = None):
        self.head = head
        
    def append(self, data):
        temp = Node(data)
        
        if(self.head == None):
            self.head = temp
            return
            
        t1 = self.head

        while(t1.next != None):
            t1 = t1.next
        t1.next = temp
        
    def insert(self, data, pos):
        temp = Node(data)
        if pos == 1:
            temp.next = self.head
            self.head = temp
            return
        p = 1
        t = self.head
        while p != pos - 1 and t.next != None:
            t = t.next
            p += 1

        temp.next = t.next
        t.next = temp
        
    def print(self):
        t1 = self.head
        
        while(t1 != None):
            print(t1.data , end = " -> ")
            t1 = t1.next
        print('NONE')
    
obj = SLL()
obj1 = SLL()
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.append(5)
obj.insert(0 , 3)
obj.print()




