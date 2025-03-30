# Library
import random
import time
import os

# Tableau
def jdlv():
	print("Bienvenue dans le Jeu de la vie façon Antoine")
	choix = input("Choisissez un nombre pour commencer la génération : ")
	cycle = input("Choisissez le nombre de cycle que vous souhaitez : ")
	if choix.isdigit():
		grille = int(choix)
		ndc = int(cycle)
		tableau = []
		print(f"Création d'une grille {grille}x{grille}")
		for x in range(grille):
			ligne = []
			for y in range(grille):
				valeur = str(random.randint(0, 1))
				ligne.append(valeur)
			tableau.append(ligne)				
		return tableau	
	else:
		print("Veuillez entrer un nombre valide.")
		return jdlv()

def afficher_grille(tableau):
	for ligne in tableau:
		print("".join("█" if c == "1" else "." for c in ligne))


# Calcul
def compter_voisines(x, y, tableau):
	compteur = 0
	for dx in [-1, 0, 1]:
		for dy in [-1, 0, 1]:
			if dx == 0 and dy == 0 :
				continue
			nx = x + dx
			ny = y + dy
			if 0 <= nx < len(tableau) and 0 <= ny < len(tableau[0]):
				if tableau[nx][ny] == "1":
					compteur += 1
	return compteur

def new_generation(tableau):
	new_tableau = []
	for x in range(len(tableau)): 
		ligne = []
		for y in range(len(tableau[0])):
			voisines = compter_voisines(x, y, tableau)
			cellule = tableau[x][y]
			if cellule == "1":
				if voisines == 2 or voisines == 3:
					ligne.append("1")
				else:
					ligne.append("0")
			else:
				if voisines == 3:
					ligne.append("1")
				else:
					ligne.append("0")
		new_tableau.append(ligne)
	return new_tableau

tableau = jdlv()

for generation in range(ndc):
    print(f"Cycle {generation + 1} / {ndc}")
    afficher_grille(tableau)
    grille = new_generation(tableau)
    time.sleep(1)