import pandas as pd
import math
import matplotlib.pyplot as plt

ds1=pd.read_csv("./xdata.csv")
ds2=pd.read_csv("./ydata.csv")

import numpy as np

X=ds1.values[:,1:]

points=np.random.random((2,2))*5

plt.scatter(X[:,0],X[:,1],c='blue')
plt.scatter(points[0][0],points[0][1],c='red')
plt.scatter(points[1][0],points[1][1],c='red')
plt.show(block=False)
plt.pause(1)
plt.close()

for i in range(5):
    near1=[]
    near2=[]
    for i in range(X.shape[0]):
        dis1=np.abs(np.sum(X[i]-points[0]))
        dis2=np.abs(np.sum(X[i]-points[1]))
        
        if(dis1 < dis2):
            near1.append(X[i])
        else:
            near2.append(X[i])

    mean1=np.mean(near1, axis=0)
    mean2=np.mean(near2, axis=0)

    points[0]=mean1
    points[1]=mean2
    plt.clf()
    plt.scatter(X[:,0],X[:,1],c='blue')
    for i in range(points.shape[0]):
        plt.scatter(points[i][0],points[i][1],c='red')  
plt.show()
