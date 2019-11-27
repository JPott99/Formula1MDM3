import numpy as np
import matplotlib.pyplot as plt

marketing = 25
n = (70 - marketing) + 1

driving = np.zeros(n)
chasis = np.zeros(n)
engine = np.zeros(n)

for n in range(n):
    driving[n] = marketing
    chasis[n] = n
    engine[-1*n] = n

engine = engine[1:]
engine = np.append(engine, 0)

#print(chasis)
#print(engine)


def performance(which):
    if which == 'Driving':
        cd = 2
        cc = ce = 1
    elif which == 'Chasis':
        cc = 2
        cd = ce = 1
    elif which == 'Engine':
        ce = 2
        cd = cc = 1
    elif which == 'Driving and Chasis':
        cd = cc = 2
        ce = 1
    elif which == 'Chasis and Engine':
        cc = ce = 2
        cd = 1
    else:
        cd = cc = ce = 1

    perform = 3*(cd*driving + cc*chasis + ce*engine)/(cd + cc + ce)
    return perform


which = 'Chasis'
track_list = ['', '', 'Driving', 'Chasis and Engine', 'Engine', 'Chasis', 'Engine', 'Driving and Chasis', '', '']
a = performance(which)
#print(a)

perform_matrix = np.zeros((n+1, len(track_list)))

for k in range(len(track_list)):
    perform_matrix[:, k] = performance(track_list[k])

point_matrix = np.zeros((n, len(track_list)))
print(perform_matrix)

for i in range(10):
    for j in range(n):
        if perform_matrix[j, i] >= 102.5:
            point_matrix[j, i] = 25
        elif 102.5 > perform_matrix[j, i] >= 100:
            point_matrix[j, i] = 20
        elif 100 > perform_matrix[j, i] >= 97.5:
            point_matrix[j, i] = 16
        elif 97.5 > perform_matrix[j, i] >= 95:
            point_matrix[j, i] = 13
        elif 95 > perform_matrix[j, i] >= 92.5:
            point_matrix[j, i] = 11
        elif 92.5 > perform_matrix[j, i] >= 90:
            point_matrix[j, i] = 10
        elif 90 > perform_matrix[j, i] >= 87.5:
            point_matrix[j, i] = 9
        elif 87.5 > perform_matrix[j, i] >= 85:
            point_matrix[j, i] = 8
        elif 85 > perform_matrix[j, i] >= 82.5:
            point_matrix[j, i] = 7
        elif 82.5 > perform_matrix[j, i] >= 80:
            point_matrix[j, i] = 6
        elif 80 > perform_matrix[j, i] >= 77.5:
            point_matrix[j, i] = 5
        elif 77.5 > perform_matrix[j, i] >= 75:
            point_matrix[j, i] = 4
        elif 75 > perform_matrix[j, i] >= 72.5:
            point_matrix[j, i] = 3
        elif 72.5 > perform_matrix[j, i] >= 70:
            point_matrix[j, i] = 2
        elif 70 > perform_matrix[j, i] >= 67.5:
            point_matrix[j, i] = 1
        elif 67.5 > perform_matrix[j, i]:
            point_matrix[j, i] = 0
        else:
            print('error')

print(point_matrix)
final_score = np.sum(point_matrix, axis=1)
#print(final_score)

chasis = chasis[1:]
chasis = chasis/10
engine = engine[:-1]
engine = engine/10
marketing = marketing/10
"""
fig, axs = plt.subplots(nrows=1, ncols=2, sharex=True)

ax = axs[0]
ax.plot(chasis, final_score)
ax.set_xlabel('chassis investment')
ax.set_ylabel('Points won in a season')

ax = axs[1]
ax.plot(engine, final_score)
ax.set_xlabel('engine investment')
ax.set_ylabel('Points won in a season')

fig.suptitle('WHICH ONE SHOULD I USE?')
plt.show()"""

fig, ax = plt.subplots()
ax.plot(chasis, final_score, label='chassis investment')
ax.set_xlabel('Investment')
ax.set_ylabel('Total points won in a season')
ax.plot(engine, final_score, label='engine investment')

fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95))
plt.tight_layout()
plt.grid(True)
plt.show()
