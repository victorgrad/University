#pragma once
#include "repo.h"
using namespace std;

class Observer {
public:
	virtual void update() = 0;
};

class Observable {
private:
	vector<Observer*> observers;
public:
	//Metoda apelata din Observer pentru a se adauga la lista obiectului observable
	void add_obs(Observer* obs) {
		observers.push_back(obs);
	}
	//Metoda apelata din Observer pentru a se sterge din lista obiectului observable
	void del_obs(Observer* obs) {
		observers.erase(remove(begin(observers), end(observers), obs), observers.end());
	}
protected:
	//Functie care apeleaza update() pentru fiecare observer
	void notify() {
		for (auto obs : observers)
			obs->update();
	}
};

class Validator {
public:
	Validator() = default;

	//Metoda primeste un produs si returneaza  o lista cu posibile erori
	//Preconditii: p - produs
	//postconditii: string cu erorile aparute
	string valideaza(const Produs& p);
};

class Service:public Observable {
public:
	Service(Repo& repo,Validator& val):repo{repo},val{val}{}

	//Metoda primeste datele, le valideaza, creeaza obiectul si apeleaza functia de adaugare din repo
	//Preconditii: id,nume,tip,pret - string
	//Postconditii: produsul cu acele nume adaugate
	//arunca un string cu erorile daca este cazul
	void addp(const string& id, const string& nume, const string& tip, const string& pret);

	//Metoda care returneaza repository-ul
	//Postconditii: vector cu produsele din repo
	const vector<Produs>& get_repo() {
		return repo.get_repo();
	}

private:
	Repo& repo;
	Validator& val;
};