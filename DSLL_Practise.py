class node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
class DSLL :
    def __init__(self , head = None):
        self.head = head
    
    def append(self, data):
        temp = node(data)
        if(self.head == None):
            self.head = temp
            return
        else:
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
            temp.prev = t1
    
    def print(self):
                t1 = self.head
                while(t1 != None):
                    print(t1.data , end = " ⇄  ")
                    t1 = t1.next
                print('NONE')

list = DSLL()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.print()            
