class node:
    def __init__(self,value):
        self.prev = None
        self.data = value
        self.next = None
class linked_list :
    def __init__(self):
        self.head = None
    def append(self, new_node):
        temp =self.head
        if temp:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else: #First Node
            self.head = new_node
    def insert(self,new_node,pos):
        temp = self.head
        if pos == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            p =  1 
            while(p!= pos - 1 and temp.next) :
                temp = temp.next
                p+=1
            new_node.next = temp.next
           
            if temp.next:    # Last Node
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev =temp
    def reverse(self):
        temp = self.head
        if temp == None:
            print("List is empty")
            return 
        while temp.next:
            temp = temp.next 
        print("\nList elements in reverse order: ")
        while temp:
            print(temp.data, end = " ")
            temp = temp.prev
            
    def delete(self, value):
        temp = self.head
        if temp.data == value:
            self.head = self.head.next
            self.head.prev = None
            
        else:
            while(temp.data != value and temp):
                temp = temp.next
                if temp == None:
                    print('Value is not present in list')
                    return 
            temp.prev.next = temp.next
            if temp.next :   # Not the last node
                temp.next.prev = temp.prev
            temp = None
    def count_occurence(self, value):
        count = 0
        temp = self.head
        while(temp):
            if temp.data == value:
                count += 1
            temp = temp.next
        print('Ocurrence are :- ' , count)
    
    def swap_first_last_node(self):
        temp = node1 = self.head #node1 is first node
        while(temp.next != None):   #temp is last node
            temp = temp.next
        
        temp.next = node1.next
        node1.next = None
        node1.prev = temp.prev
        temp.prev.next = node1
        temp.prev = None
        self.head = temp 
        
        
    def print(self):
            t1 = self.head
            while(t1 != None):
                print(t1.data , end = " <-> ")
                t1 = t1.next
            print('NONE')
    
list = linked_list()
list.append(node(1))
list.append(node(2))
list.append(node(3))
list.append(node(4))
list.append(node(5))
list.swap_first_last_node()

#list.count_occurence(1)
'''
list.delete(3)
list.delete(1)
list.delete(5)
'''
list.print()
#list.reverse()
