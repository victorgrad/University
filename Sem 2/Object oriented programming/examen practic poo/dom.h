#pragma once
#include <string>
using namespace std;
class Produs {
private:
	int id;
	double pret;
	string nume, tip;
public:
	Produs(const int& id,const string& nume, const string& tip,const double& pret ):id{id},nume{nume},tip{tip},pret{pret}{}
	
	//Metoda retureneaza id-ul produsului
	//Postconditii: id-ul(int) produsului
	const int get_id() const {
		return id;
	}

	//Metoda retureneaza numele produsului
	//Postconditii: numele(string) produsului
	const string get_nume() const {
		return nume;
	}

	//Metoda retureneaza tipul produsului
	//Postconditii: tipul(string) produsului
	const string get_tip() const {
		return tip;
	}

	//Metoda retureneaza pretul produsului
	//Postconditii: pretul(double) produsului
	const double get_pret() const {
		return pret;
	}

	~Produs() = default;
};