#include "examenpracticpoo.h"
#include <QtWidgets/QApplication>
#include "gui.h"
#include "teste.h"
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    run_tests();
    Repo repo{"fis.txt"};
    Validator val;
    Service serv{ repo,val };
    Gui w{serv};
    w.show();
    return a.exec();
}
