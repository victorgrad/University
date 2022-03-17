#pragma once

#define NULL_TELEM -1
typedef int TElem;

class IteratorMultime;

class Nod {
public:
	TElem e;
	Nod* st;
	Nod* dr;
	Nod* parinte;

	Nod(TElem el, Nod* stn, Nod* drn, Nod* prn) {
		e = el;
		st = stn;
		dr = drn;
		parinte = prn;
	}
	~Nod()=default;
};

class Multime {
	friend class IteratorMultime;

    private:
		Nod* rad;
		int dime;

    public:
 		//constructorul implicit
		Multime();

		Nod* creeazaNod(TElem e,Nod* prec) {
			Nod* p = new Nod(e,nullptr,nullptr,prec);
			return p;
		}

		//adauga un element in multime
		//returneaza adevarat daca elementul a fost adaugat (nu exista deja in multime)
		bool adauga(TElem e);
		Nod* adauga_rec(Nod* p, TElem e, Nod* prec);

		//sterge un element din multime
		//returneaza adevarat daca elementul a existat si a fost sters
		bool sterge(TElem e);
		Nod* sterge_rec(Nod* p, TElem elem);

		//returneaza nodul cu cheia minima din subarborele p;
		Nod* minim(Nod* p) const;

		//verifica daca un element se afla in multime
		bool cauta(TElem elem) const;
		bool cauta_rec(Nod* p, TElem e) const;

		//returneaza nodul cu cheia imediat mai mare decat cheia p
		Nod* succesor(Nod* p) const;

		//intoarce numarul de elemente din multime;
		int dim() const;

		//verifica daca multimea e vida;
		bool vida() const;

		//returneaza un iterator pe multime
		IteratorMultime iterator() const;

		// destructorul multimii
		~Multime();
		void delete_rec(Nod* p);

		void intersectie(const Multime& b);
};




