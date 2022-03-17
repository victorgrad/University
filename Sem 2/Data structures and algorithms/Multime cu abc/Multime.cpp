#include "Multime.h"
#include "IteratorMultime.h"

#include <iostream>
#include <stack>

Multime::Multime() {
	//Theta(1)
	rad = nullptr;
	dime = 0;
}


bool Multime::adauga(TElem elem) {
	/*int dim_veche = dime;
	rad = adauga_rec(rad, elem, nullptr);
	if (dim_veche != dime) {//daca am putut efectua adaugarea
		return true;
	}
	return false;
	*/
	//O(h)
	if (rad != nullptr) {
		Nod* p = rad;
		Nod* prec = nullptr;
		while (p != nullptr) {
			if (elem == p->e)
				return false;
			prec = p;
			if (elem < p->e) {
				p = p->st;
			}
			else {
				p = p->dr;
			}
		}
		p = creeazaNod(elem, prec);
		if (p->e < prec->e)
			prec->st = p;
		else
			prec->dr = p;
	}
	else {
		rad = creeazaNod(elem, nullptr);
	}
	dime++;
	return true;
}

Nod* Multime::adauga_rec(Nod* p, TElem e,Nod* prec) {
	if (p == nullptr) {
		dime++;
		return creeazaNod(e, prec);
	}
	else {
		if (e < p->e)
			p->st = adauga_rec(p->st, e, p);
		else if (e > p->e)
			p->dr = adauga_rec(p->dr, e, p);
		//daca e egal inseamna ca nu mai poate fi adaugat in multime si nu facem nimic(nu se modifica dime)
	}
	return p;
}

Nod* Multime::minim(Nod* p) const{
	//O(h)
	if (p != nullptr) {
		while (p->st != nullptr) {
			p = p->st;
		}
	}
	return p;
}

bool Multime::sterge(TElem elem) {
	/*
	int dim_veche = dime;
	rad = sterge_rec(rad, elem);
	if (dim_veche != dime) {//daca am putut efectua stergerea
		return true;
	}
	return false;
	*/
	//O(h)
	
	if (rad != nullptr) {
		if (rad->e == elem) {
			Nod* p = rad;
			if (p->dr == nullptr && p->st == nullptr) {//daca p e frunza
				delete p;
				rad = nullptr;
				dime--;
				return true;
			}
			else if (p->dr == nullptr) {//daca are in st
				rad = p->st;
				rad->parinte = nullptr;
				delete p;
				dime--;
				return true;
			}
			else if (p->st == nullptr) {//daca are in dr
				rad = p->dr;
				rad->parinte = nullptr;
				delete p;
				dime--;
				return true;
			}
			else {//daca are si in st si in dr
				Nod* repl = minim(p->dr);
				p->e = repl->e; //pun valoarea celui mai mic nod din dreapta si sterg nodul cel mai mic din dreapta (repl)
				Nod* tata = repl->parinte;
				tata->st = repl->dr;//daca e cel  mai mic inseamna ca el e in st tatalui si ca nu mai are fii in st
				if (repl->dr != nullptr) {
					repl->dr->parinte = tata;
				}
				delete p;
			}
		}
		Nod* p = rad;
		while (p != nullptr && p->e != elem) {
			if (elem < p->e)
				p = p->st;
			else
				p = p->dr;
		}
		if (p == nullptr)
			return false;
		else {
			if (p->dr == nullptr && p->st == nullptr) {//daca p e frunza
				Nod* parinte = p->parinte;
				if (p->e < parinte->e) {
					parinte->st = nullptr;
				}
				else {
					parinte->dr = nullptr;
				}
				delete p;
				dime--;
				return true;
			}
			else if (p->dr == nullptr) {//daca are in st
				Nod* parinte = p->parinte;
				if (p->e < parinte->e) {
					parinte->st = p->st;
				}
				else {
					parinte->dr = p->st;
				}
				p->st->parinte = parinte;
				delete p;
				dime--;
				return true;
			}
			else if (p->st == nullptr) {//daca are in dr
				Nod* parinte = p->parinte;
				if (p->e < parinte->e) {
					parinte->st = p->dr;
				}
				else {
					parinte->dr = p->dr;
				}
				p->dr->parinte = parinte;
				delete p;
				dime--;
				return true;
			}
			else {//daca are si in st si in dr
				Nod* repl = minim(p->dr);
				p->e = repl->e; //pun valoarea celui mai mic nod din dreapta si sterg nodul cel mai mic din dreapta (repl)
				Nod* tata=repl->parinte;
				tata->st = repl->dr;//daca e cel  mai mic inseamna ca el e in st tatalui si ca nu mai are fii in st
				if (repl->dr != nullptr) {
					repl->dr->parinte = tata;
				}
				delete p;
			}
		}
	}
	return false;
	
}

Nod* Multime::sterge_rec(Nod* p, TElem e) {
	if (p == nullptr)
		return nullptr;
	else{
		if (e < p->e) {
			p->st = sterge_rec(p->st, e);
			if(p->st!=nullptr)
				p->st->parinte = p;
		}
		else if (e > p->e) {
			p->dr = sterge_rec(p->dr, e);
			if (p->dr != nullptr)
				p->dr->parinte = p;
		}
		else {//am ajuns la nodul de sters
			if (p->st != nullptr && p->dr != nullptr) {//nodul are si subarbore stang si subarbore drept
				Nod* temp = minim(p->dr);//se ia nodul cu cheie minima dreapta
				p->e = temp->e;//se pune valoarea in p
				p->dr = sterge_rec(p->dr, p->e);//se sterge nodul *mutat* cu cheia minima
				return p;
			}
			else {
				Nod* temp = p;
				Nod* repl;
				if (p->st == nullptr) {//daca nu are subarbore stang
					repl = p->dr;
				}
				else {//daca nu are subarbore drept
					repl = p->st;
				}
				delete temp;
				dime--;
				return repl;
			}
		}
	}
}


bool Multime::cauta(TElem elem) const {
	//O(h)
	Nod* p = rad;
	while (p != nullptr && p->e != elem) {
		if (elem < p->e)
			p = p->st;
		else
			p = p->dr;
	}
	if (p == nullptr)
		return false;
	return true;
}

bool Multime::cauta_rec(Nod* p, TElem e) const{
	if (p == nullptr) {
		return false;
	}
	else {
		if (e < p->e)
			return cauta_rec(p->st, e);
		else if (e > p->e)
			return cauta_rec(p->dr, e);
		//daca e egal inseamna ca am gasit elementul
		return true;
	}
}

Nod* Multime::succesor(Nod* p) const{
	//O(h)
	if (p->dr != nullptr) {//daca are descendent drept
		return minim(p->dr);
	}
	else {
		Nod* prec = p->parinte;
		while (prec != nullptr && p == prec->dr) {
			p = prec;
			prec = prec->parinte;
		}
		return prec;
	}
}

int Multime::dim() const {
	//Theta(1)
	return dime;
}

bool Multime::vida() const {
	//Theta(1)
	return(dime == 0);
}

Multime::~Multime() {
	//O(dim)
	delete_rec(rad);
	dime = 0;
}

void Multime::delete_rec(Nod* p) {
	/*
	if (p != nullptr) {
		delete_rec(p->st);
		delete_rec(p->dr);
		delete p;
	}
	*/
	//O(dim)
	std::stack<Nod*> s;
	if (rad != nullptr) {
		s.push(rad);
	}
	while (!s.empty()) {
		Nod* aux = s.top();
		s.pop();
		if(aux->dr != nullptr)
			s.push(aux->dr);
		if (aux->st != nullptr)
			s.push(aux->st);
		delete aux;
	}
}

void Multime::intersectie(const Multime& b) {
	//O(max(b.h,h)*this.dim)
	/*
	* cur<-minim(abc.rad)
	* cat timp cur!= NIL executa
	*		succes<-succesor(cur)
	*		daca b.cauta(cur.e) = false atunci
	*			sterge(abc,cur.e)
	*		SfDaca
	*		cur<-succes
	* SfCatTimp
	*/
	Nod* cur = minim(rad);
	while (cur != nullptr) {
		Nod* succes = succesor(cur);
		if (b.cauta(cur->e) == false) {
			sterge(cur->e);
		}
		cur = succes;
	}
}


IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}

