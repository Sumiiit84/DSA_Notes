class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, top=None):
        self.top = top

    def isEmpty(self):
        return self.top is None

    def push(self, new_node):
        temp = Node(new_node)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
            return None
        else:
            temp = self.top
            self.top = self.top.next
            return temp.data

    def reverse_stack(self, s1, s2):
        while not s1.isEmpty():
            s2.push(s1.pop())

    def print(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            print('Stack Contains...')
            temp = self.top
            while temp:
                print(temp.data, end=' -> ')
                temp = temp.next
            print('Null')


s1 = Stack()
s2 = Stack()

s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)

print("Original Stack:")
s1.print()

s1.reverse_stack(s1, s2)

print("Reversed Stack:")
s2.print()     

            
        
        