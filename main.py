import time
from config import ACTIONS, ACTIONS_1, ACTIONS_2
from bruteforce import bruteforce
from optimized import glouton
from dynamique import dynamique1
from utils import display


for act in [ACTIONS, ACTIONS_1, ACTIONS_2]:
    start = time.time()
    print('--' * 20)
    print(" JEUX de DONNEES ")
    display(act)
    print('--' * 20)
    start = time.time()
    benef = glouton(act)
    end = time.time()
    delta_time = end - start
    print(f"\n\t ### GLOUTON ###\n temps: {delta_time} Bénéfice: {benef}€ \n")

for act in [ACTIONS, ACTIONS_1, ACTIONS_2]:
    start = time.time()
    print('--' * 20)
    print(" JEUX de DONNEES ")
    display(act)
    print('--' * 20)
    reponse = dynamique1(act)
    end = time.time()
    delta_time = end - start
    print(f"\n\t ### DYNAMIQUE ###\n temps: {delta_time} Bénéfice: {reponse}€ \n")

for act in [ACTIONS, ACTIONS_1, ACTIONS_2]:
    start = time.time()
    print('--' * 20)
    print(" JEUX de DONNEES ")
    display(act)
    print('--' * 20)
    reponse = bruteforce(act)
    end = time.time()
    delta_time = end - start
    print(f"\n\t ### BRUTE FORCE ###\n temps: {delta_time} Bénéfice: {reponse[0]}€ \n")
