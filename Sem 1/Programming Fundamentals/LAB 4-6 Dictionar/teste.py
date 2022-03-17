from functii import *


def test_add_lista():
    listat = []
    add_lista(listat, 1, 2)
    add_lista(listat, 3, 4)
    add_lista(listat, 3, 6)
    add_lista(listat, 1, -90)
    assert listat == [{'real': 1, 'imag': 2}, {'real': 3, 'imag': 4}, {'real': 3, 'imag': 6}, {'real': 1, 'imag': -90}]


def test_elimin_prim():
    """
    Functia test_elimin_prim testeaza functia elimin_prim din cadrul filtrarii
    :return:
    """
    assert elimin_prim([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 6}, {'real': 4, 'imag': 3}, {'real': 7, 'imag': 13}]) == [{'real': 1, 'imag': 3}, {'real': 6, 'imag': 6}, {'real': 4, 'imag': 3}]
    assert elimin_prim([{'real': 2, 'imag': 5}, {'real': 2, 'imag': 3}, {'real': 2, 'imag': 1}, {'real': 2, 'imag': 7}, {'real': 2, 'imag': 8}, {'real': 2, 'imag': 9}]) == []
    assert elimin_prim([{'real': 6, 'imag': 5}, {'real': 6, 'imag': 3}, {'real': 6, 'imag': 1}, {'real': 6, 'imag': 7}, {'real': 6, 'imag': 8}, {'real': 6, 'imag': 9}]) == [{'real': 6, 'imag': 5}, {'real': 6, 'imag': 3}, {'real': 6, 'imag': 1}, {'real': 6, 'imag': 7}, {'real': 6, 'imag': 8}, {'real': 6, 'imag': 9}]


def test_sterge_el():
    """
    Functia test_sterge_el testeaza functia sterge_el din cadrul modificarii listei
    :return:
    """
    assert sterge_el([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 6}, {'real': 4, 'imag': 3}, {'real': 7, 'imag': 13}], 1, 2) == [{'real': 1, 'imag': 3}, {'real': 6, 'imag': 6}, {'real': 4, 'imag': 3}, {'real': 7, 'imag': 13}]
    assert sterge_el([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 6}, {'real': 4, 'imag': 3}, {'real': 7, 'imag': 13}], 0, 5) == []
    assert sterge_el([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 6}, {'real': 4, 'imag': 3}, {'real': 7, 'imag': 13}], 1, 5) == [{'real': 1, 'imag': 3}]


def test_inlocuire_el():
    """
    Functia test_inlocuire_el testeaza functia inlocuire_el din cadrul modificarii listei
    :return:
    """
    assert inlocuire_el([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 6}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}], {'real': 1, 'imag': 3}, {'real': 6, 'imag': 9}) == [{'real': 6, 'imag': 9}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 6}, {'real': 6, 'imag': 9}, {'real': 7, 'imag': 13}]
    assert inlocuire_el([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 6}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}], {'real': 1, 'imag': 1}, {'real': 0, 'imag': 0}) == [{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 6}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}]
    assert inlocuire_el([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 6}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}], {'real': 7, 'imag': 13}, {'real': 0, 'imag': 4}) == [{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 6}, {'real': 1, 'imag': 3}, {'real': 0, 'imag': 4}]


def test_comparare():
    """
    Functia test_comparare testeaza functia comparare din cadrul filtrarii listei
    :return:
    """
    assert comparare([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 8}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}], '<', 5) == [{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 1, 'imag': 3}]
    assert comparare([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 8}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}], '=', 10) == [{'real': 6, 'imag': 8}]
    assert comparare([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 8}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}], '>', 5) == [{'real': 3, 'imag': 5}, {'real': 6, 'imag': 8}, {'real': 7, 'imag': 13}]


def test_suma_sub():
    """
    Functia test_suma_sub testeaza corectitudinea functiei suma_sub din cadrul operatiilor cu lista
    :return:
    """
    assert suma_sub([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 8}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}], 1, 2) == {'real': 5, 'imag': 9}
    assert suma_sub([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 8}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}], 1, 4) == {'real': 12, 'imag': 20}
    assert suma_sub([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 8}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}], 5, 5) == {'real': 7, 'imag': 13}


def test_prod_sub():
    """
    Functia test_suma_sub testeaza corectitudinea functiei suma_sub din cadrul operatiilor cu lista
    :return:
    """
    assert prod_sub([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 8}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}], 1, 2) == {'real': -14, 'imag': 22}
    assert prod_sub([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 8}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}], 1, 4) == {'real': -320, 'imag': -760}
    assert prod_sub([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 8}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}], 3, 3) == {'real': 6, 'imag': 8}


def test_sortd_lista():
    """
    Functia test_sortd_lista testeaza corectitudinea sortd_lista
    :return:
    """
    assert sortd_lista([{'real': 1, 'imag': 3}, {'real': 2, 'imag': 4}, {'real': 3, 'imag': 5}, {'real': 6, 'imag': 8}, {'real': 1, 'imag': 3}, {'real': 7, 'imag': 13}]) == ([{'real': 7, 'imag': 13}, {'real': 6, 'imag': 8}, {'real': 3, 'imag': 5}, {'real': 2, 'imag': 4}, {'real': 1, 'imag': 3}, {'real': 1, 'imag': 3}])
    assert sortd_lista([{'real': 1, 'imag': 2}, {'real': 2, 'imag': 33}]) == ([{'real': 2, 'imag': 33}, {'real': 1, 'imag': 2}])
    assert sortd_lista([{'real': 1, 'imag': 2}, {'real': 2, 'imag': -33}]) == ([{'real': 1, 'imag': 2}, {'real': 2, 'imag': -33}])


def run_tests():
    """
    Functia run_tests ruleaza toate testele
    :return:
    """
    test_add_lista()
    test_elimin_prim()
    test_sterge_el()
    test_inlocuire_el()
    test_comparare()
    test_suma_sub()
    test_prod_sub()
    test_sortd_lista()

