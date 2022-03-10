import csv


BUDGET = 500
FICHIERS = ['data/liste_actions.csv', 'data/dataset1_Python.csv', 'data/dataset2_Python.csv']


def lecture(fichier: str) -> list:
    """
        fonction qui va lire dans  un fichier csv et retourne une liste d'action
    """
    with open(fichier, newline='') as datafile:
        actions = list(csv.reader(datafile, delimiter=',', quotechar='|'))[1:]
    actions = [[a[0], float(a[1]), float(a[2][:-1])/100] for a in actions]
    return actions


ACTIONS = lecture(FICHIERS[0])
ACTIONS_1 = lecture(FICHIERS[1])
ACTIONS_2 = lecture(FICHIERS[2])