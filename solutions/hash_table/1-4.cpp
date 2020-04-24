/*
Problem Number 1.4
Problem : Given a string, write an alogorithm to check if it is a permutation of palindrome.A permutation is a rearrangement of letters.The palindromedoes not need to be a dictionary words.

Logic : Count the occurrence of the chars of the string.The count should be even other than one char(uptoo 1 char can be odd)
*/

#include <iostream>
#include <string>

using namespace std;

class palindrome
{
	public:
	void checkPermutationPalindrome()
	{
		cout << "\nPlease enter the string : ";
		string s;
		cin >> s;
		int countChar[128] = { 0 };
		for (int i = 0; i < s.size(); i++)
		{
			countChar[int(s[i])] = countChar[int(s[i])] + 1;
		}

		bool is_odd = false; 

		for (int i = 0; i < 128; i++)
		{
			if (countChar[i] % 2 == 1)
			{
				if (is_odd == true)
				{
					cout << "\nPermutations of this string can't be a palindrome";
					return;
				}
				is_odd = true;
			}
		}
		cout << "\nThe string's permutation is a palindrome";
	}
};

int main()
{
	palindrome p;
	p.checkPermutationPalindrome();
}
