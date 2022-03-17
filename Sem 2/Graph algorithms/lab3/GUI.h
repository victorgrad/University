#pragma once

#include <QtWidgets/qapplication.h>
#include <QtWidgets/qlistwidget.h>
#include <QtWidgets/qpushbutton.h>
#include <QtWidgets/qcombobox.h>
#include <QtWidgets/qboxlayout.h>
#include <QtWidgets/qmessagebox.h>
#include <vector>
#include "serv.h"

class GUI : public QWidget
{
public:
	GUI(Service& serv);
	void Update();
	void Show() {
		this->show();
	}

private:
	Service& service;

	QListWidget* lista1;
	QListWidget* lista2;
	QPushButton* buton_modifica;
	QPushButton* buton_pierderi;
	QComboBox* combobox;

	void modifica();
	void pierderi();
};