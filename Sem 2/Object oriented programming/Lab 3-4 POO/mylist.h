/*
Header file for mylist list declarations
*/

#ifndef MYLIST_H
#define MYLIST_H
#include "cheltuieli.h"
/*
* Tipuri de date noi pentru cheltuieli si lista de tip myList
*/

typedef struct {
	Cheltuiala* elem[101];
	int nr_elem;
}myList;

/*
	* Adauga o cheltuiala sa sfarsitul listei
	* l - myList*
	* c - Cheltuiala
*/
void adauga_sf(myList *l, Cheltuiala* c);


/*
	* Sterge cheltuiala de pe pozitia poz
	* l - myList*
	* poz - int
	*/
void sterge_poz(myList* l, int poz);


/*
	* Returneaza marimea listei de tip myList
	* l - myList*
	*/
int size(myList* l);
#endif // !MYLIST_H
