import numpy as np
import matplotlib.pyplot as plt

plt.close('all') # closes plot

data = np.array([3, 7, 9, 2, 5, 6, 3, 9, 0, 11, 4, 8])
x = sorted(data)
k = 2 # number of clusters (given)
d_list = np.zeros(len(x)-1)
k1 = np.array([])
k2 = np.array([])

for i in range(len(x)-1):
    p1 = x[i]
    p2 = x[i+1]
    dist = abs(p2-p1)
    d_list[i] = dist
    
d = np.max(d_list)/k
j = np.argmax(d_list)
mp = x[j]+d

for i in range(len(x)):
    if x[i] < mp:
        k1 = np.append(k1, x[i])
    else:
        k2 = np.append(k2, x[i])

plt.scatter(k1, np.zeros(len(k1)), c='C1')
plt.scatter(k2, np.zeros(len(k2)), c='C2')
