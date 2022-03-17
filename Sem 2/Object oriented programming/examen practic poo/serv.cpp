#include "serv.h"


void Service::addp(const string& id, const string& nume, const string& tip, const string& pret) {
	int idi = atoi(id.c_str());
	double pretd = atof(pret.c_str());
	Produs p{ idi,nume,tip,pretd };
	string err;
	err = val.valideaza(p);
	for (auto p : repo.get_repo()) {
		if (idi == p.get_id())
			err += "Id existent\n";
	}
	if (err == "") {
		repo.addp(p);
		notify();
	}
	else
		throw(err);
}

string Validator::valideaza(const Produs& p) {
	string err;
	if (p.get_nume() == "")
		err += "Numele nu poate fi vid\n";
	if (p.get_pret() < 1 || p.get_pret() > 100)
		err += "Pretul trebuie sa fie in intervalul 1-100\n";
	return err;
}