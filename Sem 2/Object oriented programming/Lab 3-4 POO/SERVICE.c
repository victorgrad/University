#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "SERVICE.h"
#include "vectordinamic.h"
#include "cheltuieli.h"

void bubbleSort(VectorDinamic* vector, int lungime, int fp(Cheltuiala* a, Cheltuiala* b));

void modificare_poz(int id,int zi, int suma, char tip[], VectorDinamic* cheltuieli,int poz) {
	/*
	*Functia modificare_poz preia parametrii, creeaza un obiect de tip cheltuiala si il modifica pe cel curent de pe pozitia poz
	* zi - int
	* suma - int
	* tip - char*
	* cheltuieli - myList*
	* poz - int
	*/
	distruge_cheltuiala(cheltuieli->elems[poz]);
	Cheltuiala* c = creeaza_cheltuiala(id, zi, suma, tip);
	cheltuieli->elems[poz] = c;
}

Service* creeazaService(VectorDinamic* v) {
	Service* service=(Service*)malloc(sizeof(Service));
	service->vector = v;
	return service;
}

void distrugeService(Service* serv) {
	distruge(serv->vector);
	free(serv);
}

void filtrare_suma(VectorDinamic* cheltuieli, VectorDinamic* listanoua, int suma) {
	int i = 0;
	for (i = 0; i < cheltuieli->lg; i++) {
		if (get_suma(cheltuieli->elems[i]) == suma) {
			Cheltuiala* c = copiaza_cheltuiala(cheltuieli->elems[i]);
			add(listanoua, c);
		}
	}
}

void filtrare_zi(VectorDinamic* cheltuieli, VectorDinamic* listanoua, int zi) {
	int i = 0;
	for (i = 0; i < cheltuieli->lg; i++) {
		if (get_zi(cheltuieli->elems[i]) == zi) {
			Cheltuiala* c = copiaza_cheltuiala(cheltuieli->elems[i]);
			add(listanoua, c);
		}
	}
}

void filtrare_tip(VectorDinamic* cheltuieli, VectorDinamic* listanoua, char* tip) {
	int i = 0;
	for (i = 0; i < cheltuieli->lg; i++) {
		if (strcmp(get_tip(cheltuieli->elems[i]), tip) == 0) {
			Cheltuiala* c = copiaza_cheltuiala(cheltuieli->elems[i]);
			add(listanoua, c);
		}
	}
}

/*
* Functia comparare sumaimeste 2 obiecte a si b de tip cheltuiala si returneaza:
* -1 : suma cheltuielii a < suma cheltuielii b
* 0 : suma celor 2 cheltuieli este egala
* 1 : suma cheltuielii a > suma cheltuielii b
* -2: nu ar intra niciodata dar imi da eroare daca nu pun
*/
int comparare_suma(Cheltuiala* a, Cheltuiala* b){
	if (get_suma(a) < get_suma(b))
		return -1;
	if (get_suma(a) == get_suma(b))
		return 0;
	if (get_suma(a) > get_suma(b))
		return 1;
	return -2;
}


/*
* Functia comparare tip primeste 2 obiecte a si b de tip cheltuiala si returneaza:
* -1 : tipul cheltuielii a < tipul cheltuielii b (ordonare alfabetica)
* 0 : tipul celor 2 cheltuieli este egal
* 1 : tipul cheltuielii a > tipul cheltuielii b (ordonare alfabetica)
*/
int comparare_tip(Cheltuiala* a, Cheltuiala* b) {
	return strcmp(get_tip(a), get_tip(b));
}

/*
* Functia reverse primeste un pointer de vector dinamic si intoarce elementele pe dos
* (ultimul element devine primul etc)
* vector - VectorDinamic*
*/
void reverse(VectorDinamic* vector) {
	int i;
	for (i = 0; i < vector->lg / 2; i++) {
		Cheltuiala* aux = vector->elems[i];
		vector->elems[i] = vector->elems[vector->lg - i - 1];
		vector->elems[vector->lg - i - 1] = aux;
	}
}

void ordonare_suma(VectorDinamic* cheltuieli, VectorDinamic* listanoua, int dir) {
	int i = 0;
	//copiez toate cheltuielile
	for (i = 0; i < cheltuieli->lg; i++) {
		Cheltuiala* c = copiaza_cheltuiala(cheltuieli->elems[i]);
		add(listanoua, c);
	}
	//qsort(listanoua->elems, listanoua->lg, sizeof(Cheltuiala*), comparare_suma);
	bubbleSort(listanoua, listanoua->lg, comparare_suma);
	if (dir == 2)
		reverse(listanoua);
}

void ordonare_tip(VectorDinamic* cheltuieli, VectorDinamic* listanoua, int dir) {
	int i = 0;
	//copiez toate cheltuielile
	for (i = 0; i < cheltuieli->lg; i++) {
		Cheltuiala* c = copiaza_cheltuiala(cheltuieli->elems[i]);
		add(listanoua, c);
	}
	//qsort(listanoua->elems, listanoua->lg, sizeof(Cheltuiala*), comparare_tip);
	bubbleSort(listanoua, listanoua->lg, comparare_tip);

	if (dir == 2)
		reverse(listanoua);
}

void bubbleSort(VectorDinamic* vector, int lungime,int fp(Cheltuiala* a,Cheltuiala* b))
{
	int i, j;
	for (i = 0; i < lungime - 1; i++)
		for (j = 0; j < lungime - i - 1; j++)
			if ((*fp)(vector->elems[j], vector->elems[j + 1]) > 0) {
				Cheltuiala* aux = vector->elems[j];
				vector->elems[j] = vector->elems[j+1];
				vector->elems[j+1] = aux;
			}
				
}