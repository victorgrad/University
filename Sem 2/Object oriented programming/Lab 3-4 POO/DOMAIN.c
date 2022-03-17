#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "vectordinamic.h"
#include "validator.h"
#include "cheltuieli.h"


int valideaza_cheltuiala(int id, int zi, int suma, char tip[], VectorDinamic* cheltuieli) {
	/*
	* Valideaza detalii despre o cheltuiala si returneaza valori int pt diferite date introduse gresit
	* zi - int
	* suma - int
	* tip - char*
	*/
	if (zi <= 0 || zi>31)
		return 1;
	if (suma < 0)
		return 2;
	if (strlen(tip) <= 0)
		return 3;
	int i;
	for (i = 0; i < cheltuieli->lg; i++) {
		if (id == get_id(cheltuieli->elems[i])) {
			return 4;
		}
	}
	return 0;

}

int valideaza_poz(int poz, VectorDinamic* cheltuieli) {
	/*
	* Valideaza detalii despre o pozitie si returneaza valori int pt date introduse gresit
	* poz - int
	* cheltuieli - myList*
	*/
	if (poz > (cheltuieli->lg - 1) || poz < 0)
		return 1;
	return 0;
}

Cheltuiala* creeaza_cheltuiala(int id, int zi, int suma, char* tip) {
	Cheltuiala* c=(Cheltuiala*)malloc(sizeof(Cheltuiala));
	c->id = id;
	c->suma = suma;
	c->zi = zi;
	c->tip = (char*)malloc((strlen(tip)+1) * sizeof(char));
	strcpy(c->tip, tip);
	return c;
}

void distruge_cheltuiala(Cheltuiala* c) {
	free(c->tip);
	free(c);
}

int get_id(Cheltuiala* c) {
	return c->id;
}

int get_zi(Cheltuiala* c) {
	return c->zi;
}

int get_suma(Cheltuiala* c) {
	return c->suma;
}

char* get_tip(Cheltuiala* c) {
	return c->tip;
}

Cheltuiala* copiaza_cheltuiala(Cheltuiala* c) {
	Cheltuiala* copie = creeaza_cheltuiala(c->id, c->zi, c->suma, c->tip);
	return copie;
}


struct beverage {
	char* name;
	char* container;
	int volume;
	int alc_volume;
};

struct beverage make_beverage(char* name,char* container,int vol, int alc) {
	struct beverage bev;
	bev.name = (char*)malloc((strlen(name)+1)*sizeof(char));
	bev.container = (char*)malloc((strlen(container) + 1) * sizeof(char));
	strcpy(bev.name, name);
	strcpy(bev.container, container);
	bev.volume = vol;
	bev.alc_volume = alc;
	return bev;
}

void display(struct beverage b) {
	if (b.alc_volume != 0)
		printf("[%s, %s, %d ml, %d %]", b.name, b.container, b.volume, b.alc_volume);
	else
		printf("[%s, %s, %d ml, non-alcoholic]", b.name, b.container, b.volume);
}

void sort(struct beverage* array, int n) {
	int sorted = 0;
	while (sorted == 0) {
		sorted = 1;
		int i;
		int j;
		for (i = 0; i < n - 1; i++) {
			if (strcmp(array[i].name, array[i + 1].name) == 0 && array[i].alc_volume > array[i + 1].alc_volume) {
				struct beverage aux=array[i];
				array[i] = array[i + 1];
				array[i + 1] = aux;
				sorted = 0;
			}
			else if (strcmp(array[i].name, array[i + 1].name) > 0) {
				struct beverage aux = array[i];
				array[i] = array[i + 1];
				array[i + 1] = aux;
				sorted = 0;
			}
		}
	}
}