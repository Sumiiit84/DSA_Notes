class Node:
    def __init__(self, pid , name, pr):
        self.pid = pid
        self.name = name
        self.pr = pr
        self.next = None
    
class priorityqueue:
    def __init__(self):
        self.front = self.rear = None
        
    def enqueue(self, newNode):
        if self.front is None:
            self.front = self.rear = newNode
            return
         # [1 > 2 > 3]
        if newNode.pr < self.front.pr:
            newNode.next = self.front
            self.front = newNode
            return
        
        temp = self.front
        while temp.next is not None and temp.next.pr <= newNode.pr:
            temp = temp.next
            
        newNode.next = temp.next
        temp.next = newNode
        
        if newNode.next is None:
            self.rear = newNode
            
    def display(self):
        if self.front is None:
            print("there is no data")
            return
        temp = self.front
        while(temp.next is not None):
            print(temp.pid , '' , temp.name , '', temp.pr) 
            temp.next = temp
            
obj = priorityqueue()

while(True):
    print('Hospital System Management')
    print('''
          1 : 'Add Patient'
          2 : 'display all'
          ''')
    choice = int(input('Enter a Choise :- '))
    
    if choice == 1:
        pid = int(input('Enter a patient id :- '))
        name = input('Enter a patient name :- ')
        print('''
              1 :- critical
              2 :- serious
              3 :- normal
              ''')
        pr = int(input('Enter a priority :- '))
        obj.enqueue(Node(pid,name,pr))
    
    elif choice == 2:
        obj.display()
        
    else:
        print('Done')
        break
        