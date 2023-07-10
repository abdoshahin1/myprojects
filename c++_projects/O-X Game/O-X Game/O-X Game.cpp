#include <iostream>
#include <vector>
#include <string>
#include <thread>
#include <string.h>
using namespace std;
string show[3][3] =
{
	{"1","2","3"},
	{"4","5","6"},
	{"7","8","9"}
};
void start();
void play();
void shape();
bool check_win();
int main()
{
	start();
	short option = 0;
	cout << "Enter the option: ";
	cin >> option;
	switch (option)
	{
		case 1:play(); break;
		case 2: break;
	}
	return 0;
}
bool check_win()
{
	for(int row = 0 ; row < 3 ; row++)
	{
		if (show[row][0] == show[row][1] && show[row][0] == show[row][2])
			return true;
	}
	for (int col = 0; col < 3; col++)
	{
		if (show[0][col] == show[1][col] && show[0][col] == show[2][col])
			return true;
	}
	if (show[0][2] == show[1][1] && show[0][2] == show[2][0] || show[0][0] == show[1][1] && show[0][0] == show[2][2])
		return true;
	return false;
}
void start()
{
	cout << "\t" << "======================================================\n";
	cout << "\t\t\t" << "1- Start The Game.\n";
	cout << "\t\t\t" << "2- Exit.\n";
	cout << "\t" << "======================================================\n";
}
void play()
{
	system("cls");
	string name1;
	string player = "x";
	cout << "Enter your player: ";
	cin.ignore();
	getline(cin, name1);
	cout << name1 << " choose your player (x,o): ";
	cin >> player;
	cout << "Hi ," << name1 << " you will play first \nyour player is " << player << endl;
	this_thread::sleep_for(chrono::milliseconds(1500));
	do {
		system("cls");
		shape();
		short position;
		cout << name1 << " is playing..." << endl;
		cout << "Enter your position (1:9) : ";
		cin >> position;
		switch(position)
		{
		case 1: show[0][0] = player;  shape(); break;
		case 2: show[0][1] = player;  shape(); break;
		case 3: show[0][2] = player;  shape(); break;
		case 4: show[1][0] = player;  shape(); break;
		case 5: show[1][1] = player;  shape(); break;
		case 6: show[1][2] = player;  shape(); break;
		case 7: show[2][0] = player;  shape(); break;
		case 8: show[2][1] = player;  shape(); break;
		case 9: show[2][2] = player;  shape(); break;
		}
		if (player == "x")
			player = "o";
		else
			player = "x";
	} while (check_win() != true );
	if (check_win() == true)
	{
		if (player == "x")
			player = "o";
		else
			player = "x";
		cout << "the winer is: " << player;
	}else
		cout << "Draw.";
}
void shape()
{
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			cout << show[i][j] << " # ";
		}
		cout << endl;
	}
}