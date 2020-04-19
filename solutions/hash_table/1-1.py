"""
Problem Number 1.1
Problem : Implement an algorithm to determine if a string has all unique characters.
"""
import array
class hash_table_class(object):

	def __init__ (self):
		self.hash_table = [None]*128

	def calculate_hash(self,char_to_hash):
		return ord(char_to_hash)

	def insert_to_hash (self,string):

		for char_from_string in string:
			hash_value=self.calculate_hash(char_from_string)
			
			# If a char already exists on this location means the string having a duplication char. No need to check further
			if self.hash_table[hash_value] != None:
				print("There are duplicate characters")
				return
			
			self.hash_table[hash_value]=char_from_string

		# Control reached here means there is no duplicate char
		print("All character are unique")

print("Please enter the ASCII string")
string=input()

# Total characters in ASCII is 128. So, If a string contains more than 128 chars then there are duplicates
if len(string) > 128:
	print("There are duplicate characters")

HT = hash_table_class()
HT.insert_to_hash(string)
