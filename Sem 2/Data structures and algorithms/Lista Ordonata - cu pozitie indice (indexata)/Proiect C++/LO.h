#pragma once

class Iterator;

typedef int TComparabil;
typedef TComparabil TElement;

typedef bool (*Relatie)(TElement, TElement);

#define NULL_TELEMENT -1

class LO {
private:
	friend class Iterator;
private:
	/* aici e reprezentarea */
	TElement* e;
	int* urm;
	int* prec;
	//o poz
	int prim;
	int ultim;
	//o poz
	int primLiber;
	//un nr
	int nrelem;
	//un nr
	int cp;
	//un nr
	int lg;
	Relatie r;

	/*
	* Overall complexity Theta(1)
	*/
	int aloca();

	/*
	* Overall complexity Theta(1)
	*/
	void dealoca(int i);

	/*
	* Best Case Theta(1)
	* Medium Case Theta(n)
	* Worst Case Theta(n)
	* Overall complexity  Theta(1) amortizat
	*/
	int creeazaNod(TElement e);

	/*
	* Overall complexity Theta(n)
	*/
	void redim();

	/*
	* Overall complexity Theta(n)
	*/
	void initSpatiuLiber(int cp);

	/*
	* Overall complexity Theta(cp)
	*/
	void reinitSpatiuLiber(int cpveche);


public:
	// constructor
	/*
	* Overall complexity Theta(1)
	*/
	LO(Relatie r);

	// returnare dimensiune
	/*
	* Overall complexity Theta(1)
	*/
	int dim() const;

	// verifica daca LO e vida
	/*
	* Overall complexity Theta(1)
	*/
	bool vida() const;

	// returnare element
	//arunca exceptie daca i nu e valid
	/*
	* Best Case Theta(1)
	* Medium Case Theta(n)
	* Worst Case Theta(n)
	* Overall complexity O(n)
	*/
	TElement element(int i) const;

	// adaugare element in LO a.i. sa se pastreze ordinea intre elemente
	/*
	* Overall complexity Theta(1)
	*/
	void adauga(TElement e);

	// sterge element de pe o pozitie i si returneaza elementul sters
	//arunca exceptie daca i nu e valid
	/*
	* Best Case Theta(1)
	* Medium Case Theta(n)
	* Worst Case Theta(n)
	* Overall complexity O(n)
	* pt ca trebuie parcurse pana la poz i
	*/
	TElement sterge(int i);

	// cauta element si returneaza prima pozitie pe care apare (sau -1)
	/*
	* Best Case Theta(1)
	* Medium Case Theta(n)
	* Worst Case Theta(n)
	* Overall complexity O(n)
	*/
	int cauta(TElement e) const;

	// returnare iterator
	/*
	* Overall complexity Theta(1)
	*/
	Iterator iterator();

	void afisare();

	//destructor
	~LO();

};
