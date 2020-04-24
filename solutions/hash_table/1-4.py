"""
Problem Number 1.4
Problem : Given a string, write an alogorithm to check if it is a permutation of palindrome. A permutation is a rearrangement of letters. The palindromedoes not need to be a dictionary words.
"""

import array

class palindrome(object):

	def check_for_permutation_palindrome(self):
		
		count_char = [0]*128  # Number of ASCII char is 128 

		print ("Please enter the string : ")
		s = input()

		for i in s:
			count_char [ ord(i) ] = count_char [ ord(i) ] + 1

		is_odd = False

		for i in range (0,127):
			
			if count_char[i] % 2 == 1:
				if is_odd == True:
					print ("Permutations of this string can't be a palindrome")
					return
				is_odd = True
		print ("The string's permutation is a palindrome")

p= palindrome()
p.check_for_permutation_palindrome()
