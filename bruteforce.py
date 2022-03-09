import csv
import time
from itertools import combinations

# Initialisation du chronomètre
start = time.time()
BUDGET = 500
FICHIER = 'data/liste_actions.csv'


def lecture(fichier: list[str]) -> list[str, float, float]:
    """
        fonction qui va lire dans  un fichier csv et retourne une liste d'action
    """
    with open(fichier, newline='') as datafile:
        actions = list(csv.reader(datafile, delimiter=',', quotechar='|'))[1:]
    actions = [[a[0], float(a[1]), float(a[2][:-1])/100] for a in actions]
    return actions

def benefice(portefeuille: list[str, float, float]) -> float:
    """
        Fontion qui retourne le bénéfice à partir d'une liste d'action (portefeuille)
    """
    s = 0
    for action in portefeuille:
        s += action[1] * action[2]
    return s

def depense(portefeuille: list[str, float, float]) -> float:
    return sum([a[1] for a in portefeuille])

def display(p: list[str, float, float]) -> None:
    """
        Ensemble des informations d'un portefeuille
    """
    print(20*"#")
    print(f"Nombre d'actions : {len(p)} Coût : {depense(p)} Bénéfice : {benefice(p)}")
    print(20 * "#")

b = lecture(FICHIER)

display(b)
portefeuilles = []
for i in range(1, len(b)):

    a = combinations(b, i)
    for l in a:
        if depense(l) <= 500:
            portefeuilles.append((benefice(l), l))
print(f" {len(portefeuilles)} portefeuilles sont valides")
p = max(portefeuilles, key= lambda x: x[0])
display(p[1])
print(p)



# calcul du temps écoulé et affichage de ce temps
end = time.time()
delta_time = end - start
print(f"\n\n\t ### Le programme c'est déroulé en {delta_time} secondes ###\n")