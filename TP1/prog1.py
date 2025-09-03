print("Hello, World!", "\n")

import fonctions as f

while True:
	nbr=(int, float)(input("Entree un nombre : "))
	puissance=(int, float)(input("Entree sa puissance : "))

	res = f.puissance_nombre(nbr,puissance)
	print(nbr,"**",puissance,"=", res, "\n")


