#pragma once
#include <vector>
#include <algorithm>
#include <fstream>
#include "dom.h"
using namespace std;

class Repo {
private:
	vector<Produs> produse;
	string filename;
public:
	Repo(const string& filen) :filename{ filen }{
		load_from_file();
		sortp();
	}

	//Metoda care returneaza repository-ul
	//Postconditii: vector cu produsele din repo
	const vector<Produs>& get_repo() const {
		return produse;
	}

	//Metoda care adauga produs in repo
	//Preconditii: p produs VALID
	//Postconditii: p adaugat in repo
	void addp(const Produs& prod);

	//Metoda incarca din fisier toate produsele
	//Preconditii: nume de fisier valid/existent
	//Postconditii: Produsele din fisier incarcate in repo
	void load_from_file();

	//Metoda incarca in fisier toate produsele
	//Postconditii: Produsele din repo incarcate in fisier
	void store_to_file();

	//Metoda sorteaza produsele din repo dupa pretul produselor
	//Postconditii:: repo sortat dupa pretul produselor
	void sortp();
};