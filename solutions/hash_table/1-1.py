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

			if self.hash_table[hash_value] != None:
				print("There are duplicate characters")
				return
			
			self.hash_table[hash_value]=char_from_string
		
		print("All character are unique")

print("Please enter the ASCII string")
string=input()

if len(string) > 128:
	print("There are duplicate characters")

HT = hash_table_class()
HT.insert_to_hash(string)
