import time
from itertools import combinations
from config import BUDGET, ACTIONS, ACTIONS_1, ACTIONS_2


def benefice(portefeuille: list) -> float:
    """
        Fonction qui retourne le bénéfice à partir d'une liste d'action (portefeuille)
    """
    return sum([action[1] * action[2] for action in portefeuille])


def depense(portefeuille: list[str, float, float]) -> float:
    """Retourne le cout d'un portefeuille d'actions"""
    return sum([a[1] for a in portefeuille])


def display(p: list[str, float, float]) -> None:
    """Ensemble des informations d'un portefeuille"""
    print(f"{20*'#'}\n Nombre d'actions : {len(p)} Coût : {depense(p)} Bénéfice : {benefice(p)} \n{20*'#'}")


def meilleur_choix(liste_actions):

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


# Initialisation du chronomètre
for act in [ACTIONS, ACTIONS_1, ACTIONS_2]:
    start = time.time()
    reponse = meilleur_choix(act)
    print(reponse)
    # calcul du temps écoulé et affichage de ce temps
    end = time.time()
    delta_time = end - start
    print(f"\nt ### Le programme c'est déroulé en {delta_time} secondes pour une jeu de {len(act)} actions ###\n")