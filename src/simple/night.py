import numpy as np

def runNight(players, citizens):
    """ Function to run the day phase of the game """
    toRemove = np.random.choice(citizens)
    elimOne = np.setdiff1d(players, toRemove)
    return elimOne