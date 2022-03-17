#include "gui.h"


Gui::Gui(Service& serv) :serv{ serv } {
	QHBoxLayout* window = new QHBoxLayout;
	this->setLayout(window);

	//stanga
	QVBoxLayout* stanga = new QVBoxLayout;
	tabel = new QTableView;
	model = new MyTableModel{ serv.get_repo() };
	tabel->setModel(model);
	stanga->addWidget(tabel);

	pretf = new QSlider{ Qt::Horizontal };
	pretf->setMinimum(1);
	pretf->setMaximum(100);
	stanga->addWidget(pretf);
	connect(pretf, &QSlider::valueChanged, this, &Gui::filtrare);

	//dreapta
	QVBoxLayout* dreapta = new QVBoxLayout;
	QFormLayout* formular = new QFormLayout;
	QLabel* id = new QLabel{ "ID:" };
	QLabel* nume = new QLabel{ "Nume:" };
	QLabel* tip = new QLabel{ "Tip:" };
	QLabel* pret = new QLabel{ "Pret:" };
	txtid = new QLineEdit;
	txtnume = new QLineEdit;
	txttip = new QLineEdit;
	txtpret = new QLineEdit;
	formular->addRow(id, txtid);
	formular->addRow(nume, txtnume);
	formular->addRow(tip, txttip);
	formular->addRow(pret, txtpret);
	dreapta->addLayout(formular);

	adauga = new QPushButton{ "Adauga" };
	dreapta->addWidget(adauga);
	connect(adauga, &QPushButton::released, this, &Gui::adaugap);

	window->addLayout(stanga);
	window->addLayout(dreapta);

	//pt ferestrele multiple
	unordered_map<string, int> dict;
	vector<Produs> vec = serv.get_repo();
	for (auto el : vec) {
		string tip = el.get_tip();
		if (dict[tip] == 0)
			dict[tip] = 1;
	}
	for (auto el : dict) {
		GenericWindow* g = new GenericWindow{ serv,el.first };
		g->show();
		g->update();
	}

}

void Gui::adaugap() {
	string id, nume, tip, pret;
	id = txtid->text().toStdString();
	nume = txtnume->text().toStdString();
	tip = txttip->text().toStdString();
	pret = txtpret->text().toStdString();
	try {
		serv.addp(id, nume, tip, pret);
		Update();
	}
	catch (const string& err) {
		QMessageBox::critical(nullptr, "Eroare", QString::fromStdString(err));
	}
}

void Gui::filtrare() {
	int val = pretf->value();
	model->set_filtru(val);
	model->setTable(serv.get_repo());
}

void Gui::Update() {
	model->setTable(serv.get_repo());
	txtid->clear();
	txtnume->clear();
	txttip->clear();
	txtpret->clear();
}