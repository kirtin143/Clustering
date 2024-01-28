import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.datasets import load_iris

plt.close('all') # closes plot

#X = np.array([[1, 2], [6, 7], [8, 4], [9, 11], [-1, 0], [0, 4]])
#X = np.array([[10, 0], [9, 2], [8, 1], [1, 7], [2, 10], [0, 12]]) # data (given)
#X = np.array([[0, 0], [10, 5], [1, 2]]) # data (given)
X, _ = make_blobs(20, 2, centers=2, cluster_std=1) # function to create random data
#data = load_iris()
#X = data.data[:, [2, 3]] #petal length and width
k = 2 # number of clusters (given)
y_pred = [] # predicted cluster labels for test data

# finds line of best fit for the data given
X_cord = X[:, 0]
Y_cord = X[:, 1]
z = np.polyfit(X_cord, Y_cord, 1) # 1st degree straight line of best fit
m = z[0] # slope of line of best fit
b = z[1] # y-int of line of best fit
line = m*X_cord+b

#rotates the line of best fit by 90 degrees
m_2 = -1/m
avg_point = (np.min(X_cord)+np.max(X_cord))/2
avg_point_y = m*avg_point+b
avg_point_line_2_y = m_2*avg_point
b_2 = avg_point_y - avg_point_line_2_y
line_2 = m_2*X_cord+b_2

# adds predictions to cluster labels
for i in X:
    if i[1] >= m_2*i[0]+b_2:
        y_pred.append(0)
    else:
        y_pred.append(1)

# plotting
#plt.plot(X_cord, line)
plt.scatter(avg_point, avg_point_y, s=100, c="red")
plt.plot(X_cord, line, c="C0")
plt.plot(X_cord, line_2, c="C1")
plt.scatter(X[:, 0], X[:, 1], cmap="winter", c=y_pred)
plt.axis('equal')
plt.xlim([np.min(X_cord)-1, np.max(X_cord)+1])
plt.ylim([np.min(Y_cord)-1, np.max(Y_cord)+1])
plt.grid()
