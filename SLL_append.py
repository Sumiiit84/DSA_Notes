#Append or a add a data 
class Node:       
    #[data , -> ]                            
    def __init__(self, data , next = None):
        self.data = data
        self.next = next
        
class SLL:
    # head -> [first node]
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
        
    def print(self):
        t1 = self.head
        
        while(t1 != None):
            print(t1.data , end = " -> ")
            t1 = t1.next
        print('NONE')
    
obj = SLL()
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.append(5)
obj.print()




