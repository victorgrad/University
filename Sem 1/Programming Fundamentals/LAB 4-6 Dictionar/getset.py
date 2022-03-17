def get_real(a):
    return a["real"]


def get_imag(a):
    return a["imag"]


def set_real(a, b):
    """
    Seteaza partea reala a numarului complex a la b
    :param a:
    :param b:
    :return z:
    """
    c = a["imag"]
    z = {
        "real": b,
        "imag": c
            }
    return z


def set_imag(a, b):
    """
    Seteaza partea imaginara a numarului complex a la b
    :param a:
    :param b:
    :return z:
    """
    c = a["real"]
    z = {
        "real": c,
        "imag": b
    }
    return z
