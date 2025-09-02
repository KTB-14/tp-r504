def puissance_nombre(nbr,puissance):
    if type(nbr) is not int or type(puissance) is not int:
        raise TypeError("Only integers are allowed")
    calcule= nbr ** puissance
    return calcule