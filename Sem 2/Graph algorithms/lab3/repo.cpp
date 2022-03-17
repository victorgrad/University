#include "repo.h"

void Repository::loadFromFile() {
	std::ifstream in(filename);
	if (!in.is_open()) {
		throw(std::exception());
	}
	while (!in.eof()) {
		float buget_alocat, buget_estimat;
		std::string nume, tip;
		in >> nume;
		if (in.eof()) break;
		in >> tip;
		if (in.eof()) break;
		in >> buget_alocat;
		in >> buget_estimat;
		Proiect pr{ nume,tip,buget_alocat,buget_estimat };
		proiecte.push_back(pr);
	}
	in.close();
}

std::vector<Proiect>& Repository::get_all() {
	return proiecte;
}