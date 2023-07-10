#include<iostream>
#include "all_books.h"
using namespace std;
void all_books::type_book()
{
	system("cls");
	cout << "===========================================\n";
	for (int i = 0; i < type.size(); i++)
		cout << i + 1 << "- " << type.at(i) << endl;
	cout << "===========================================\n";
}
void all_books::number_of_books()
{
	cout << number_book;
}
void all_books::number_of_book_sold()
{
}
void all_books::total_money()
{
}