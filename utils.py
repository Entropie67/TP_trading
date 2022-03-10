import csv

def lecture(fichier: str) -> list:
    """
        fonction qui va lire dans  un fichier csv et retourne une liste d'action
    """
    with open(fichier, newline='') as datafile:
        actions = list(csv.reader(datafile, delimiter=',', quotechar='|'))[1:]
    actions = [[a[0], float(a[1]), float(a[2][:-1])/100] for a in actions]
    return actions


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
    print(f"\n Nombre d'actions : {len(p)} Coût total : {depense(p)} \n")
