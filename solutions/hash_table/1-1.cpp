/*
Problem Number 1.1
Problem : Implement an algorithm to determine if a string has all unique characters.
*/

#include <iostream>
#include <string>
using namespace std;
class MyHash
{
    char hashTable[128];

public:
    MyHash()
    {
        hashTable[128] = {};
    }

private:
    int getHashValue(char c)
    {
        return int(c);
    }

public:
    void insertToHash(string s)
    {
        int hashValue;
        for (int i = 0; i < s.size(); i++)
        {
            hashValue = getHashValue(s[i]);
            if (hashTable[hashValue] != NULL)
            {
                std::cout << "\nThere are duplicate characters";
                return;
            }

            hashTable[hashValue] = s[i];
        }
        std::cout << "All character(s) are unique";
    }
};

int main()
{
    string s;
    std::cout << "\nPlease enter the ASCII string : ";
    std::cin >> s;

    //Total characters in ASCII is 128. So, If a string contains more than 128 chars then there are duplicates
    if (s.size() > 128)
    {
        std::cout << "There are duplicate characters";
        return 1;
    }

    MyHash MH;

    MH.insertToHash(s);

}
