#include "MD.h"
#include "IteratorMD.h"
#include <exception>
#include <iostream>

using namespace std;

void Element::operator=(const Element& el) {
	this->cheie = el.cheie;
	this->head = el.head;
}

MD::MD() {
	/*
	* Complexitate
	* overall case Theta(m),nr maxim de chei
	*/
	ch = new Element[100000];
	urm = new int[100000];
	m = 100000;
	primLiber = 0;
	prim = 13;
	for (int i = 0; i < m; i++) {
		urm[i] = -1;
	}
	dime = 0;
}


void MD::adauga(TCheie c, TValoare v) {
	/*
	* Complexitate
	* best case Theta(1)
	* worst case Theta(m) m,nr de chei din tabela
	* medium case Theta(m)
	* overall case O(m),nr maxim de chei
	*/
	int poz = d(c);
	if (ch[poz].cheie == cheie_nula) {//poz este libera, memoram
		ch[poz].cheie = c;
		nod* el = new nod;
		el->val = v;
		el->next = nullptr;
		ch[poz].head = el;
		dime++;
		if(poz==primLiber)
			actprimLiber();
	}
	else {
		int prev=0;
		while (poz != -1 and ch[poz].cheie!=c) {//cautam pozitia pe care trebuie inserat
			prev = poz;
			poz = urm[poz];
		}
		if (poz != -1) {//am mai gasit cheia deci adaugam doar valoarea
			nod* el = new nod;
			el->val = v;
			el->next = ch[poz].head;
			ch[poz].head = el;
			dime++;
		}
		else {
			if (primLiber < m - 1) {//tabela nu e plina
				ch[primLiber].cheie = c;
				nod* el = new nod;
				el->val = v;
				el->next = nullptr;
				ch[primLiber].head = el;
				urm[prev] = primLiber;
				actprimLiber();
				dime++;
			}
			else {//depasire tabela

			}
		}
	}
	/*
	itr = frecv.find(to_string(v));
	if (itr != frecv.end()) {
		itr->second++;
	}
	else {//daca nu e in dict
		frecv.insert(pair<string, int>(to_string(v), 1));
	}*/
}


bool MD::sterge(TCheie c, TValoare v) {
	/*
	* Complexitate
	* best case Theta(1)
	* worst case Theta(m) m,nr de chei din tabela sau theta(n),n este nr de ordine a valorii gasite pe acea cheie(daca)
	* medium case Theta(m) sau Theta(n)
	* overall case O(m)
	*/
	int i = d(c);
	int j = 1;
	int k = 0;
	/*
	while (k < m && j != -1) {
		if (urm[k] == i)
			j = k;
		k++;
	}
	*/
	while (i != -1 and ch[i].cheie != c) {
		j = i;
		i = urm[i];
	}
	bool gata;
	if (i == -1)//nu am gasit cheia
		return false;
	else {//daca am gasit-o
		//daca e singura valoare
		if (ch[i].head->val==v && ch[i].head->next==nullptr) {
			gata = false;
			delete ch[i].head;
			while (true) {
				k = urm[i];
				int ka = i;
				while (k != -1 && d(ch[i].cheie) != i) {
					ka = k;
					k = urm[k];
				}
				if (k == -1) {
					gata = true;
					break;
				}
				else {
					ch[i] = ch[k];
					i = k;
					j = ka;
				}
			}
			if (j != -1) {
				urm[j] = urm[i];
			}
			//stergerea
			ch[i].cheie = cheie_nula;
			ch[i].head = nullptr;
			urm[i] = -1;
			if (i < primLiber)
				primLiber = i;
			dime--;
		}
		else {//daca sunt >= 2 val
			if (ch[i].head->val == v) {//daca e prima
				nod* aux= ch[i].head;
				ch[i].head = ch[i].head->next;
				delete aux;
				aux = nullptr;
				dime--;
			}
			else {//daca nu e prima valoare
				nod* prev = ch[i].head;
				nod* cur = ch[i].head->next;
				while (cur != nullptr && cur->val!=v) {
					prev = cur;
					cur = cur->next;
				}
				if (cur == nullptr)//daca nu am gasit valoarea
					return false;
				else {//altfel refacem legaturile
					prev->next = cur->next;
					delete cur;
					cur = nullptr;
					dime--;
				}
			}

		}
	}
	return true;
}


vector<TValoare> MD::cauta(TCheie c) const {
	/*
	* Complexitate
	* best case Theta(1),
	* worst case Theta(m+n) m nr de chei,n nr de valori a cheii
	* medium case Theta(m+n)
	* overall case O(m+n)
	*/
	vector<TValoare> rez;
	int i = d(c);
	while (i != -1 && ch[i].cheie != c) {
		i = urm[i];
	}
	if (i != -1) {
		nod* next=ch[i].head;
		while (next != nullptr) {
			rez.push_back(next->val);
			next = next->next;
		}
		return rez;
	}
	return vector<TValoare>();
}


int MD::dim() const {
	/*
	* Complexitate
	* Theta(1),
	*/
	return dime;
}


bool MD::vid() const {
	/*
	* Complexitate
	* Theta(1),
	*/
	if (dime != 0)
		return false;
	return true;
}

IteratorMD MD::iterator() const {
	/*
	* Complexitate
	* Theta(1),
	*/
	return IteratorMD(*this);
}

MD::~MD() {
	/*
	* Complexitate
	* overall case Theta(n) n nr total de valori
	*/
	for (int i = 0; i < m; i++) {
		delnoduri(ch[i].head);
	}
	delete[] ch;
	delete[] urm;
	dime = 0;
	ch = nullptr;
	urm = nullptr;
}

int MD::d(TCheie c) const{
	/*
	* Complexitate
	* Theta(1),
	*/
	if (c < 0)
		c = -c;
	return c % prim;
}

void MD::actprimLiber() {
	/*
	* Complexitate
	* best case Theta(1),
	* worst case Theta(m) m nr de chei
	* medium case Theta(m)
	* overall case O(m)
	*/
	primLiber++;
	while (primLiber < m && ch[primLiber].cheie != cheie_nula) {
		primLiber++;
	}
}

void MD::delnoduri(nod* head) {
	/*
	* Complexitate
	* best case Theta(1),
	* worst case Theta(n) n nr de noduri
	* medium case Theta(n)
	* overall case O(n)
	*/
	nod* nextt ;
	while (head != nullptr) {
		nextt = head->next;
		delete head;
		head = nextt;
	}
	head = nullptr;
}
TCheie MD::cheieMinima() const {
	/*
	* Complexitate Theta(m),m nr de chei
	* i<-0
	* minn<-9999999 (max_tcheie)
	* daca md.dime = 0 atunci
	*		returneaza NULL_TCHEIE
	* altfel
	*		pentru i<-0,m,1 executa
	*			daca md.ch[i].cheie != cheie_nula si md.ch[i].cheie < minn
					minn = md.ch[i].cheie
			returneaza minn
	*/
	int i = 0;
	int minn = 9999999;
	if (dime == 0)
		return NULL_TCHEIE;
	else {
		for (i = 0; i < m; i++) {
			if (ch[i].cheie != cheie_nula and ch[i].cheie < minn)
				minn = ch[i].cheie;
		}
		return minn;
	}
}