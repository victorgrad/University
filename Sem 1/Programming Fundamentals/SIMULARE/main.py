from UI.ui_consola import *
from TEST.teste import *

if __name__ == '__main__':
    repository = Repository()
    service = Service(repository)
    consola = Consola(service)
    run_all_tests()
    run(consola)