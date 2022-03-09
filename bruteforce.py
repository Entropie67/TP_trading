import csv
import time

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

b = lecture(FICHIER)
print(benefice(b))





# calcul du temps écoulé et affichage de ce temps
end = time.time()
delta_time = end - start
print(f"\n\n\t ### Le programme c'est déroulé en {delta_time} secondes ###\n")