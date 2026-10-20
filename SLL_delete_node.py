
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
            
    def delete_a_node(self, value):
        temp = self.head
        if(temp.data == value):
            self.head = temp.next
            return temp
        else:
            prev = self.head
            while(temp.data != value):
                prev = temp
                temp = temp.next
                
            prev.next = temp.next
            return temp     
              
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
obj.delete_a_node(5)
obj.print()