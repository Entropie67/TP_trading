import csv
import time

# Initialisation du chronomètre
start = time.time()

# Lecture du csv
with open('data/liste_actions.csv', newline='') as datafile:
    actions = list(csv.reader(datafile, delimiter=',', quotechar='|'))[1:]


print(actions)






# calcul du temps écoulé et affichage de ce temps
end = time.time()
delta_time = end - start
print(f"\n\n\t ### Le programme c'est déroulé en {delta_time} secondes ###\n")