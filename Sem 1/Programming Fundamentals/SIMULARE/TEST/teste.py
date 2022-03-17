from UI.ui_consola import *

def run_all_tests():
    test_creare_comanda()
    test_creare_rata()
    test_comenzi_cu_str()
    test_rata()
    test_rata_ex()

def test_creare_comanda():
    cmd = Comanda(1234, "BIll McCoy", "smecherie", 9999)
    assert cmd.get_id() == 1234
    assert cmd.get_valoare() == 9999
    assert cmd.get_tip_produs() == "smecherie"
    assert cmd.get_nume_client() == "BIll McCoy"

def test_creare_rata():
    cmd = Comanda(1234, "BIll McCoy", "smecherie", 70)
    rata = Rata(cmd, 10)
    assert rata.get_tip_produs() == "smecherie"
    assert rata.get_nume_client() == "BIll McCoy"
    assert rata.get_rata() == 7.0

def test_comenzi_cu_str():
    cmd = Comanda(1234, "BIll McCoy", "smecherie", 70)
    repository = Repository()
    service = Service(repository)
    service.repository.comenzi[cmd.get_id()] = cmd
    assert service.comenzi_cu_str("sme") == [cmd]
    assert service.comenzi_cu_str("uau") == []

def test_rata():
    cmd = Comanda(1234, "BIll McCoy", "smecherie", 70)
    repository = Repository()
    service = Service(repository)
    service.repository.comenzi[cmd.get_id()] = cmd
    assert service.rata(1234, 10) == ("BIll McCoy", "smecherie", 7.0)

def test_rata_ex():
    cmd = Comanda(1234, "BIll McCoy", "smecherie", 70)
    repository = Repository()
    service = Service(repository)
    service.repository.comenzi[cmd.get_id()] = cmd
    try:
        obj = service.rata(123, 10)
        assert False
    except:
        assert True
