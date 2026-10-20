
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
    
    def insert_any_position(self, data , pos):
        # check at first position
        temp = Node(data)
        t1 = self.head
        if(pos == 1):
            self.head = temp
            self.head.next = t1
            return
        else:
            for i in range(pos - 2):
                t1 = t1.next
            
            temp.next = t1.next
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
    
    def search(self, value):
        temp = self.head
        while(temp.next != None):
            if(temp.data == value):
                print("Element is Found :- " , temp.data)
                return
            else:
                temp = temp.next
        print('Element is Not Found' , value)
    
    def updating_a_data(self, old, new):
        temp = self.head
        while(temp != None):
            if(temp.data == old):
                temp.data = new
                return
            else:
                temp = temp.next
                
    def find_middle(self):
        temp = self.head
        mid = self.head
        prev = self.head
        while(temp != None and temp.next != None):
            mid = prev.next 
            prev = prev.next
            temp = temp.next.next 
              
        
        print('Middle data is :- ' , mid.data) 
         
        
    def find_middle_del(self):
        temp = self.head
        mid = self.head
        prev = self.head
        while(temp != None and temp.next != None):
            mid = prev.next 
            t = prev
            prev = prev.next
            temp = temp.next.next 
                      
                
        print('Middle data is :- ' , mid.data)
        t.next = mid.next
   
    def sorting(self):
        temp = self.head
        while(temp != None):
            cur = temp.next
            while(cur != None):
                if(temp.data > cur.data):
                    temp.data , cur.data = cur.data , temp.data
                    
                cur = cur.next
                
            temp = temp.next
           
    def concatination(self):
        temp = self.head
        
        while(temp.next != None):
            temp = temp.next
            
        temp.next = obj1.head   
        
    def reverse(self):
            curr = self.head
            prev = None
            while(curr):
                nextnode = curr.next    
                curr.next = prev
                prev = curr
                curr = nextnode
            self.head = prev       
                
    def sum_consecutive(self):
        temp = self.head
        sum = 0
        while(temp.next != None):
            sum = temp.data + temp.next.data 
            temp = temp.next 
            
        print(sum)  
        
    def sum_of_nodes(self):
        temp = self.head
        sum = 0
        while(temp != None):
            sum += temp.data   
            temp = temp.next
            
        print(sum)  
        
    def del_alternate(self):
            prev = self.head
            temp = self.head.next
            while(prev != None and temp != None):
                prev.next = temp.next
                temp = None      #delete a node
                prev = prev.next
                temp = prev.next
                if(prev != None):
                    temp = prev.next
                    
    def len(self):
        temp = self.head
        count = 0
        while(temp != None):
            count += 1
            temp = temp.next
            
        print(count)
            
                               
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
obj.len()
obj.print()
