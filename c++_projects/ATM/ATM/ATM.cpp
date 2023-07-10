#include <iostream>
#include <string.h>
#include <string>
#include <random>
#include <chrono>
#include <thread>
#include <functional>
using namespace std;

struct found
{
	string name;
	string address;
	string account;
	int age;
	int pass;
	int con_pass;
	int recieved;
};
bool set_the_name(string arry[], int size, string m)
{
	bool found = false;
	for (int i = 0; i < size; i++)
	{
		if (arry[i] == m)
		{
			found = true;
		}
	}
	return found;
}
bool set_num(int array[], int size, int rig)
{
	bool found = false;
	for (int i = 0; i < size; i++)
	{
		if (array[i] == rig)
		{
			found = true;
		}
	}
	return found;
}
class New_Account
{
private:
 	string the_name[3];
	int num[3];
	found array;
public:
	void set_fun()
	{
		void set_name();
		{
			cout << "enter your name: ";
			cin >> array.name;
			the_name[0] = array.name;
		}

		void set_age();
		{
			do {
				cout << "enter your age: ";
				cin >> array.age;
				num[0] = array.age;
				try
				{
					if (array.age < 0)
					{
						throw "please,enter a positive number";
					}
				}
				catch (const char* message)
				{
					cout << message << endl;
				}
			} while (array.age < 0);

		}
		void set_address();
		{
			cout << "enter your address: ";
			cin >> array.address;
			the_name[1] = array.address;
		}

		void set_account();
		{
			cout << "enter new account: ";
			cin.ignore();
			getline(cin, array.account);
			the_name[2] = array.account;
		}

		void set_password();
		{
			do {
				cout << "enter password: ";
				cin >> array.pass;
				num[1] = array.pass;
				try
				{
					if (array.pass < 0)
					{
						throw "please,enter a positive number";
					}
				}
				catch (const char* message)
				{
					cout << message << endl;
				}
			} while (array.pass < 0);
		}
		void set_con_pass();
		{
			do {
				cout << "enter confirm the password: ";
				cin >> array.con_pass;
				num[2] = array.con_pass;
				try
				{
					if (array.con_pass == array.pass)
					{
						cout << "loading";
						this_thread::sleep_for(chrono::milliseconds(500));
						cout << ".";
						this_thread::sleep_for(chrono::milliseconds(500));
						cout << ".";
						this_thread::sleep_for(chrono::milliseconds(500));
						cout << ".";
						this_thread::sleep_for(chrono::milliseconds(500));
						cout << ".";
						this_thread::sleep_for(chrono::milliseconds(500));
						cout << ".";
						this_thread::sleep_for(chrono::milliseconds(500));
						cout << ".";
						this_thread::sleep_for(chrono::milliseconds(500));
						cout << "\b\b\b\b\b\b\b\b\b\b\b\b\b";
						this_thread::sleep_for(chrono::milliseconds(200));
						cout << "";
						this_thread::sleep_for(chrono::milliseconds(200));
						cout << "loading";
						this_thread::sleep_for(chrono::milliseconds(700));
						cout << ".";
						this_thread::sleep_for(chrono::milliseconds(500));
						cout << ".";
						this_thread::sleep_for(chrono::milliseconds(500));
						cout << ".";
						this_thread::sleep_for(chrono::milliseconds(500));
						cout << ".";
						this_thread::sleep_for(chrono::seconds(1));
						cout << ".";
						this_thread::sleep_for(chrono::milliseconds(500));
						cout << "." << endl;
						this_thread::sleep_for(chrono::milliseconds(1100));
						cout << "your account is ready.\n";
						this_thread::sleep_for(chrono::milliseconds(1100));
					}
					else
					{
						throw "please enter the same password.";
					}
				}
				catch (const char* message)
				{
					cout << message << endl;
				}
			} while (array.con_pass != array.pass);
		}
	}
	void log()
	{
		do
		{
			do
			{
				cout << "enter your account: ";
				cin.ignore();
				getline(cin, array.account);
				if (set_the_name(the_name, 3, array.account) == false)
				{
					cout << "enter a correct account." << endl;
				}
			} while (set_the_name(the_name, 3, array.account) != true);
			do
			{
				cout << "enter your password: ";
				cin >> array.pass;
				if (set_num(num, 3, array.pass) == false)
				{
					cout << "enter a correct password." << endl;
				}
				try
				{
					if (array.pass < 0)
					{
						throw "please enter the correct password.";
					}
				}
				catch (const char* message)
				{
					cout << message << endl;
				}
			} while (set_num(num, 3, array.pass) != true);
		} while (array.pass < 0);
	}

	void set_recieved(int money)
	{
		array.recieved = money;
	}

	void get_recieved()
	{
		cout << "####################" << endl;
		cout << "the recieved money is: " << array.recieved << " $" << endl;
		cout << "####################" << endl;
	}

};
void menu()
{
	cout << "####################" << endl;
	cout << "1- " << "Create an account." << endl;
	cout << "2- " << "log in to your account." << endl;
	cout << "3- " << "exit." << endl;
	cout << "####################" << endl;
}
void bransh_menu()
{
	cout << "####################" << endl;
	cout << "1- " << "menu." << endl;
	cout << "2- " << "deposit." << endl;
	cout << "3- " << "withdraw." << endl;
	cout << "4- " << "transifar money from account to account." << endl;
	cout << "5- " << "the money that racieved." << endl;
	cout << "6- " << "total money." << endl;
	cout << "7- " << "back." << endl;
	cout << "####################" << endl;
}

int main()
{
	New_Account account;
	int option;
	double withdraw = 0;
	double total_money = 0;
	double deposit = 0;
	do {
	menu:
		system("cls");
		menu();
		cout << "option: ";
		cin >> option;
		switch (option)
		{
		case 1:
		{
			system("cls");
			do
			{
				int option;
				system("cls");
				account.set_fun();
				cout << "####################" << endl;
				cout << "1- " << "enter your account." << endl;
				cout << "2- " << "back." << endl;
				cout << "####################" << endl;
				cout << "option: ";
				cin >> option;
				if (option == 1)
				{
					goto branch;
				}
				else if (option == 2)
				{
					goto menu;
				}
			} while (option != 2);
		}
		case 2:
		{
		branch:
			system("cls");
			account.log();
			system("cls");
			bransh_menu();
			int option;
			int money = 0;
			do
			{
				cout << "option: ";
				cin >> option;
				if (option == 1)
				{
					system("cls");
					bransh_menu();
				}
				else if (option == 2)
				{
					cout << "####################" << endl;
					cout << "enter the money: ";
					cin >> deposit;
					cout << "####################" << endl;
					total_money += deposit;
				}
				else if (option == 3)
				{
					do
					{
						try
						{
							cout << "####################" << endl;
							cout << "enter the money: ";
							cin >> withdraw;
							cout << "####################" << endl;
							if (withdraw <= total_money)
							{
								total_money = total_money - withdraw;
								break;
							}
							else
							{
								throw "please, enter money again.";
							}
						}
						catch (const char* message)
						{
							cout << message << endl;
						}
					} while (withdraw > total_money);
				}
				else if (option == 4)
				{
					string account1;
					string account2;
					int money1;
					int money2 = 0;
					cout << "####################" << endl;
					cout << "enter the first account(send): ";
					cin >> account1;
					cout << "enter the second account(receive): ";
					cin >> account2;
					cout << "enter the money: ";
					cin >> money1;
					money2 += money1;
					money += money2;
					total_money += money2;
					cout << "loading";
					this_thread::sleep_for(chrono::milliseconds(500));
					cout << ".";
					this_thread::sleep_for(chrono::milliseconds(500));
					cout << ".";
					this_thread::sleep_for(chrono::milliseconds(500));
					cout << ".";
					this_thread::sleep_for(chrono::milliseconds(500));
					cout << ".";
					this_thread::sleep_for(chrono::milliseconds(500));
					cout << ".";
					this_thread::sleep_for(chrono::milliseconds(500));
					cout << ".";
					this_thread::sleep_for(chrono::milliseconds(500));
					cout << "\b\b\b\b\b\b\b\b\b\b\b\b\b";
					this_thread::sleep_for(chrono::milliseconds(200));
					cout << "little time left";
					this_thread::sleep_for(chrono::milliseconds(700));
					cout << ".";
					this_thread::sleep_for(chrono::milliseconds(500));
					cout << ".";
					this_thread::sleep_for(chrono::milliseconds(500));
					cout << ".";
					this_thread::sleep_for(chrono::milliseconds(500));
					cout << ".";
					this_thread::sleep_for(chrono::seconds(1));
					cout << ".";
					this_thread::sleep_for(chrono::milliseconds(500));
					cout << "." << endl;
					this_thread::sleep_for(chrono::milliseconds(1100));
					cout << "the money is transiferd."<<endl;
					this_thread::sleep_for(chrono::milliseconds(1100));
					cout << "####################" << endl;
				}
				else if (option == 5)
				{
					account.set_recieved(money);
					account.get_recieved();
				}
				else if (option == 6)
				{
					cout << "####################" << endl;
					cout << "the total money is : " << total_money << "  $" << endl;
					cout << "####################" << endl;
				}
				else if (option == 7)
				{
					break;
				}
			} while (option != 7);
		}
		case 3: break;
		}
	} while (option != 3);
	return 0;
}