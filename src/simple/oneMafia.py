import numpy as np
import matplotlib.pyplot as plt
from recursive import probabilityRR

players = np.arange(1, 11, 1)
values = []

for T in players:
    values.append(probabilityRR(T,1))

plt.plot(players, values);
plt.title("Probability that 1 Mafia Member Wins")
plt.xlabel("Number of Players (T)")
plt.ylabel("Probability")
plt.show()