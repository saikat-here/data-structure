/*
Problem Number 1.2
Problem : Givem two string, decide if one is a permutation of the other one.
*/

#include <iostream>
#include <string>

using namespace std;

class permutation
{
	string s1, s2;
	int HashForS1[128] = { 0 };
	int HashForS2[128] = { 0 };

	public: 
	void checkPermutation()
	{
		cout << "\nPlease enter the first string : ";
		getline(std::cin, s1);

		cout << "\nPlease enter the second string : ";
		getline(std::cin, s2);

		if (s1.size() != s2.size())
		{
			cout << "\nNot permutation to each other";
			return;
		}

		for (int i = 0; i <s1.size(); i++)
		{
			HashForS1[(int(s1[i]))] = HashForS1[(int(s1[i]))] + 1;
		}
		 
		for (int i = 0; i < s2.size(); i++)
		{
			HashForS2[(int(s2[i]))] = HashForS2[(int(s2[i]))] + 1;
		}
	 
		for (int i = 0; i < 128 ; i++)
		{
			if (HashForS1[i] != HashForS2[i])
			{
				cout << "\nNot permutation to each other";
				return;
			}
		}
		cout << "Permutation to each other";
	}
};

int  main()
{
	permutation permutation_obj;
	permutation_obj.checkPermutation();
	
}
