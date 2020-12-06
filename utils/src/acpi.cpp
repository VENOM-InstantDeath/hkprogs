#include <iostream>
#include <fstream>
using namespace std;

//Reemplazo de ACPI
//Escrita por Darth Venom
//< = >

int main() {
	ifstream File;
	string X;
	File.open("/sys/class/power_supply/BAT0/capacity");
	getline(File, X);
	File.close();
	cout << X << "%, ";
	File.open("/sys/class/power_supply/BAT0/status");
	getline(File, X);
	cout << X << endl;
	File.close();
	return 0;
}
