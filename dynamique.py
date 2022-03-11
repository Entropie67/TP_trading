from config import BUDGET, ACTIONS

def recursive():
    return 0

# version 1


def dynamique1(act, poids_max=BUDGET):
    print("... Dynamique...")
    n = len(act)
    poids_max *= 100
    # On range les actions par cout croissant.
    act.sort(key=lambda x: x[1])
    valeurs = [a[1] * a[2] for a in act]
    # Conversion des points en int en multipliant par 100
    poids = [int(a[1] * 100) for a in act]
    # Création d'une matrice n ligne et poids_max colonnes
    v = [[0] * (poids_max + 1) for i in range(n)]
    for p in range(poids[0], poids_max + 1):
        v[0][p] = valeurs[0]
    for i in range(1, n):
        for p in range(poids[i]):
            v[i][p] = v[i - 1][p]
        for p in range(poids[i], poids_max + 1):
            v[i][p] = max(v[i - 1][p], valeurs[i] + v[i - 1][p - poids[i]])
    return v[n - 1][poids_max]


print(dynamique1(ACTIONS))
