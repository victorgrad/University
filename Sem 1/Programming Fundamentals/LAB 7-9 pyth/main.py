from UI.UI_consola import *
from Test.teste import *


if __name__ == '__main__':
    unittest.main(exit=False)
    catalog = CatalogFisier()
    validator = Validator()
    repos = Repos(catalog, validator)
    service = Service(repos)
    console = Consola(service)
    run(console)
