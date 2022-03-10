import csv


BUDGET = 500
FICHIER = 'data/liste_actions.csv'


def lecture(fichier: str) -> list:
    """
        fonction qui va lire dans  un fichier csv et retourne une liste d'action
    """
    with open(fichier, newline='') as datafile:
        actions = list(csv.reader(datafile, delimiter=',', quotechar='|'))[1:]
    actions = [[a[0], float(a[1]), float(a[2][:-1])/100] for a in actions]
    return actions


ACTIONS = lecture(FICHIER)