/*
* Repository header file
*/

#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "vectordinamic.h"

/*
	*Functia adauga_cheltuiala preia parametrii, creeaza un obiect de tip cheltuiala si apeleaza functia adauga_sf
	* zi - int
	* suma - int
	* tip - char*
	* c - VectorDinamic* cu cheltuieli
	*/
void adauga_cheltuiala(int id,int zi, int suma, char tip[], VectorDinamic* c);


/*
	*Functia sterge_cheltuiala preia parametrii si apeleaza functia sterge_poz
	* c - VectorDinamic* cu cheltuieli
	* poz - int
	*/
void sterge_cheltuiala(VectorDinamic* c, int poz);

#endif // !REPOSITORY_H
