"""
Problem Number 1.6
Problem : Implement a method to perform basic string compression using the counts of repeated characters. 
String aabcccccaaa would became a2b1c5a3. If the compressed string would not became smaller than the original string then it should return the original string.
You can assume the string has only uppercase and lower case letters.
"""

class CompressString(object):
	
	def compress_string (self,s):
		
		count = 0
		temp_string = ""
		compressed_string= ""
		
		for i in range (len(s)):
			count+=1
			temp_string = s[i]

			if ( (i+1) == len(s)) or ( s[i] != s[i+1]) :
				compressed_string = compressed_string + temp_string + str(count)
				count = 0
				temp_string = ""
			
			if len(compressed_string) > len(s) :
				print ("String : " + s)
				return

		print ("String : " + compressed_string)
			 
print ("Please enter the string : ")
s=input()

CS = CompressString()
CS.compress_string(s)
