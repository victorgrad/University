#include "repo.h"

void Repo::addp(const Produs& prod) {
	produse.push_back(prod);
	sortp();
	store_to_file();
}

void Repo::load_from_file() {
	ifstream in(filename);
	if (!in.is_open()) {
		throw(string{ "Eroare la deschidere fisier" });
	}
	while (!in.eof()) {
		int id;
		double pret;
		string nume, tip;
		in >> id;
		in.get();
		in >> nume;
		if (in.eof()) break;
		in >> tip;
		if (in.eof()) break;
		in >> pret;
		Produs prod{ id,nume,tip,pret };
		addp(prod);
	}
	in.close();
}

void Repo::store_to_file() {
	ofstream out(filename,ofstream::trunc);
	if (!out.is_open()) {
		throw(string{ "Eroare la deschidere fisier" });
	}
	for (auto& prod : produse) {
		out << prod.get_id() << "\n";
		out << prod.get_nume() << "\n";
		out << prod.get_tip() << "\n";
		out << prod.get_pret() << "\n";
	}
	out.close();
}

void Repo::sortp() {
	sort(produse.begin(), produse.end(), [](const Produs& p1, const Produs& p2) {
		return p1.get_pret() < p2.get_pret();
		});
}