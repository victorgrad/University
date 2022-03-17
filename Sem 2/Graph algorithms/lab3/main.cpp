#include "Simulare.h"
#include "teste.h"
#include "GUI.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    run_tests();
    Repository repo{"in.txt"};
    Service serv{ repo };
    GUI fereastra{ serv };
    fereastra.show();
    fereastra.Update();
    return a.exec();
}
