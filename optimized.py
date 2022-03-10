import time
from config import BUDGET, ACTIONS, ACTIONS_1, ACTIONS_2
from utils import display
################################
#          Algo Glouton        #
################################


def tri_rentabilite(actions):
    act = actions.copy()
    act.sort(key=lambda x: x[2], reverse=True)
    return act



def glouton(actions):
    print("..... glouton ....")
    actions_triees = tri_rentabilite(actions)
    total = 0
    benefice = 0
    portefeuille = []
    for action in actions_triees:
        if action[1] + total <= 500:
            total += action[1]
            portefeuille.append(action)
            benefice += action[1] * action[2]
        if total == 500:
            return benefice
    return benefice








#######################################
#      Programmation dynamique        #
#######################################