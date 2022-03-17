#include <stdio.h>
#include <string.h>
#include "REPOSITORY.h"
//#include "vectordinamic.h"
#include "cheltuieli.h"

void adauga_cheltuiala(int id, int zi, int suma, char tip[], VectorDinamic* cheltuieli) {
	/*
	*Functia adauga_cheltuiala preia parametrii, creeaza un obiect de tip cheltuiala si apeleaza functia adauga_sf
	* zi - int
	* suma - int
	* tip - char*
	* cheltuieli - VectorDinamic*
	*/
	Cheltuiala* c=creeaza_cheltuiala(id,zi,suma,tip);
	add(cheltuieli, c);
}

void sterge_cheltuiala(VectorDinamic* cheltuieli, int poz) {
	/*
	*Functia sterge_cheltuiala preia parametrii si apeleaza functia sterge_poz
	* cheltuieli - VectorDinamic*
	* poz - int
	*/
	del(cheltuieli, poz);
}


