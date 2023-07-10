#include <iostream>
#include "all_books.h"
#include "history.h"
using namespace std;
int main()
{
	all_books shop;
	history books;
	int password = 12345;
	int pass;
	int op;
again:
	cout << "enter the password to show the details of your bookshop: ";
	cin >> pass;
	if (pass == password)
	{
		system("cls");
		cout << "===========================================\n";
		cout << "1- type of books\n" << "2- number of books\n" << "3- number of book already sold\n" << "4- total money\n" << "5- exit\n";
		cout << "===========================================\n";
		cout << "enter your option : ";
		cin >> op;
	}else{
		cout << "please enter the correct password." << endl;
		goto again;
	}
	switch (op)
	{
	case 1: shop.type_book(); break;
	case 2: shop.number_of_books(); break;
	case 3: shop.number_of_book_sold(); break;
	case 4: shop.total_money(); break;
	case 5: break;
	}
	return 0;
}