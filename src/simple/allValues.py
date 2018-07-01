import numpy as np
import matplotlib.pyplot as plt
from recursive import probabilityRR

players = np.arange(1, 51, 1)
mafia = np.arange(1, 11, 1)

shape = (mafia.size, players.size)
values = np.zeros(shape)

for T in players:
    for M in mafia:
        values[M-1][T-1] = probabilityRR(T,M)

plt.contourf(values);

cbar = plt.colorbar(ticks=np.arange(0,1.2,0.2))
cbar.set_label("Probability")

plt.xticks(np.arange(4,50,5), np.arange(5, 51, 5))
plt.yticks(np.arange(0,10,1), np.arange(1,11,1))

plt.title("Probability that Mafia Wins")
plt.xlabel("Number of Players (T)")
plt.ylabel("Number of Mafia (M)")
plt.show()