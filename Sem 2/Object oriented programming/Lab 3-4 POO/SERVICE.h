/*
* Service header file
*/

#ifndef SERVICE_H
#define SERVICE_H
#include "vectordinamic.h"

typedef struct {
	VectorDinamic* vector;
}Service;

/*
	*Functia modificare_poz preia parametrii, creeaza un obiect de tip cheltuiala si il modifica pe cel curent de pe pozitia poz
	* id - int
	* zi - int
	* suma - int
	* tip - char*
	* cheltuieli - VectorDinamic*
	* poz - int
	*/
void modificare_poz(int id, int zi, int suma, char tip[], VectorDinamic* cheltuieli, int poz);

/*
* Creeaza service-ul pentru aplicatie
* v - vectorul dinamic aka repo-ul
*/
Service* creeazaService(VectorDinamic* v);

/*
* Elibereaza memoria ocupata de service
*/
void distrugeService(Service* serv);

/*
* Functia filtrare suma preia lista de cheltuieli, o lista noua in care va returna cheltuielile care contin acea suma, si suma de cautat
* cheltuieli - VectorDinamic*
* listanoua - VectorDinamic*
* suma - int
*/
void filtrare_suma(VectorDinamic* cheltuieli,VectorDinamic* listanoua,int suma);

/*
* Functia filtrare zi preia lista de cheltuieli, o lista noua in care va returna cheltuielile care contin acea zi, si ziua de cautat
* cheltuieli - VectorDinamic*
* listanoua - VectorDinamic*
* zi - int
*/
void filtrare_zi(VectorDinamic* cheltuieli, VectorDinamic* listanoua,int zi);

/*
* Functia filtrare suma preia lista de cheltuieli, o lista noua in care va returna cheltuielile care contin acel tip, si tipul de cautat
* cheltuieli - VectorDinamic*
* listanoua - VectorDinamic*
* tip - char*
*/
void filtrare_tip(VectorDinamic* cheltuieli, VectorDinamic* listanoua,char* tip);

/*
* Functia ordonare suma preia lista de cheltuieli, o lista noua in care va returna cheltuielile ordonate dupa suma, si directia (1-crescator/2-descrescator)
* cheltuieli - VectorDinamic*
* listanoua - VectorDinamic*
* dir - int
*/
void ordonare_suma(VectorDinamic* cheltuieli, VectorDinamic* listanoua, int dir);


/*
* Functia ordonare tip preia lista de cheltuieli, o lista noua in care va returna cheltuielile ordonate dupa tip, si directia (1-crescator/2-descrescator)
* cheltuieli - VectorDinamic*
* listanoua - VectorDinamic*
* dir - int
*/
void ordonare_tip(VectorDinamic* cheltuieli, VectorDinamic* listanoua, int dir);


#endif // !SERVICE_H

