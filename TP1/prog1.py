print("Hello, World!", "\n")

import fonctions as f

while True:
	nbr=int(input("Entree un nombre : "))
	puissance=int(input("Entree sa puissance : "))

	res = f.puissance_nombre(nbr,puissance)
	print(nbr,"**",puissance,"=", res, "\n")