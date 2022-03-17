#pragma once
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qtableview.h>
#include <QtWidgets/qboxlayout.h>
#include <QAbstractTableModel>
#include <QtWidgets/qformlayout.h>
#include <QtWidgets/qlabel.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qpushbutton.h>
#include <unordered_map>
#include <QtWidgets/qheaderview.h>
#include <qmessagebox.h>
#include <qstandarditemmodel.h>
#include <qslider.h>
#include "serv.h"

class GenericWindow :public QWidget, public Observer {
private:
	QLabel* nrel = new QLabel;
	string tip;
	Service& serv;
	QVBoxLayout* l = new QVBoxLayout;
public:
	GenericWindow(Service& sr, string tip) :serv{ sr }, tip{ tip }{
		sr.add_obs(this);
		setWindowTitle(QString::fromStdString(tip));
		setLayout(l);
		l->addWidget(nrel);
	}

	void update() override {
		vector<Produs> vec = serv.get_repo();
		int nr = 0;
		for (auto prod : vec) {
			if (prod.get_tip() == tip)
				nr++;
		}
		nrel->setText(QString::number(nr));
	}
};

class MyTableModel : public QAbstractTableModel {
private:
	vector<Produs> lista;
	int filtru = -1;

public:
	MyTableModel(const vector<Produs>& lis) :lista{ lis } {};

	//Metoda returneaza numarul de linii din tabelul nostru
	int rowCount(const QModelIndex& parent = QModelIndex()) const override {
		return lista.size();
	}

	//Metoda returneaza numarul de coloane din tabelul nostru
	int columnCount(const QModelIndex& parent = QModelIndex()) const override {
		return 5;
	}

	//Metoda care seteaza filtrul pentru colorare
	void set_filtru(const int& val) { 
		filtru = val;
	}

	//Metoda returneaza date despre casutele vizibile de pe tabel
	QVariant data(const QModelIndex& index, int role) const override {
		int linie = index.row();
		int col = index.column();
		if (role == Qt::DisplayRole) {
			Produs p = lista.at(linie);
			if (col == 0) {//id
				return QString::number(p.get_id());
			}
			if (col == 1) {//nume
				return QString::fromStdString(p.get_nume());
			}
			if (col == 2) {//tip
				return QString::fromStdString(p.get_tip());
			}
			if (col == 3) {//pret
				return QString::number(p.get_pret());
			}
			if (col == 4) {//vocale
				string nume = p.get_nume();
				int voc = 0;
				for (int i = 0; i < nume.length(); i++) {
					if (nume[i] == 'a' || nume[i] == 'e' || nume[i] == 'i' || nume[i] == 'o' || nume[i] == 'u' || nume[i] == 'A' || nume[i] == 'E' || nume[i] == 'I' || nume[i] == 'O' || nume[i] == 'U')
						voc++;
				}
				return QString::number(voc);
			}
		}
		if (role == Qt::BackgroundRole) {
			Produs p = lista.at(linie);
			if (p.get_pret() <= filtru)
				return QBrush(Qt::red);
			else
				return QBrush(Qt::white);
		}
		return QVariant();
	}

	//Metoda apelata in cazul modificarii de date
	void setTable(vector<Produs> lis) {
		beginResetModel();
		lista = lis;
		QModelIndex topLeft = createIndex(0, 0);
		QModelIndex bottomRight = createIndex(rowCount(), columnCount());
		emit dataChanged(topLeft, bottomRight);
		endResetModel();
	}
};


class Gui :public QWidget {
private:
	Service& serv;
	QTableView* tabel;
	MyTableModel* model;

	QLineEdit* txtid;
	QLineEdit* txtnume;
	QLineEdit* txttip;
	QLineEdit* txtpret;
	
	QSlider* pretf;
	QPushButton* adauga;

	//metoda care updateaza ui-ul cu cele mai noi date
	//Postconditii: Tabel actualizat si casute de scriere goale
	void Update();

	//metoda preia date din campurile ui-ului si adauga produsul corespunzator in repo
	//Preconditii: date din qlineedit valide
	//Postconditii: produs adaugat in repo
	void adaugap();

	//metoda apelata la schimbarea valorii din slider care preia valoarea sliderului si actualizeaza tabelul corespunzator
	//Postconditii: tabel actualizat cu culorile corespunzatoare
	void filtrare();
public:
	Gui(Service& serv);
};