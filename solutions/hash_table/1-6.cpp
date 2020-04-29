/*
Problem Number 1.6
Problem : Implement a method to perform basic string compression using the counts of repeated characters. 
String aabcccccaaa would became a2b1c5a3. If the compressed string would not became smaller than the original string then it should return the original string.
You can assume the string has only uppercase and lower case letters.
*/

#include <iostream>
#include <string>
using namespace std;

class StringCompress
{
	public:
		void compress(string s1)
		{
			int count = 0, StringLength = 0;
			string compressedString, tempString;

			for (int i = 0; i < s1.size(); i++)
			{
				count++;
				tempString = s1[i];

				if (s1[i] != s1[i + 1])
				{
					compressedString = compressedString + tempString + to_string(count);
					count = 0;
					tempString = "";
					StringLength = StringLength + 2;

				}

				 
				if (compressedString.size() > s1.size())
				{
					cout << "\nString : "+ s1;
					return;
				}
				 
			}

			cout << "\nString : "+compressedString;
		}
};


int main()
{
	string s1;

	cout << "\nPlease enter the string to compress : ";
	cin >> s1;

	StringCompress SC;

	SC.compress(s1);

}
