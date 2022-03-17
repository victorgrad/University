#pragma once
#include<vector>
#include<utility>
#include<map>
#include<string>

#define NULL_TCHEIE 0

using namespace std;

typedef int TCheie;
typedef int TValoare;
#define cheie_nula 900000

typedef std::pair<TCheie, TValoare> TElem;

class IteratorMD;

struct nod {
	TValoare val;
	nod* next;
};


class Element {
public:
	Element() {
		cheie = cheie_nula;
		head = nullptr;
		cheie_negativa = false;
	}
	~Element()=default;
	TCheie cheie;
	bool cheie_negativa;
	nod* head;
	void operator=(const Element& el);
};



class MD
{
	friend class IteratorMD;

private:
	/* aici e reprezentarea */
	int m;//capacitatea tabelei
	int prim;//nr la care facem modulo dispersia
	Element* ch;//elementele
	int* urm;//urm
	int primLiber;
	int d(TCheie c) const;//functie de dispersie
	int dime;
	void actprimLiber();
	void delnoduri(nod* head);//sterge nodurile

	map<string, int> frecv;
	map<string, int>::iterator itr;

public:
	// constructorul implicit al MultiDictionarului
	MD();
	// adauga o pereche (cheie, valoare) in MD	
	void adauga(TCheie c, TValoare v);

	//cauta o cheie si returneaza vectorul de valori asociate
	vector<TValoare> cauta(TCheie c) const;

	//sterge o cheie si o valoare 
	//returneaza adevarat daca s-a gasit cheia si valoarea de sters
	bool sterge(TCheie c, TValoare v);

	//returneaza numarul de perechi (cheie, valoare) din MD 
	int dim() const;

	//verifica daca MultiDictionarul e vid 
	bool vid() const;

	// se returneaza iterator pe MD
	IteratorMD iterator() const;

	// destructorul MultiDictionarului	
	~MD();
	TValoare ceaMaiFrecventaValoare() const;

	//Gaseste si returneaza cheia minima din dictionar
	TCheie cheieMinima() const;
};

