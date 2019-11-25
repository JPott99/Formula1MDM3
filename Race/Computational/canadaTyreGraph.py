import matplotlib.pyplot as plt
import numpy as np
from canada import *
x=np.linspace(0,20,1000)
y_sft = []
y_med = []
y_hrd = []
for i in x:
    y_sft.append(tyre_performance(i,'soft'))
    y_med.append(tyre_performance(i,'medium'))
    y_hrd.append(tyre_performance(i,'hard'))

plt.plot(x,y_sft,x,y_med,x,y_hrd)
plt.legend(["Soft Tyres","Medium Tyres","Hard Tyres"])
plt.grid(1)
plt.xlabel("Laps")
plt.ylabel("p_t")
fileString = ("graphs/CanadianTyres.png")
plt.savefig(fileString)
