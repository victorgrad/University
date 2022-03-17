#include "GUI.h"

GUI::GUI(Service& serv) :service{ serv } {
	QHBoxLayout* Window = new QHBoxLayout;
	this->setLayout(Window);

	lista1 = new QListWidget;
	lista2 = new QListWidget;

	Window->addWidget(lista1);

	QVBoxLayout* layout_mij = new QVBoxLayout;

	combobox = new QComboBox;
	combobox->addItem("Reducere x2");
	combobox->addItem("Reducere x3");
	combobox->addItem("Reducere x5");

	layout_mij->addWidget(combobox);
	buton_modifica = new QPushButton{ "Modifica" };
	buton_pierderi = new QPushButton{ "Calculeaza Pierderi" };
	connect(buton_modifica, &QPushButton::released, this, &GUI::modifica);
	connect(buton_pierderi, &QPushButton::released, this, &GUI::pierderi);
	layout_mij->addWidget(buton_modifica);
	layout_mij->addWidget(buton_pierderi);


	Window->addWidget(lista1);
	Window->addLayout(layout_mij);
	Window->addWidget(lista2);
}

void GUI::Update() {
	std::vector<Proiect> proiecte = service.get_all();
	lista1->clear();
	lista2->clear();
	for (const Proiect& pr : proiecte) {
		std::string desc;
		desc += pr.get_nume();
		desc += " ";
		desc += std::to_string(pr.get_buget_alocat());
		desc += " ";
		desc += std::to_string(pr.get_buget_estimat());
		QString nume(pr.get_nume().c_str());
		QVariant nume_data(nume);
		QListWidgetItem* item= new QListWidgetItem(QString::fromUtf8(desc.c_str()));
		item->setData(Qt::UserRole, nume_data);
		if (pr.get_buget_estimat() > pr.get_buget_alocat()) {
			QListWidgetItem* new_item = new QListWidgetItem(QString::fromUtf8(desc.c_str()));
			if (pr.get_tip().compare("modern") == 0) {
				new_item->setBackground(Qt::magenta);
			}
			lista2->addItem(new_item);
		}
		lista1->addItem(item);
	}
}

void GUI::modifica() {
	int index = combobox->currentIndex();
	//QListWidgetItem selected = *lista1->currentItem();
	QVariant data = lista1->currentItem()->data(Qt::UserRole);
	QString nume = data.toString();
	std::string nume_std = nume.toUtf8().constData();
	for (Proiect& pr : service.get_all()) {
		if (pr.get_nume().compare(nume_std) == 0) {
			if (index == 0) {
				pr.set_buget_alocat(pr.get_buget_alocat() / 2);
			}
			else if (index == 1) {
				pr.set_buget_alocat(pr.get_buget_alocat() / 3);
			}
			else if (index == 2) {
				pr.set_buget_alocat(pr.get_buget_alocat() / 5);
			}
		}
	}
	Update();
}

void GUI::pierderi() {
	float pierderi = service.get_pierderi();
	QString pierdere = QString::number(pierderi);
	QString titlu("Pierderi");
	QMessageBox* mesaj = new QMessageBox;
	mesaj->setText(pierdere);
	mesaj->setWindowTitle(titlu);
	mesaj->show();
}