def puissance_nombre(nbr, puissance):
    if type(nbr) not in (int, float) or type(puissance) not in (int, float):
        raise TypeError("Only integers or decimals are allowed")

    if nbr == 0 and puissance <= 0:
        raise ValueError("opération puissance indéfinie, puissance doit être positive")

    return nbr ** puissance
