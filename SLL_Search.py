
class Node:
    def __init__(self, data , next = None):
        self.data = data
        self.next = next
        
class SLL:
    def __init__(self , head = None):
        
        self.head = head
        
    def append(self, data):
        temp = Node(data)
        if(self.head == None):
            self.head = temp
            return
        else:
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
    
    def search(self, value):
        temp = self.head
        while(temp.next != None):
            if(temp.data == value):
                print("Element is Found :- " , temp.data)
                return
            else:
                temp = temp.next
        print('Element is Not Found' , value)    
              
    def print(self):
        temp = self.head
        while(temp != None):
            print(temp.data , end= ' -> ')
            temp = temp.next
        print('NULL')
        
obj = SLL()
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.append(5)
obj.search(6)
obj.print()