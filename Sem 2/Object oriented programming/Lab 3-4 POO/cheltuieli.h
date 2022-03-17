
#ifndef CHELTUIELI_H
#define CHELTUIELI_H

typedef struct {
	int zi;
	int suma;
	int id;
	char *tip;
}Cheltuiala;

/*
* creeaza un obiect de tip cheltuiala
*/
Cheltuiala* creeaza_cheltuiala(int id, int zi, int suma, char* tip);

/*
* Distruge elementul c de tip cheltuiala si elibereaza spatiul corespunzator din heap
* c - Cheltuiala*
*/
void distruge_cheltuiala(Cheltuiala* c);

/*
* Returneaza id-ul unei cheltuieli
* c - Cheltuiala*
*/
int get_id(Cheltuiala* c);

/*
* Returneaza tipul unei cheltuieli
* c - Cheltuiala*
*/
char* get_tip(Cheltuiala* c);

/*
* Returneaza suma unei cheltuieli
* c - Cheltuiala*
*/
int get_suma(Cheltuiala* c);

/*
* Returneaza ziua unei cheltuieli
* c - Cheltuiala*
*/
int get_zi(Cheltuiala* c);

/*
* creeaza si returneaza o copie a unei cheltuieli c
* c - Cheltuiala*
*/
Cheltuiala* copiaza_cheltuiala(Cheltuiala* c);
#endif // !CHELTUIELI_H
