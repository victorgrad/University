#include "Iterator.h"
#include "LO.h"

#include <iostream>
using namespace std;

#include <exception>

int LO::aloca() {
	int i;
	i = primLiber;
	primLiber = urm[primLiber];
	return i;
}

void LO::dealoca(int i) {
	urm[i] = primLiber;
	primLiber = i;
	e[primLiber] = NULL_TELEMENT;
}

void LO::initSpatiuLiber(int cp) {
	for (int i = 0; i < cp; i++) {
		urm[i] = i + 1;
		e[i] = NULL_TELEMENT;
	}
	urm[cp - 1] = -1;
	primLiber = 0;
}

void LO::reinitSpatiuLiber(int cpv) {
	int i = primLiber;
	//cautam ultimul el liber si ii punem urm sa fie cp veche
	for (int i = cpv; i < cp; i++) {
		urm[i] = i + 1;
		e[i] = NULL_TELEMENT;
	}
	urm[cp - 1] = -1;
	primLiber = cpv;
}

void LO::redim() {
	cp *= 2;
	TElement* newe = new TElement[cp];
	int* newurm = new int[cp];
	int* newprec = new int[cp];
	for (int i = 0; i < cp; i++) {
		newe[i] = e[i];
		newurm[i] = urm[i];
		newprec[i] = prec[i];
	}

	delete[] e;
	delete[] urm;
	delete[] prec;
	e = newe;
	urm = newurm;
	prec = newprec;
}

int LO::creeazaNod(TElement el) {
	if (primLiber == -1) {
		redim();
		reinitSpatiuLiber(cp/2);
	}
	int i = aloca();
	e[i] = el;
	urm[i] = -1;
	prec[i] = -1;
	return i;
}



LO::LO(Relatie rel) {
	/* de adaugat */
	r = rel;
	e = new TElement[1];
	urm = new int[1];
	prec = new int[1];
	e[0] = NULL_TELEMENT;
	urm[0] = -1;
	prec[0] = -1;
	cp = 1;
	prim = -1;
	ultim = -1;
	primLiber = 0;
	lg = 0;
	nrelem = 0;
}

// returnare dimensiune
int LO::dim() const {
	return nrelem;
	//return 0;
}

// verifica daca LO e vida
bool LO::vida() const {
	if(prim==-1)
		return true;
	return false;
}

// returnare element
//arunca exceptie daca i nu e valid
TElement LO::element(int piz) const{
	/* de adaugat */
	if (piz < 0 or piz >= nrelem)//or e[i]== NULL_TELEMENT)
		throw(exception());
	int poz = prim;
	int incr = 0;
	while (incr < piz) {
		poz = urm[poz];
		incr++;
	}
	int i = poz;
	return e[i];
}

// sterge element de pe o pozitie i si returneaza elementul sters
//arunca exceptie daca i nu e valid
TElement LO::sterge(int piz) {
	if (piz < 0 or piz >= nrelem )//or e[i]== NULL_TELEMENT)
		throw(exception());
	int poz = prim;
	int incr = 0;
	while (incr < piz) {
		poz = urm[poz];
		incr++;
	}
	int i = poz;
	TElement el = e[i];
	if (i == prim) {
		//daca nu era singurul element
		if (urm[i] != -1) {
			prim = urm[i];
			prec[prim] = -1;
		}//daca era singurul elem
		else {
			prim = -1;
		}
	}
	else {
		//daca nu e primul
		if (urm[i] != -1) {
			//daca nu e ultimul
			int precedent, urmator;
			precedent = prec[i];
			urmator = urm[i];
			urm[precedent] = urmator;
			prec[urmator] = precedent;
			//urm[prec[i]] = urm[i];
			//prec[urm[i]] = prec[i];
		}
		else { //daca e ultimul
			ultim = prec[i];
			urm[prec[i]] = -1;
		}
	}
	dealoca(i);
	nrelem--;
	return el;
}

// cauta element si returneaza prima pozitie pe care apare (sau -1)
int LO::cauta(TElement el) const {
	//	ADD COND DE STOP
	int poz = prim;
	int incr = 0;
	while (poz != -1) {
		if (e[poz] == el)
			return incr;
		poz = urm[poz];
		incr++;
	}
	return -1;
}

// adaugare element in LO
void LO::adauga(TElement el) {
	int nou = creeazaNod(el);
	//l-am adaugat, trebuie sa ne ocupam de vectorul urm si prec
	if (vida()) {
		//daca e singurul element
		prim = nou;
	}
	else if (r(e[nou], e[prim])) {
		//daca vine inaintea primului
		prec[prim] = nou;
		urm[nou] = prim;
		prim = nou;
	}
	else {
		//trebuie sa gasim unde sa il inseram
		int poz = prim;
		while (r(e[poz], e[nou]) and urm[poz] != -1) {
			poz = urm[poz];
		}
		//avem 2 cazuri, ori s-a ajuns la finalul listei si trebuie pus la final 
		//ori nu indeplineste relatia cu ultimul el(trebuie sa il inlocuiasca)
		if (r(e[poz], e[nou]) and urm[poz] == -1) {
			//daca indeplineste relatia cu ultimul el trebuie pus la final
			urm[poz] = nou;
			prec[nou] = poz;
			ultim = nou;
		}
		else {
			//altfel trebuie doar inserat pe pozitia poz

			prec[nou] = prec[poz];
			urm[nou] = poz;
			urm[prec[poz]] = nou;
			prec[poz] = nou;
		}
	}
	nrelem++;
}

// returnare iterator
Iterator LO::iterator(){
	return Iterator(*this);
}


//destructor
LO::~LO() {
	/* de adaugat */
	delete[] e;
	delete[] urm;
	delete[] prec;
	cp = 0;
	prim = -1;
	primLiber = -1;
	lg = -1;
	nrelem = -1;
}

void LO::afisare() {
	std::cout << "\np: ";
	int poz = prim;
	while (poz != -1) {
		cout << poz << ' ';
		poz = urm[poz];
	}
	cout << "\ne: ";
	poz = prim;
	while (poz != -1) {
		cout << e[poz] << ' ';
		poz = urm[poz];
	}
	cout << "\nu: ";
	poz = prim;
	while (poz != -1) {
		cout << urm[poz] << ' ';
		poz = urm[poz];
	}
	cout << "\np: ";
	poz = prim;
	while (poz != -1) {
		cout << prec[poz] << ' ';
		poz = urm[poz];
	}
}
