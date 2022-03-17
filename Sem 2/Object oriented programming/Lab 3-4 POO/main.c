#include <stdio.h>
#include "UI.h"
#include "teste.h"
#include "vectordinamic.h"
#include "SERVICE.h"
#include <crtdbg.h>

int main() {
	run_tests();
	VectorDinamic* cheltuieli = creazaVectorDinamic();
	Service* service = creeazaService(cheltuieli);
	UI* ui = creeazaUi(service);
	run_app(ui);
	distrugeUi(ui);
	_CrtDumpMemoryLeaks();
	return 0;
}
