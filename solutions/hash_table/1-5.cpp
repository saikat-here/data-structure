/*
Problem Number 1.5
Problem : Given two strings, write an algo to check if they are one edit (insert, remove, replace) away.
*/

#include <iostream>
#include <streambuf>
using namespace std;

class MyString
{
	public:
				void checkInsert(string s1, string s2)
				{
					int index1 = 0, index2 = 0;

					while (index1 < s1.size() && index2 < s2.size())
					{

						if ((index2 - index1) > 1)
						{
							cout << "\nInsert False";
							return;
						}

						if (s1[index1] != s2[index2])
						{
							index2++;
							continue;
						}


						index1++;
						index2++;
					}

					cout << "\nInsert True";
				}

				void checkReplace(string s1, string s2)
				{
					bool is_replaced = false;

					for (int i = 0; i < s1.size(); i++)
					{
						if (s1[i] != s2[i])
						{
							if (is_replaced)
							{
								cout << "\nReplaced False";
								return;
							}
							is_replaced = true;
						}
					}
					cout << "\nReplaced True";
				}

				void checkRemove(string s1, string s2)
				{
					int index1 = 0, index2 = 0;

					while (index1 < s1.size() && index2 < s2.size())
					{
						if ((index1 - index2) > 1)
						{
							cout << "\nRemove False";
							return;
						}

						if (s1[index1] != s2[index2])
						{
							index1++;
							continue;
						}
						index1++;
						index2++;

					}

					cout << "Remove True";
				}
};


int main()
{
	string s1, s2;
	cout << "\nPlease enter enter the first string : ";
	cin >> s1;

	cout << "Please enter the second string : ";
	cin >> s2;

	MyString MS;

	// If replaced
	if (s1.size() == s2.size())
		MS.checkReplace(s1, s2);
	// If inserted
	else if ((s1.size() + 1) == s2.size())
		MS.checkInsert(s1, s2);
	// If removed
	else if (s1.size() == (s2.size() + 1))
		MS.checkRemove(s1, s2);
	else
		cout << "\nFalse";
}
