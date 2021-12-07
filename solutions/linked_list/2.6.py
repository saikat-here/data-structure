"""
Problem Number 2.6
Problem : Verify if a linked list is Palindrome or not
"""

class Node (object):
	
	def __init__(self, value = None):
		self.val = value 
		self.next = None

class operation(object):
	
	def __init__(self):
		self.head = Node ()
	

	def insert(self):
		
		cur = self.head 

		print("Enter the value to insert")
		val = input()

		new_node = Node(val)

		while cur.next != None:
			cur = cur.next
		
		cur.next = new_node


	def display(self):
		
		cur = self.head.next
		
		while cur != None:
			cur = cur.next

	def check_palindrome(self):
		stack = []
		fast = self.head.next
		slow = self.head.next	
		
		while (fast != None) and (fast.next != None):
			stack.append(slow.val)
			fast = fast.next.next
			slow = slow.next

			
			

		if (fast != None):
			slow = slow.next

		while slow != None:
			stk_val = stack.pop()

			if stk_val != slow.val:
				print ("Its not Palindrome")
				return
			slow = slow.next

		print (" Its a Palindrome")

op = operation()

while True:
	
	print (" 1.Insert  2. Check Palindrome  3.Display  4. Exit ")
	menu_op = input()

	if menu_op=="1":
		op.insert()
	
	elif menu_op == "4":
		exit()

	elif menu_op=="2":
		op.check_palindrome()

	elif menu_op == "3":
		op.display()

		
