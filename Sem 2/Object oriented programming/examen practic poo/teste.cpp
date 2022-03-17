#include "teste.h"
#include "serv.h"


void test_obj() {
	Produs p{ 5,"Nume","tip",116.3 };
	assert(p.get_id() == 5);
	assert(p.get_nume() == "Nume");
	assert(p.get_pret() == 116.3);
	assert(p.get_tip() == "tip");
}

void test_add_order() {
	ofstream out("test.txt", ofstream::trunc);
	out.close();
	Repo repo{ "test.txt" };
	Validator val;
	Service serv{ repo,val };
	Produs p{ 5,"Nume","tip",116.3 };
	repo.addp(p);
	assert(repo.get_repo().size() == 1);
	assert(repo.get_repo()[0].get_id() == 5);
	serv.addp("6", "Nume", "Tipul", "12.3");
	assert(repo.get_repo().size() == 2);
	assert(repo.get_repo()[1].get_id() == 5);
	assert(repo.get_repo()[0].get_id() == 6);
	try {
		serv.addp("6", "Nume", "Tipul", "12.3");
		assert(false);
	}
	catch (const string& err) {}
	try {
		serv.addp("7", "", "Tipul", "12.3");
		assert(false);
	}
	catch (const string& err) {}
	try {
		serv.addp("7", "Nume", "Tipul", "0.5");
		assert(false);
	}
	catch (const string& err) {}
	try {
		serv.addp("7", "Nume", "Tipul", "100.5");
		assert(false);
	}
	catch (const string& err) {}
}


void run_tests() {
	test_obj();
	test_add_order();
}