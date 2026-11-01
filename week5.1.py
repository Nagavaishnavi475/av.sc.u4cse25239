class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, n):
        self.head = None

        for i in range(n):
            data = int(input(f"Enter data for node {i + 1}: "))
            self.insert_end(data)

        print("Linked List created successfully")

    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new

    def insert_position(self, data, position):
        new = Node(data)

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            new.next = self.head
            self.head = new
            print("Node inserted successfully")
            return
        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
        else:
            new.next = temp.next
            temp.next = new
            print("Node inserted successfully")

    def delete_value(self, value):
        if self.head is None:
            print("No Data to delete")
            return

        if self.head.data == value:
            self.head = self.head.next
            print("Value deleted")
            return

        temp = self.head

        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print("Value not present")
        else:
            temp.next = temp.next.next
            print("Value deleted")

    def delete_first(self):
        if self.head is None:
            print("No Data to delete")
        else:
            print("Deleted Value =", self.head.data)
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("No Data to delete")

        elif self.head.next is None:
            print("Deleted Value =", self.head.data)
            self.head = None

        else:
            temp = self.head

            while temp.next.next:
                temp = temp.next

            print("Deleted Value =", temp.next.data)
            temp.next = None

    def count(self):
        if self.head is None:
            print("No Linked List")
        else:
            c = 0
            temp = self.head

            while temp:
                c += 1
                temp = temp.next

            print("Number of nodes =", c)

    def display(self):
        if self.head is None:
            print("No Linked List")
        else:
            temp = self.head

            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")

ll = LinkedList()

while True:
    print("\n--- Singly Linked List Operations ---")
    print("1. Create a Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Specific Position")
    print("5. Delete a Value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count Number of Nodes")
    print("9. Display Nodes")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of nodes: "))
        ll.create(n)

    elif choice == 2:
        data = int(input("Enter data: "))
        ll.insert_begin(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        ll.insert_end(data)

    elif choice == 4:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        ll.insert_position(data, position)

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        ll.delete_value(value)

    elif choice == 6:
        ll.delete_first()

    elif choice == 7:
        ll.delete_last()

    elif choice == 8:
        ll.count()

    elif choice == 9:
        ll.display()

    elif choice == 10:
        print("Program ended")
        break

    else:
        print("Invalid choice")
