
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BSL:
    def __init__(self):
        self.root = None

    def insert(self, newNode):
        if self.root is None:
            self.root = newNode
        else:
            temp = self.root
            while True:
                if newNode.data < temp.data:
                    if temp.left is None:
                        temp.left = newNode
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = newNode
                        return
                    else:
                        temp = temp.right

    def findminmax(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root
        while temp.left:
            temp = temp.left
        print("Minimum Value is :-", temp.data)

        temp1 = self.root
        while temp1.right:
            temp1 = temp1.right
        print("Maximum Value is :-", temp1.data)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=' -> ')
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.data, end=' -> ')
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=' -> ')

    def get_succ(self, root):
        temp = root.right
        while temp.left:
            temp = temp.left
        return temp

    def delete(self, root, value):
        if root is None:
            return None

        if value < root.data:
            root.left = self.delete(root.left, value)

        elif value > root.data:
            root.right = self.delete(root.right, value)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            succ = self.get_succ(root)
            root.data = succ.data
            root.right = self.delete(root.right, succ.data)

        return root


# Main program
b = BSL()
b.insert(Node(100))
b.insert(Node(10))
b.insert(Node(450))
b.insert(Node(0))
b.insert(Node(65))
b.insert(Node(300))

b.inorder(b.root)
print("\n")
b.delete(b.root , 450)
b.inorder(b.root)
                            
            
        