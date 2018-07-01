""" 
Code to run a simulation of the simple version of the game (mafia and townsfolk only).
This code is ported from MATLAB code developed while I was taking MA499 Game Theory at Eastern Nazarene College
""" 
import numpy as np
import math
from day import runDay
from night import runNight

def checkCitizenWin(mafia):
    if mafia.size == 0:
        return True
    return False
def checkMafiaWin(mafia, citizens):
    if mafia.size >= citizens.size:
        return True
    return False

def runGame(num_players, num_mafia):
    # Number of players
    n = num_players
    players = np.arange(0,n,1)

    # Number of mafia
    n_mafia = num_mafia
    mafia = np.random.permutation(players)[:n_mafia]

    # Number of citizens
    n_citizens = n - n_mafia
    citizens = np.setdiff1d(players, mafia)

    win = False
    while not win:
        # Day and Night Phases
        players = runNight(players, citizens)
        players = runDay(players)

        # Update arrays after phases
        citizens = np.setdiff1d(players, mafia)
        mafia = np.setdiff1d(players, citizens)

        if checkCitizenWin(mafia):
            print("The citizens won")
            win = True
        elif checkMafiaWin(mafia, citizens):
            print("The mafia won")
            win = True

runGame(6, 1)
