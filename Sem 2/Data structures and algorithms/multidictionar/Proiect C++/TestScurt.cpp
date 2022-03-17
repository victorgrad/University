#include "TestScurt.h"
#include "MD.h"
#include "IteratorMD.h"
#include <assert.h>
#include <vector>
#include <iostream>

void testmeu() {
	MD m;
	for (int i = 0; i < 2; i++) {
		m.adauga(i, i);
	}
	assert(m.vid() == false);
	for (int i = -1; i < 3; i++) { //mai adaugam elemente [-1, 3), acum anumite elemente [0, 2) sunt de 2 ori
		m.adauga(i, 2 * i);
	}
	assert(m.vid() == false);
	for (int i = -2; i < 4; i++) { //mai adaugam elemente [-2, 4), acum anumite elemente [0, 2) sunt de 3 ori, altele [-1, 0), si [2, 3) sunt de 2 ori
		m.adauga(i, 3 * i);
	}
	assert(m.vid() == false);
	for (int i = -3; i < 5; i++) { //numaram de cate ori apar anumite elemente (inclusiv elemente inexistente)
		vector<TValoare> v;
		if (i < -2) {
			v = m.cauta(i);
			assert(v.size() == 0);
		}
		else if (i < -1) {
			v = m.cauta(i);
			assert(v.size() == 1);
		}
		else if (i < 0) {
			v = m.cauta(i);
			assert(v.size() == 2);
		}
		else if (i < 2) {
			v = m.cauta(i);
			assert(v.size() == 3);
		}
		else if (i < 3) {
			v = m.cauta(i);
			assert(v.size() == 2);
		}
		else if (i < 4) {
			v = m.cauta(i);
			assert(v.size() == 1);
		}
		else {
			v = m.cauta(i);
			assert(v.size() == 0);
		}
	}
}

void testAll() {
	//testmeu();
	MD m;
	m.adauga(1, 100);
	m.adauga(2, 200);
	m.adauga(3, 300);
	m.adauga(1, 500);
	m.adauga(2, 600);
	m.adauga(4, 800);

	assert(m.dim() == 6);

	assert(m.sterge(5, 600) == false);
	assert(m.sterge(1, 500) == true);

	assert(m.dim() == 5);

    vector<TValoare> v;
	v=m.cauta(6);
	assert(v.size()==0);

	v=m.cauta(1);
	assert(v.size()==1);

	assert(m.vid() == false);

	IteratorMD im = m.iterator();
	assert(im.valid() == true);
	while (im.valid()) {
		im.element();
		im.urmator();
	}
	assert(im.valid() == false);
	im.prim();
	assert(im.valid() == true);

}
