from random import *

cartes = [0] * 52
incr = 0
carte = 2
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
        print("AS ! 1 ou 11 pts ?")
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
    tirees[tir] = pioche
    pioche = cartes[pioche]
    return pioche

tirees = [0] * 52
tir = 0

scoreJ = 0
scoreB = 0


for loop in range(20):
    pioche = piocher()
    score = points()
    tir += 1
    scoreJ += score

print(tirees)
print(scoreJ)
