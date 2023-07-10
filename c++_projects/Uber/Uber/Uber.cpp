#include <iostream>
#include <string.h>
#include <string>
#include <random>
#include <chrono>
#include <thread>
using namespace std;
class uber {
private:
	string nema;
	string account;
	int pass;
	int confirm_pass;
public:
	void set_name() {
		cout << "enter your name: ";
		cin >> nema;
	}
	void set_account(){ 
		cout << "enter the account: ";
		cin >> account;
	}
	void set_pass() {
		do {
			cout << "enter the password: ";
			cin >> pass;
			try {
				if (pass <= 0) throw "please enter only positive number.";
			}
			catch (const char* message){
				cout << message << endl;
			}
		} while (pass <= 0);
	}
	void set_conferm_pass() {
		do {
			cout << "enter the conferm password: ";
			cin >> confirm_pass;
			try {
				if (confirm_pass != pass) throw "please enter the same password.";
			}
			catch (const char* message) {
				cout << message << endl;
			}
		} while (confirm_pass != pass);
	}
};
bool research(string name[], int size, string nam) {
	bool research = false;
	for (int i = 0; i < size; i++) {
		if (nam == name[i]) {
			research = true;
		}
	}
	return research;
}
bool research2(int name[], int size, int nam) {
	bool research = false;
	for (int j = 0; j < size; j++) {
		if (nam == name[j]) {
			research = true;
		}
	}
	return research;
}
bool found(string array[], int size, string name) {
	bool search = false;
	for (int i = 0; i < size; i++){
		if (name == array[i]){
			search = true;
			break;
		}
		else{
			search = false;
		}
	}
	return search;
}
bool search2(string array[], int size, string name, bool search){
	for (int j = 0; j < size; j++) {
		if (name == array[j] && search == true){
			search = true;
			break;
		}
		else{
			search = false;
		}
	}
	return search2;
}
void  number_car(string name1, string name2, bool test){
	if (name1 == "cairo" && name2 == "el-geza" || name1 == "el-geza" && name2 == "cairo" || name1=="cairo" && name2=="el-monofya" || name1=="el-monofya" && name2=="cairo" || name1=="cairo"&& name2=="sohag" || name1=="sohag" && name2 == "cairo" || name1=="cairo"&&name2=="el-apoor" || name1=="el-apoor"&&name2=="cairo" ||name1=="cairo"&&name2=="el-shekh-zayed"||name1=="el-shekh-zayed"&&name2=="cairo"||name1=="cairo"&&name2=="shpen-el-com"||name1=="shpen-el-com"&&name2=="cairo"||name1=="cairo"&&name2=="aswan"||name1=="aswan"&&name2=="cairo"){
		cout << rand()%30 << endl;
	}
}
void menu() {
	cout << "########################################### Welcom to the Uber application #############################################" << endl;
	cout << "\t\t\t\t\t\t" << "1- " << "create a new account." << endl;
	cout << "\t\t\t\t\t\t" << "2- " << "log in with your account." << endl;
	cout << "\t\t\t\t\t\t" << "3- " << "exit." << endl;
	cout << "########################################################################################################################" << endl;
}
void log() {
	int pass;
	int test[1];
	string account;
	string test1[1];
do {
		cout << "enter your account: ";
		cin >> account;
		test1[0] = account;
		try {
			if (research(test1, 1, account) == false) throw "please enter the correct account.";
		}
		catch (const char* message) {
			cout << message << endl;
		}
	} while (research(test1, 1, account) == false);
	cout << "enter the password: ";
	cin >> pass;
	test[0] = pass;
	do {
		try {
			if (research2(test, 1,pass) == false) throw "please enter the correct password.";
		}
		catch (const char* message) {
			cout << message << endl;
		}
	} while ((research2(test, 1, pass) == false));
}
void choose() {
	cout << "=================================\n";
	cout << "1- " << "the menu.\n";
	cout << "2- " << "start to travel.\n";
	cout << "3- " << "back.\n";
	cout << "=================================\n";
}
void detials() {
	string place[8] = { "cairo","el-geza","el-monofya","sohag","el-shekh-zayed","el-apoor","shpen-el-com","aswan" };
	string first_place, second_place;
	cout << "=================================\n";
	cout << "where will you go ?" << endl;
	cout << "enter the first place: ";
	cin >> first_place;
	cout << "enter the second place: ";
	cin >> second_place;
	number_car(first_place, second_place, search2(place, 8, second_place, found(place, 8, first_place)));
	cout << "=================================\n";
}
int main(){
	uber accout;
	int option;
	do {
		system("cls");
		menu();
		cout << "option: ";
		cin >> option;
		switch (option){
		case 1:{
				system("cls");
				accout.set_name();
				accout.set_account();
				accout.set_pass();
				accout.set_conferm_pass();
			
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
				cout << "your account is ready.";
				this_thread::sleep_for(chrono::milliseconds(1100));
				goto choose;
		}
		case 2:{
			this_thread::sleep_for(chrono::milliseconds(50));
			system("cls");
			log();
			int option;
		choose:
			system("cls");
			choose();
			do {
				cout << "option: ";
				cin >> option;
				if (option == 1){
					system("cls");
					choose();
				}
				else if (option == 2){
					detials();
				}
			} while (option != 3);
			break;
		}
		case 3:break;
		}
	} while (option != 3);
	return 0;
}