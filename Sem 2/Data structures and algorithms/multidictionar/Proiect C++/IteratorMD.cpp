#include "IteratorMD.h"
#include "MD.h"

using namespace std;

IteratorMD::IteratorMD(const MD& _md): md(_md) {
	/*
	* Complexitate
	* overall case Theta(1)
	* va fi un nr constant in functie de metoda de dispersie, in acest caz prin impartire la 13, deci vor fi <=13 pasi,
	* luand in considerare redimensionarea si redispersia , amortizat tot theta 1 ar fi
	*/
	i_curent = 0;
	if (md.dime != 0) {
		while (md.ch[i_curent].cheie == cheie_nula)
			i_curent++;
	}
	h_curent = 0;
}

TElem IteratorMD::element() const{
	/*
	* Complexitate
	* best case Theta(1)
	* worst case Theta(n) n nr de noduri
	* medium case Theta(n)
	* overall case O(n)
	*/
	if (!valid())
		throw(exception());
	else {
		nod* nodul=md.ch[i_curent].head;
		for (int i = 0; i < h_curent; i++) {//iteram prin elementele cu cheia elementului curent
			nodul = nodul->next;
		}
		TValoare val = nodul->val;
		return pair <TCheie, TValoare>(md.ch[i_curent].cheie, val);
	}
	//return pair <TCheie, TValoare>  (-100000, -1);
}

bool IteratorMD::valid() const {
	/*
	* Complexitate
	* Theta(1)
	*/
	if (md.ch[i_curent].cheie == cheie_nula)//daca nu arata spre o cheie valida
		return false;
	if (i_curent >= md.m)//daca depaseste marimea containerului
		return false;
	return true;
}

void IteratorMD::urmator() {
	/*
	* Complexitate
	* best case Theta(1)
	* worst case Theta(n) n nr de noduri
	* medium case Theta(n)
	* overall case O(n)
	*/
	//verificam daca mai putem incrementa h_curent
	nod* nodul = md.ch[i_curent].head;
	int i=0;
	while (i < h_curent) {
		nodul = nodul->next;
		i++;
	}
	if (nodul->next == nullptr) {//nu putem incrementa
		h_curent = 0;
		i_curent++;
		while (md.ch[i_curent].cheie == cheie_nula)//cautam urmatorul i_curent
			i_curent++;
	}
	else {//putem incrementa
		h_curent++;
	}
}

void IteratorMD::prim() {
	/*
	* Complexitate
	* overall case Theta(1)
	* la fel ca la constructor
	*/
	i_curent = 0;
	while (md.ch[i_curent].cheie == cheie_nula)
		i_curent++;
	h_curent = 0;
}

