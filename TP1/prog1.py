print("Hello, World!", "\n")

import fonctions as f

while True:
	nbr=float(input("Entree un nombre : "))
	puissance=float(input("Entree sa puissance : "))

	res = f.puissance_nombre(nbr,puissance)
	print(nbr,"**",puissance,"=", res, "\n")


