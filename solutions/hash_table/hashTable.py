
hash_array_size=10;
hash_array=[None]*hash_array_size
class MyList(object):
	
	def __init__(self, v):
		self.value=v
		self.next_node=None


def hash_calculate(number):
	return number%hash_array_size

def insert_to_hash(number):
	node=MyList(number)
	hash_value=hash_calculate(number)
	if hash_array[hash_value] == None:
		hash_array[hash_value]= node

	else:
		this_node=hash_array[hash_value]
		while this_node.next_node!=None:
			# Duplicate values will not be storaed
			if this_node.value == number:
				return;
			this_node=this_node.next_node
		
		# Duplicate values will not be storaed
		if this_node.value != number:
			this_node.next_node=node

def listChain (array_location):
	if (array_location > (hash_array_size-1)):
		print ("Invalid array location")
		return 
	this_node=hash_array [array_location]
	if this_node==None:
		print ("Location is empty")
		return
	print ("-----------------")
	while this_node !=None :
		print (this_node.value)
		this_node=this_node.next_node
	print ("-----------------")
	print ("That's all")
	print ("Note : I have not stored any duplicate values to save space")
	
def input_from_user():
	print ("How many numbers you want to enter :")
	number_of_element=int(input())
	numbers=[]
	i=0

	while i< number_of_element:
		print ("Enter the number : ")
		number_to_insert=input()
		insert_to_hash(int(number_to_insert))
		i=i+1

def search(number_to_search):
	hash_val=hash_calculate(number_to_search)

	this_node=hash_array [hash_val]

	while this_node !=None :
		if this_node.value == number_to_search:
			print ("Number is available")
			return
		this_node=this_node.next_node
	print ("Number is not available")

def remove_number():
	print ("Enter the number to remove :")
	number_to_remove=input()
	hash_val=hash_calculate(int(number_to_remove))

	this_node=hash_array [hash_val]

	if this_node == None:
		print ("Number does not exists")
		return

	if this_node.value == int (number_to_remove):
		hash_array [hash_val]=this_node.next_node
		del this_node
		print("Removed the number")
		return

	next_node = this_node.next_node

	while this_node != None :
		if this_node.value == int (number_to_remove):
			previous_node.next_node = next_node
			del this_node
			print ("Removed the number")
			return

		previous_node = this_node
		this_node = this_node.next_node
		if this_node != None :
			next_node = this_node.next_node

	print ("Number does not exists")

input_from_user()

while True:
	print ("Options : \n 1. Search a number \n 2. Enter New Number to list \n 3. List all the values of a location \n 4. Remove a number\n 5. Exit")
	option=input()
	
	if option=="1":
		print ("Enter the numner to search :")
		number_to_search=input()
		search(int(number_to_search))
	elif option=="2":
		input_from_user()
	elif option=="3":
		print ("Enter the array location to list. Location range is 0 to {0}".format((hash_array_size-1)))
		number_to_search=input()
		listChain(int(number_to_search))
	elif option=="4":
		remove_number()
	elif option=="5":
		exit()
	else:
		print ("Invalid option")
