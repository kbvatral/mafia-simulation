import numpy as np

def runDay(players):
    """ Function to run the day phase of the game """
    elimOne = np.random.choice(players, len(players) -1, replace=False)
    return elimOne 