import time
from itertools import combinations
from config import BUDGET
from utils import benefice, depense, display


def bruteforce(liste_actions):

    display(liste_actions)
    benefice_max = [-1, []]
    for i in range(1, len(liste_actions)):
        # On va prendre toutes les combinaisons de i éléments de la liste
        combinaison = combinations(liste_actions, i)
        for portefeuille in combinaison:
            if depense(portefeuille) <= BUDGET:
                gain = benefice(portefeuille)
                if gain > benefice_max[0]:
                    benefice_max[0] = gain
                    benefice_max[1] = portefeuille
    return benefice_max


