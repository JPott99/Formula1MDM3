import numpy as np
import matplotlib.pyplot as plt
a = 0
b = 0
c = 0
d = 0.45
f = 0
g = 0
k = 0.08
P = 14
t_b = 74
GEA = []
lA = []
l_maxI = range(1,100)
for l_max in l_maxI:
    l = np.array(range(0,l_max))
    GE = (a*np.sum(l**2) + (b+k)*np.sum(l) + f*np.sum(np.exp(g*l)) + c*np.sum(np.sqrt(l)) + P)/l_max + 0.5 + t_b + d
    GEA.append(GE)
    lA.append(l_max)

print(lA[np.argmin(GEA)])
plt.plot(lA,GEA)
plt.grid()
#plt.show()
