"""
Problem Number 2.2
Problem : Implement an algo to find the Kth to last element of a singly linked list
"""

class Node(object):
	def __init__(self, val = None):
		self.val = val
		self.next = None

class ListOp(object):
	def __init__(self):
		self.head = Node()

	
	def insert(self):
		print("Enter the value")
		val = input()
		cur = self.head

		new_node = Node()
		new_node.val = val

		while cur.next != None:
			cur = cur.next

		cur.next = new_node
	
	def print_all(self):
		cur = self.head
		
		while cur.next != None:
			cur = cur.next
			print(cur.val)
			

	def find_k_th (self):
		print("Enter the Kth position")
		k_th = int(input())
		count = 0
		
		cur2 = self.head

		while cur2.next != None:
			cur2 = cur2.next
			count = count + 1
			print ("Count : "+str(count))

			if count==k_th:
				print("Break")
				break

		if k_th != count :
			print ("Invalid Kth")
			return
		
		cur1 = self.head.next
		while cur2.next != None :
			cur2 = cur2.next
			cur1 = cur1.next
		
		print ( cur1.val )


op = ListOp()

while True:
	print ("1. Insert  2. List 3. Find Kth 4. Exit")
	operation = input()

	if operation == "1":
		op.insert()
	elif operation == "2":
		op.print_all()
	elif operation == "3":
		op.find_k_th()
	elif operation == "4":
		exit()
			

