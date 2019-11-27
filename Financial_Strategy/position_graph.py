import matplotlib.pyplot as plt
import numpy as np

a = np.array((0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 20, 25))
b = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
labels = ['22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', '3',
          '2', '1']

plt.rc('font', size=15)
plt.plot(b, a)
plt.xticks(b, labels)
plt.xlabel('Position at the end of the race')
plt.ylabel('Number of points received')
plt.grid(linestyle='-.', linewidth=0.5)
plt.show()