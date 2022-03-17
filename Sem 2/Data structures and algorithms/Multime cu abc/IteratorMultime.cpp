#include "IteratorMultime.h"
#include "Multime.h"


IteratorMultime::IteratorMultime(const Multime& m) : multime(m){
	//O(h) - de la minim
	curent = multime.minim(multime.rad);
}


void IteratorMultime::prim() {
	//O(h) - de la minim
	curent = multime.minim(multime.rad);
}


void IteratorMultime::urmator() {
	//O(h) - de la succesor
	if (!valid())
		throw(std::exception());
	curent = multime.succesor(curent);
}


TElem IteratorMultime::element() const {
	//Theta(1)
	return curent->e;
}

bool IteratorMultime::valid() const {
	//Theta(1)
	if (curent == nullptr)
		return false;
	return true;
}
