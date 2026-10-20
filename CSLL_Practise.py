class Node:                                   
    def __init__(self, data , next = None):
        self.data = data
        self.next = next
        
class SLL:
    def __init__(self, head = None):
        self.head = head