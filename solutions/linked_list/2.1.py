"""
Problem Number 2.1
Problem : Write code to remove duplicates from as unsorted linked list (temp buffer is not allowed)
"""
class Node(object):

    def __init__(self, val = None):
        self.value = val
        self.next = None

class operation(object):

    def __init__(self):
        self.head = Node()

    def insert(self):
        print("Enter the value")
        val = input()
        cur = self.head

        new_node = Node()
        new_node.value= val
        
        while (cur.next != None):
            cur = cur.next

        cur.next = new_node

    def display(self):

        cur = self.head

        while (cur.next != None):
            cur = cur.next
            print(cur.value)

    def remove_duplicate(self):

        cur = self.head
        
        while cur != None:
            cur2 = cur.next

            while cur2 != None:

                print(cur.value)
                print(cur2.value)
                print("*****")
                
                if cur.value == cur2.value:
                    cur.next = cur2.next
                    print("Removed duplicate value "+cur2.value)
                cur2 = cur2.next

            cur = cur.next


op = operation()

while True:
    print("1. Inset 2. Display 3. Remove Duplicate 4. Exit")
    option = input()

    if option == "1":
        op.insert()

    elif option == "2":
        op.display()

    elif option == "3":
        op.remove_duplicate()
        
    elif option == "4":
        exit()
