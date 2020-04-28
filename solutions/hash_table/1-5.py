"""
Problem Number 1.5
Problem : Given two strings, write an algo to check if they are one edit (insert, remove, replace) away.
"""

import array

class check_string (object):

	def check_insert(self, str1, str2):
		index1=0
		index2=0

		while (index1 < len(str1)) and (index2 < len(str2)):
			if str1[index1] != str2[index2]:
				index2+=1
				if index2 != index1 + 1:
					print ("Insert False")
					return
				continue
			index2+=1
			index1+=1

		print ("Insert True")			

	def check_replace(self, str1, str2):
		is_changed = False;
		for i in range (len(str1)):
			if str1[i] != str2[i]:
				if is_changed == True:
					print ("Replace False")
					return
				is_changed = True
		print ("Replace True")

	def check_remove(self, str1, str2):
		index1 = 0
		index2 = 0 
		while (index1 < len(str1)) and (index2 < len(str2)):
			if str1[index1] != str2[index2]:
				index1+=1
				if index1 > (index2+1) :
					print ("Remove False")
					return
				continue
			index1+=1
			index2+=1

		print("Remove True")

print ("Please enter the 1st string : ")
s1 = input()

print ("Please enter the 2nd string : ")
s2 = input()

check_string_obj = check_string()

# Its replaced if the lengths are same
if len(s1) == len(s2):
	check_string_obj.check_replace(s1,s2)

elif len(s1) == len(s2)+1:
	check_string_obj.check_remove(s1,s2)

elif len(s1)+1 == len(s2) :
	check_string_obj.check_insert(s1,s2)

else :
	print ("False")
	
