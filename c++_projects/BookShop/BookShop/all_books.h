#pragma once
#include <string>
#include <vector>
using namespace std;
class all_books
{
private:
	int number_book = 1000;
	int total = 0;
	int book_already_sold = 0;
	vector <string> type = { "History","Romantec","Comedy","Super Heros","Manga","Fiction","action","Mystery and crime" };
public:
	void type_book();
	void number_of_books();
	void number_of_book_sold();
	void total_money();
};