import numpy as np
import matplotlib.pyplot as plt

X=np.array([1,2,3,4,5])
Y=np.array([1,2,3,4,5])

def gradient_descent(X,Y):
    m=0
    c=0
    L=0.01
    epochs=1000
    n=X.size
    
    
    for i in range(epochs):
        Dm=(-2/n) * np.sum(X * (Y-(m*X + c)))
        Dc=(-2/n) * np.sum(Y-(m*X + c))
        m=m-L*Dm
        c=c-L*Dc
        
    return m,c

m,c=gradient_descent(X,Y)

plt.scatter(X,Y)    #Original Line
plt.plot(X,m*X+c,c='red')   #Points with predicted Y for a given X
plt.show()
