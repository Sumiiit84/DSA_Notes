
class node:
    def __init__(self, pid, name, pr):
        self.pid = pid
        self.name = name
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    
    def enqueue(self, new_node):

        if self.front is None:
            self.front = self.rear = new_node
            print("Patient added successfully")
            return

        if new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
            print("Patient added successfully")
            return

        temp = self.front

        while temp.next is not None and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        if new_node.next is None:
            self.rear = new_node

        print("Patient added successfully")

    def display_next(self):
        if self.front is None:
            print("Priority queue is empty")
            return

        print("\nNext Patient to be Treated:")
        print("Patient ID:", self.front.pid)
        print("Patient Name:", self.front.name)
        print("Priority:", self.front.priority)

    
    def dequeue(self):
        if self.front is None:
            print("Priority queue is empty")
            return

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print("Patient treated and removed:", temp.name)

    
    def display_all(self):
        if self.front is None:
            print("Priority queue is empty")
            return

        temp = self.front

        print("\nWaiting Patients:")

        while temp is not None:
            if temp.priority == 1:
                pr = "Critical"
            elif temp.priority == 2:
                pr = "Serious"
            else:
                pr = "Normal"

            print("Patient ID:", temp.pid,
                  "Name:", temp.name,
                  "Priority:", pr)

            temp = temp.next



pq = PriorityQueue()


while True:
    print("\n===== HOSPITAL EMERGENCY MANAGEMENT =====")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")

        print("1. Critical")
        print("2. Serious")
        print("3. Normal")

        pr = int(input("Enter Priority: "))

        if pr < 1 or pr > 3:
            print("Invalid Priority!")
        else:
            pq.enqueue(node(pid, name, pr))

    elif choice == 2:
        pq.display_next()

    elif choice == 3:
        pq.dequeue()

    elif choice == 4:
        pq.display_all()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
