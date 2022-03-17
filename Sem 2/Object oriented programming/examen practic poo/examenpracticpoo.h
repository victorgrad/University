#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_examenpracticpoo.h"

class examenpracticpoo : public QMainWindow
{
    Q_OBJECT

public:
    examenpracticpoo(QWidget *parent = Q_NULLPTR);

private:
    Ui::examenpracticpooClass ui;
};
