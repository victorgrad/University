#include "Iterator.h"
#include "LO.h"
#include <iostream>
#include <exception>

Iterator::Iterator(const LO& lo) : lista(lo){
	/* de adaugat */
	curent = lista.prim;
}

void Iterator::prim() {
	/* de adaugat */
	curent = lista.prim;
}

void Iterator::ultim() {
	curent = lista.ultim;
}

void Iterator::urmator(){
	/* de adaugat */
	if (!valid())
		throw(std::exception());
	curent = lista.urm[curent];
}

void Iterator::anterior() {
	if (!valid())
		throw(std::exception());
	curent = lista.prec[curent];
}

bool Iterator::valid() const{
	/* de adaugat */
	return curent != -1;
}

TElement Iterator::element() const{
	if (!valid())
		throw(std::exception());
	return lista.e[curent];
}


