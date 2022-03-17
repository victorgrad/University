#include <assert.h>
#include <stdio.h>
#include <string.h>
#include "cheltuieli.h"
#include "validator.h"
#include "REPOSITORY.h"
#include "vectordinamic.h"
#include "SERVICE.h"

void test_add() {
	VectorDinamic* chl = creazaVectorDinamic();
	Service* serv = creeazaService(chl);
	Cheltuiala* c = creeaza_cheltuiala(2, 3, 4, "wow");
	add(chl, c);
	assert(size(chl) == 1);
	assert(strcmp(get_tip(chl->elems[0]), "wow")==0);


	adauga_cheltuiala(1, 2, 3, "bun", chl);
	assert(size(chl) == 2);
	assert(strcmp(get_tip(chl->elems[1]), "bun")==0);
	distrugeService(serv);
}

void test_del(){
	VectorDinamic* chl = creazaVectorDinamic();
	Service* serv = creeazaService(chl);
	adauga_cheltuiala(1, 2, 3, "bun", chl);
	assert(size(chl) == 1);

	sterge_cheltuiala(chl, 0);
	assert(size(chl) == 0);

	adauga_cheltuiala(2, 2, 3, "ban", chl);
	adauga_cheltuiala(3, 2, 3, "beu", chl);
	assert(size(chl) == 2);
	sterge_cheltuiala(chl, 1);
	assert(size(chl) == 1);
	assert(get_id(chl->elems[0]) == 2);
	adauga_cheltuiala(3, 1, 2, "bau", chl);
	sterge_cheltuiala(chl, 0);
	assert(get_id(chl->elems[0]) == 3);
	distrugeService(serv);
}

void test_val_cheltuiala() {
	VectorDinamic* chl = creazaVectorDinamic();
	Service* serv = creeazaService(chl);
	assert(valideaza_cheltuiala(1,-1, 5, "bun", chl) == 1);
	assert(valideaza_cheltuiala(1,0, 5, "bun", chl) == 1);
	assert(valideaza_cheltuiala(1,1, 5, "bun", chl) == 0);

	assert(valideaza_cheltuiala(1,2, -3, "bun", chl) == 2);
	assert(valideaza_cheltuiala(1,2, 0, "bun", chl) == 0);
	assert(valideaza_cheltuiala(1,2, -1, "bun", chl) == 2);

	assert(valideaza_cheltuiala(1,1, 5, "", chl) == 3);
	assert(valideaza_cheltuiala(1,1, 5, "dwawad", chl) == 0);
	assert(valideaza_cheltuiala(1,1, 5, "1", chl) == 0);

	adauga_cheltuiala(1, 2, 3, "bun", chl);
	assert(valideaza_cheltuiala(1, 1, 5, "adw", chl) == 4);
	distrugeService(serv);
}

void test_val_poz() {
	VectorDinamic* chl = creazaVectorDinamic();
	Service* serv = creeazaService(chl);
	adauga_cheltuiala(1, 2, 3, "bun", chl);
	assert(valideaza_poz(0, chl) == 0);
	assert(valideaza_poz(1, chl) == 1);
	assert(valideaza_poz(-1, chl) == 1);

	adauga_cheltuiala(2, 2, 3, "bun", chl);
	assert(valideaza_poz(0, chl) == 0);
	assert(valideaza_poz(1, chl) == 0);
	assert(valideaza_poz(-1, chl) == 1);
	distrugeService(serv);
}

void test_mod() {
	VectorDinamic* chl = creazaVectorDinamic();
	Service* serv = creeazaService(chl);
	adauga_cheltuiala(1, 2, 3, "bun", chl);
	assert(strcmp(get_tip(chl->elems[0]), "bun") == 0);
	assert(get_suma(chl->elems[0]) == 3);
	assert(get_zi(chl->elems[0]) == 2);
	assert(get_id(chl->elems[0]) == 1);

	modificare_poz(5, 4, 2, "yey", chl, 0);
	assert(strcmp(get_tip(chl->elems[0]), "yey") == 0);
	assert(get_suma(chl->elems[0]) == 2);
	assert(get_zi(chl->elems[0]) == 4);
	assert(get_id(chl->elems[0]) == 5);
	distrugeService(serv);
}

void test_get_el() {
	VectorDinamic* chl = creazaVectorDinamic();
	Service* serv = creeazaService(chl);
	Cheltuiala* c = creeaza_cheltuiala(2, 3, 4, "wow");
	add(chl, c);
	assert(get(chl, 0) == c);
	distrugeService(serv);
}

void test_resize_down() {
	VectorDinamic* chl = creazaVectorDinamic();
	Service* serv = creeazaService(chl);
	adauga_cheltuiala(1, 2, 3, "bun", chl);
	adauga_cheltuiala(2, 2, 3, "bun", chl);
	adauga_cheltuiala(3, 2, 3, "bun", chl);
	adauga_cheltuiala(4, 2, 3, "bun", chl);
	adauga_cheltuiala(5, 2, 3, "bun", chl);
	sterge_cheltuiala(chl, 0);
	sterge_cheltuiala(chl, 0);
	sterge_cheltuiala(chl, 0);
	sterge_cheltuiala(chl, 0);
	distrugeService(serv);
}

void test_get_poz() {
	VectorDinamic* chl = creazaVectorDinamic();
	Service* serv = creeazaService(chl);
	adauga_cheltuiala(1, 2, 3, "bun", chl);
	adauga_cheltuiala(2, 2, 3, "bun", chl);

	assert(get_poz(chl, 1) == 0);
	assert(get_poz(chl, 2) == 1);
	assert(get_poz(chl, 3) == -1);

	distrugeService(serv);
}

void test_copiaza_chelt() {
	Cheltuiala* c = creeaza_cheltuiala(2, 3, 4, "wow");
	Cheltuiala* copie = copiaza_cheltuiala(c);
	assert(copie->id == 2);
	assert(copie->suma == 4);
	assert(strcmp(copie->tip, "wow") == 0);
	assert(copie->zi == 3);
	distruge_cheltuiala(c);
	distruge_cheltuiala(copie);
}

void test_filtrare() {
	VectorDinamic* chl = creazaVectorDinamic();
	Service* serv = creeazaService(chl);
	adauga_cheltuiala(1, 3, 3, "ben", chl);
	adauga_cheltuiala(2, 2, 1, "bun", chl);
	adauga_cheltuiala(3, 3, 1, "brn", chl);
	adauga_cheltuiala(4, 2, 3, "bun", chl);
	adauga_cheltuiala(5, 4, 3, "bin", chl);

	VectorDinamic* listanoua1 = creazaVectorDinamic();
	filtrare_suma(chl, listanoua1, 1);
	assert(size(listanoua1) == 2);
	assert(get_suma(listanoua1->elems[0]) == 1);
	distruge(listanoua1);

	VectorDinamic* listanoua2 = creazaVectorDinamic();
	filtrare_zi(chl, listanoua2, 2);
	assert(size(listanoua2) == 2);
	assert(get_zi(listanoua2->elems[0]) == 2);
	distruge(listanoua2);

	VectorDinamic* listanoua3 = creazaVectorDinamic();
	filtrare_tip(chl, listanoua3, "bun");
	assert(size(listanoua3) == 2);
	assert(strcmp(get_tip(listanoua3->elems[0]),"bun") == 0);
	distruge(listanoua3);

	distrugeService(serv);
}

void test_ordonare() {
	VectorDinamic* chl = creazaVectorDinamic();
	Service* serv = creeazaService(chl);
	adauga_cheltuiala(1, 3, 2, "az", chl);
	adauga_cheltuiala(2, 2, 1, "c", chl);
	adauga_cheltuiala(3, 3, 2, "b", chl);
	adauga_cheltuiala(4, 2, 4, "a", chl);


	VectorDinamic* listanoua1 = creazaVectorDinamic();
	ordonare_suma(chl, listanoua1, 1);
	assert(get_suma(listanoua1->elems[0]) == 1);
	assert(get_suma(listanoua1->elems[1]) == 2);
	assert(get_suma(listanoua1->elems[2]) == 2);
	assert(get_suma(listanoua1->elems[3]) == 4);
	distruge(listanoua1);

	VectorDinamic* listanoua2 = creazaVectorDinamic();
	ordonare_suma(chl, listanoua2, 2);
	assert(get_suma(listanoua2->elems[0]) == 4);
	assert(get_suma(listanoua2->elems[1]) == 2);
	assert(get_suma(listanoua2->elems[2]) == 2);
	assert(get_suma(listanoua2->elems[3]) == 1);
	distruge(listanoua2);

	VectorDinamic* listanoua3 = creazaVectorDinamic();
	ordonare_tip(chl, listanoua3, 1);
	assert(strcmp(get_tip(listanoua3->elems[0]),"a") == 0);
	assert(strcmp(get_tip(listanoua3->elems[1]), "az") == 0);
	assert(strcmp(get_tip(listanoua3->elems[2]), "b") == 0);
	assert(strcmp(get_tip(listanoua3->elems[3]), "c") == 0);
	distruge(listanoua3);

	VectorDinamic* listanoua4 = creazaVectorDinamic();
	ordonare_tip(chl, listanoua4, 2);
	assert(strcmp(get_tip(listanoua4->elems[3]), "a") == 0);
	assert(strcmp(get_tip(listanoua4->elems[2]), "az") == 0);
	assert(strcmp(get_tip(listanoua4->elems[1]), "b") == 0);
	assert(strcmp(get_tip(listanoua4->elems[0]), "c") == 0);
	distruge(listanoua4);

	distrugeService(serv);
}

void run_tests() {
	test_add();
	test_val_cheltuiala();
	test_val_poz();
	test_del();
	test_mod();
	test_get_el();
	test_resize_down();
	test_get_poz();
	test_copiaza_chelt();
	test_filtrare();
	test_ordonare();
}
