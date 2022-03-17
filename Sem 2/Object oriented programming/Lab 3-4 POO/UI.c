#include <stdlib.h>
#include <stdio.h>
#include "UI.h"
#include "validator.h"
#include "REPOSITORY.h"
#include "vectordinamic.h"
#include "SERVICE.h"
#include "cheltuieli.h"

UI* creeazaUi(Service* serv) {
	UI* uim = (UI*)malloc(sizeof(UI));
	uim->serv = serv;
	return uim;
}

void distrugeUi(UI* ui) {
	distrugeService(ui->serv);
	free(ui);
}

int citeste_cheltuiala(int *id, int *zi, int *suma, char *tip) {
	/*
	* Functia citeste_cheltuiala citeste de la utilizator date despre o cheltuiala(zi,suma si tip)
	* zi-int*
	* suma-int*
	* tip-char*
	*/
	printf("Introduceti id-ul cheltuielii:");
	if (scanf_s("%d", id) != 1) {
		while(getchar()!='\n');
		printf("ID invalid\n");
		return -1;
	}
	printf("Introduceti ziua cheltuielii:");
	if (scanf_s("%d", zi) != 1) {
		while (getchar() != '\n');
		printf("Zi invalida\n");
		return -1;
	}
	printf("Introduceti suma cheltuielii:");
	if (scanf_s("%d", suma) != 1) {
		while (getchar() != '\n');
		printf("Suma invalida\n");
		return -1;
	}
	printf("Introduceti tipul cheltuielii:");
	scanf_s("%s", tip, 20);
	while (getchar() != '\n');
	return 1;
}

void adauga(VectorDinamic *cheltuieli){
	/*
	* Functia adauga preia de la tastatura date despre o cheltuiala,le valideaza si apeleaza functia adauga_cheltuiala
	* Trateaza datele invalide si printeaza raspunsuri adecvate
	* cheltuieli - VectorDinamic*
	*/
	int zi = 0, suma = 0,id = -1;
	char tip[20];
	int er = 0;
	int er2;
	er2=citeste_cheltuiala(&id, &zi, &suma, tip);
	if (er2 != -1) {
		er = valideaza_cheltuiala(id, zi, suma, tip, cheltuieli);
		if (er == 0) {
			adauga_cheltuiala(id, zi, suma, tip, cheltuieli);
		}
		else if (er == 1) {
			printf("Zi invalida\n");
		}
		else if (er == 2) {
			printf("Suma invalida\n");
		}
		else if (er == 3) {
			printf("Tip invalid\n");
		}
		else if (er == 4) {
			printf("ID existent\n");
		}
	}
	
}

void modifica(VectorDinamic* cheltuieli) {
	/*
	* Functia modifica preia de la tastatura date despre o cheltuiala,le valideaza si apeleaza functia modifica_cheltuiala
	* Trateaza datele invalide si printeaza raspunsuri adecvate
	* cheltuieli-myList*
	*/
	int id, er = 0,er2=0;
	printf("Inotrduceti id-ul cheltuielii pe care doriti sa o modificati: ");
	scanf_s("%d", &id);
	er = get_poz(cheltuieli,id);
	if (er != -1) {
		int zi = 0, suma = 0,ero=0, idn=-1;
		char tip[20];
		er2=citeste_cheltuiala(&idn, &zi, &suma, tip);
		if (er2 != -1) {
			ero = valideaza_cheltuiala(idn, zi, suma, tip, cheltuieli);
			if (ero == 0) {
				modificare_poz(idn, zi, suma, tip, cheltuieli, er);
			}
			else if (ero == 1) {
				printf("Zi invalida\n");
			}
			else if (ero == 2) {
				printf("Suma invalida\n");
			}
			else if (ero == 3) {
				printf("Tip invalid\n");
			}
			else if (ero == 4) {
				printf("ID existent\n");
			}
		}
	}
	else if (er == -1) {
		printf("ID invalid\n");
	}

}

void sterge(VectorDinamic* cheltuieli) {
	/*
	* Functia sterge preia de la tastatura o pozitie,o valideaza si apeleaza functia sterge_cheltuiala
	* Trateaza datele invalide si printeaza raspunsuri adecvate
	* cheltuieli-VectorDinamic*
	*/
	int id,er=0;
	printf("Introduceti id-ul cheltuielii pe care doriti sa o stergeti:");
	scanf_s("%d", &id);
	er = get_poz(cheltuieli,id);
	if (er !=-1) {
		sterge_cheltuiala(cheltuieli, er);
	}
	else if (er == -1) {
		printf("ID invalid\n");
	}
}

void afisare_cheltuieli(VectorDinamic* cheltuieli) {
	/*
	* Functia afisare_cheltuieli afiseaza cheltuielile din lista de cheltuieli
	* Trateaza datele invalide si printeaza raspunsuri adecvate
	* cheltuieli-VectorDinamic*
	*/
	int i;
	if (cheltuieli->lg > 0) {
		printf("================================================\n");
		for (i = 0; i < cheltuieli->lg; i++) {
			printf("ID: %d  /  ", get_id(cheltuieli->elems[i]));
			printf("ZI: %d  /  ", get_zi(cheltuieli->elems[i]));
			printf("SUMA: %d  /  ", get_suma(cheltuieli->elems[i]));
			printf("TIP: %s\n", get_tip(cheltuieli->elems[i]));
			}
		printf("================================================\n");
	}
	else {
		printf("Nu exista cheltuieli de afisat\n");
	}
}

/*
* Functia filtrare preia vectorul dinamic cu cheltuieli, filtreaza cheltuielile dupa un anumit criteriu si le afiseaza
* cheltuieli - VectorDinamic*
*/
void filtrare(VectorDinamic* cheltuieli) {
	printf("Dupa ce criteriu doriti filtrarea listei?:\n1 - Suma\n2 - Ziua\n3 - Tip\n");
	int optiune = -1;
	if (scanf_s("%d", &optiune));
	VectorDinamic* listanoua = creazaVectorDinamic();
	if (optiune == 1) {
		int suma = -1;
		printf("Introduceti suma dorita: ");
		scanf_s("%d", &suma);
		filtrare_suma(cheltuieli, listanoua, suma);
	}
	else if (optiune == 2) {
		int zi = -1;
		printf("Introduceti ziua dorita: ");
		scanf_s("%d", &zi);
		filtrare_zi(cheltuieli, listanoua, zi);
	}
	else if (optiune == 3) {
		char tip[20];
		printf("Introduceti tipul dorit: ");
		scanf_s("%s", tip,20);
		filtrare_tip(cheltuieli, listanoua, tip);
	}
	else
		printf("Comanda invalida\n");


	afisare_cheltuieli(listanoua);
	distruge(listanoua);
}

/*
* Functia ordonare preia vectorul dinamic cu cheltuieli, ordoneaza cheltuielile dupa un anumit criteriu si le afiseaza
* cheltuieli - VectorDinamic*
*/
void ordonare(VectorDinamic* cheltuieli) {
	printf("Dupa ce criteriu doriti ordonarea listei?:\n1 - Suma\n2 - Tip\n");
	int optiune = -1;
	if (scanf_s("%d", &optiune));
	VectorDinamic* listanoua = creazaVectorDinamic();
	if (optiune == 1) {
		printf("Doriti ordonare:\n1 - Crescatoare\n2 - Descrescatoare\n");
		int optiune2 = -1;
		if (scanf_s("%d", &optiune2));
		if (optiune2 == 1) {
			ordonare_suma(cheltuieli, listanoua, 1);
		}
		else if (optiune2 == 2) {
			ordonare_suma(cheltuieli, listanoua, 2);
		}
		else
			printf("Comanda invalida\n");

	}
	else if (optiune == 2) {
		printf("Doriti ordonare:\n1 - Crescatoare\n2 - Descrescatoare\n");
		int optiune2 = -1;
		if (scanf_s("%d", &optiune2));
		if (optiune2 == 1) {
			ordonare_tip(cheltuieli, listanoua, 1);
		}
		else if (optiune2 == 2) {
			ordonare_tip(cheltuieli, listanoua, 2);
		}
		else
			printf("Comanda invalida\n");

	}
	else
		printf("Comanda invalida\n");


	afisare_cheltuieli(listanoua);
	distruge(listanoua);
}

void run_app(UI* ui) {
	/*
	* Functia run_app ruleaza aplicatia si contine meniul principal
	*/
	while (1) {
		printf("1 - Vizualizati Cheltuieli\n2 - Adaugati cheltuiala\n3 - Stergeti cheltuiala\n4 - Modificati cheltuiala\n5 - Vizualizare lista de cheltuieli filtrat dupa o proprietate\n6 - Vizualizare lista de cheltuieli ordonat dupa suma sau tip\n7 - Exit\n");
		fflush(stdout);
		int optiune;
		if(scanf_s("%d", &optiune));
		if (optiune == 1) {
			afisare_cheltuieli(ui->serv->vector);
		}
		else if (optiune == 2) {
			adauga(ui->serv->vector);
		}
		else if (optiune == 3) {
			sterge(ui->serv->vector);
		}
		else if (optiune == 4) {
			modifica(ui->serv->vector);
		}
		else if (optiune == 5) {
			filtrare(ui->serv->vector);
		}
		else if (optiune == 6) {
			ordonare(ui->serv->vector);
		}
		else if (optiune == 7) {
			break;
		}
	}
	printf("By By!");
}