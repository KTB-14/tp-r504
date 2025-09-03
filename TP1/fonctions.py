def puissance_nombre(nbr, puissance):
    if type(nbr) not in (int, float) or type(puissance) not in (int, float):
        raise TypeError("Only integers or decimals are allowed")
    
    if nbr == 0 and puissance <= 0:
        raise ValueError("opération puissance indéfinie, puissance doit être positive")
    
    
    puissance_int = int(puissance)
    if puissance != puissance_int or puissance_int < 0:
        raise ValueError("Cette fonction supporte uniquement les puissances entières positives")
    
    calcule = 1
    for _ in range(puissance_int):
        calcule = calcule * nbr
    
    return calcule