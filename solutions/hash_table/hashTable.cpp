
#include <iostream>
using namespace std;

struct MyNode
{
	int value = NULL;
	struct MyNode* next = NULL;
};

MyNode* hashArray[20] = {};

int calculateHash(int number)
{
	return (number % 20);
};

void insert_to_hash(int number)
{
	int hashValue = calculateHash(number);

	MyNode* tmp = new MyNode;

	tmp->value = number;
	tmp->next = NULL;

	if (hashArray[hashValue] == NULL)
	{
		hashArray[hashValue] = tmp;
		return;
	}

	MyNode* thisNode = hashArray[hashValue];

	while (thisNode->next != NULL)
	{
		// Will not insert duplicate value
		if (thisNode->value == number)
			return;
		thisNode = thisNode->next;
	}
	
	// Will not insert duplicate value
	if (thisNode->value != number)
		thisNode->next = tmp;

	return;
}

void findNumber()
{
	int number;
	cout << "\nPlease enter the number to find : ";
	cin >> number;
	int hashValue = calculateHash(number);
	
	if (hashArray[hashValue] == NULL)
	{
		cout << "\nNumber NOT found";
		return;
	}
	else 
	{
		MyNode* thisNode = hashArray[hashValue];
	 
		while (thisNode != NULL)
		{
			if (thisNode->value == number)
			{
			 
				cout << "\nNumber is AVAILABLE";
				return;
			}
			 
			thisNode = thisNode->next;
		}
	}

	cout << "\nNumber NOT found";
}

void inputAndPush()
{
	int totalNumber, tempNumber;
	cout << "How many numbers you want to insert ? ";
	cin >> totalNumber;

	for (int i = 0; i < totalNumber; i++)
	{
		cout << "\n Please enter the number : ";
		cin >> tempNumber;
		insert_to_hash(tempNumber);
	}
}

void removeNumber()
{
	int numberToRemove;
	cout << "\nPlease enter the number to remove\n";
	cin >> numberToRemove;
	int hashValue = calculateHash(numberToRemove);
	MyNode* thisNode = hashArray[hashValue];

	if (thisNode->value == numberToRemove)
	{
		hashArray[hashValue] = thisNode->next;
		cout << "Removed Successfully";
		return;
	}

	MyNode* previousNode = NULL;
	while (thisNode != NULL)
	{
		if (thisNode->value == numberToRemove)
		{
			previousNode->next = thisNode->next;
			cout << "Removed Successfully";
			return;
		}
		previousNode = thisNode;
		thisNode = thisNode->next;
	}

	cout << "Number is not available";
}

void listNumbers()
{
	int location;
	cout << "\nPlease enter the location. Valid range is 0 to 19\n";
	cin >> location;

	if (hashArray[location] == NULL)
	{
		cout << "Location is empty";
		return;
	}

	MyNode* thisNode = hashArray[location];

	cout << "\n------------------";
	while (thisNode != NULL)
	{
		cout << "\n" << thisNode->value;
		thisNode = thisNode->next;
	}
	cout << "\n------------------";
	cout << "\nThat's all. \nNote : I have not saved duplicate values to save space";
}

int main()
{
	 
	inputAndPush();
	int option;
	while (true)
	{
		cout << "\nPlease selecet an option. \n1. Find a number  \n2. Insert new numbers \n3. Remove a number \n4. List all values of a location\n5. Exit\n";
		cin >> option;

		if (option == 1)
			findNumber();
		else if (option == 2)
			inputAndPush();
		else if (option == 3)
			removeNumber();
		else if (option == 4)
			listNumbers();
		else if (option == 5)
			exit(1);
		else
			cout << "Invalid option";
	}
}
