from random import *
import sys

# Code pour jouer avec un jeu unique sans piocher les mêmes cartes

"""cartes = [0] * 52
incr = 0
carte = 2
tirees = []
for loop in range(13):
    for boucle in range(4):
        cartes[incr] = carte
        incr += 1
    carte += 1


def points():
    if pioche > 10 and pioche < 14:
        score = 10
        return score
    elif pioche == 14:
        print("Tu dois choisir la valeur de ton AS, 1 ou 11 ?")
        score = int(input())
        while score != 1 and score != 11:
            print("Tu dois choisir entre 1 ou 11.")
            score = int(input())
        return score
    else:
        score = pioche
        return score

def piocher():
    pioche = randint(0, 51)
    while pioche in tirees:
        pioche = randint(0, 51)
    tirees.append(pioche)
    pioche = cartes[pioche]
    return pioche"""

mainJoueur = []
mainBanque= []

arret = "OK"

# Fonctions

def piocher():
	pioche = randint(2, 14)
	if pioche == 11:
		return "valet"
	elif pioche == 12:
		return "dame"
	elif pioche == 13:
		return "roi"
	elif pioche == 14:
		return "AS"
	else:
		return str(pioche)

def mainJ():
	return ", ".join(mainJoueur)

def mainB():
	return ", ".join(mainBanque)
	
def piocheJ():
	mainJoueur.append(piocher())
	return print("Vous avez pioché : ", mainJoueur[-1])
	

def choix():
	print("Que voulez-vous faire ?")
	print("Pour voir les mains : 1")
	print("Pour tirer une carte : 2")
	print("Pour arrêter : 3")
	x = input()
	if x == "1":
		return print("Vous avez : ", mainJ()," et la banque a un ", mainBanque[0])
	elif x == "2":
		return piocheJ()
	elif x == "3":
		return "Nope"
		
def scoreSimple(main):
	score = 0
	for x in main:
		if x == "valet" or x == "dame" or x == "roi":
			score += 10
		elif x == "AS":
			score += 1
		else:
			score += int(x)
	return score
		
def score(main):
	score = 0
	for x in main:
		if x == "valet" or x == "dame" or x == "roi":
			score += 10
		elif x == "AS":
			print("Choisissez la valeur de l'AS : 1 ou 11 ?'")
			AS = int(input())
			while AS != 1 and AS != 11:
				print("La valeur doit être de 1 ou 11.")
				AS = int(input())
			score += AS
		else:
			score += int(x)
	return score
			
def scoreBanque(main):
	score = 0
	for x in main:
		if x == "valet" or x == "dame" or x == "roi":
			score += 10
		elif x == "AS":
			if score + 11 <= 21:
				score += 11
			else:
				score += 1
		else:
			score += int(x)
	return score
	
#Début du jeu
		

print("Début de la partie")
print()
print("Distribution des cartes")
print()

for loop in range(2):
	mainJoueur.append(piocher())
	mainBanque.append(piocher())

print("Vous avez pioché :", mainJ(), " et la banque a", mainBanque[0])
print()

# Partie joueur

while arret != "Nope":
	print()
	arret = choix()	
	scoreJ = scoreSimple(mainJoueur)
	if scoreJ > 21:
		print()
		print("Votre score est de ", scoreJ,", vous avez perdu...")
		sys.exit()
scoreJ = score(mainJoueur)
if scoreJ > 21:
		print()
		print("Votre score est de ", scoreJ,", vous avez perdu...")
		sys.exit()

# Partie banque

scoreB = scoreBanque(mainBanque)
while scoreB < 17:
	mainBanque.append(piocher())
	scoreB = scoreBanque(mainBanque)
if scoreB > 21:
	print("La banque a ", mainB(), "pour un score total de ", scoreB, ", vous avez gagné !")
	sys.exit()

print()	
if scoreJ > scoreB:
	print("Vous avez gagné !")
	print("Vous avez ", mainJ(), " pour un score de ", scoreJ)
	print("La banque a ", mainB(), "pour un score de ", scoreB)
elif scoreJ < scoreB:
	print("Vous avez perdu...")
	print("Vous avez ", mainJ(), " pour un score de ", scoreJ)
	print("La banque a ", mainB(), "pour un score de ", scoreB)
else:
	print("Egalité.")
	print("Vous avez ", mainJ(), " pour un score de ", scoreJ)
	print("La banque a ", mainB(), "pour un score de ", scoreB)
