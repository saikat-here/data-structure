"""
Problem Number 2.5
Problem : You have two numbers represented by a linked link, where each node contains a single digit. The digits are stored in reverse order, 
such that the 1's digit is at thea head of the list. Wite a function that adds the two numbers and returns the sum as a linked list.
Example :
INPUT : (7 -> 1 -> 6) + (5 -> 9 -> 2)
OUTPUT : 2 -> 1 -> 9
"""



class MyNode(object):
	def __init__(self,val= None):
		self.val = val
		self.next = None


class operation(object):
	def __init__(self):
		self.num1_head = MyNode()
		self.num2_head = MyNode()
		self.result_head = MyNode()


	def insert(self,head):
		cur = head
		print("Enter the number")
		val = input()

		while cur.next != None:
			cur = cur.next

		newNode= MyNode(val)
		cur.next = newNode
		self.print_val(head)

	def print_val(self,head):
		cur = head.next
		while cur != None :
			print(cur.val)
			cur = cur.next

	def getNumber(self,head):
		
		cur = head.next
		c=1
		num1=0
		
		while cur!= None:
			num1 = num1 + ( int(cur.val) * c)
			cur = cur.next
			c = c*10

		return num1


	def doSum(self):
		num1 = self.getNumber(self.num1_head)
		print ("Number1-"+str(num1))
		num2 = self.getNumber(self.num2_head)
		print ("Number2-"+str(num2))
		
		result = num1 + num2
		
		while result >0:
			val = result % 10
			
			cur = self.result_head
			while cur.next != None:
				cur = cur.next
			
			newNode = MyNode(val)
			cur.next = newNode
			
			result = int (result / 10)

		print("Printing the result list")
		self.print_val(self.result_head)	

	def menu(self):
		
		while True:
			print("1. Insert to Num1   2. Insert to Num2.   3.Sum   4.Exit")
		
			op = input()
			if op == "1":
				self.insert(self.num1_head)
			elif op =="2":
				self.insert(self.num2_head)
			elif op =="3":
				self.doSum()
			elif op=="4":
				exit()


opObject = operation()
opObject.menu()
