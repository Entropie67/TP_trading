from config import BUDGET, ACTIONS

def recursive():
    return 0

# version 1
def dynamique1(act, poids_max=BUDGET):
    n = len(act)
    # On range les actions par cout croissant.
    act.sort(key=lambda x: x[1])
    valeurs = [a[1] * a[2] for a in act]
    # Conversion des points en int en multipliant par 100
    poids = [int(a[2] * 100) for a in act]

    # Création d'une matrice n ligne et poids_max colonnes
    v = [[0] * (poids_max + 1) for i in range(n)]
    print(act)
    print(poids)

dynamique1(ACTIONS)
