"""
Problem Number 1.2
Problem : Given two string, decide if one is a permutation of the other one.
"""

import array

class permutation(object):

	def __init__(self):
		self.hash_for_s1 = [0]*128
		self.hash_for_s2 = [0]*128

	def check_permutation(self):
		
		print ("Please enter the first string : ")
		s1=input()

		print("Please enter the second string : ")
		s2=input()

		if len(s1) != len(s2) :
			print ("Not permutation to each other")
			return

		for i in s1:
			self.hash_for_s1[ord(i)] =  self.hash_for_s1[ord(i)] + 1

		for i in s2:
			self.hash_for_s2[ord(i)] = self.hash_for_s2[ord(i)] + 1 

		for i in range (0,127):
			if self.hash_for_s1[i] != self.hash_for_s2[i] :
				print ("Not permutation to each other")
				return 
		print ("Permutation to each other")


p = permutation()
p.check_permutation()
