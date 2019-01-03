import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("data.csv", delimiter=",")
for i in range(0,8):
    X = data[:,i]
    print(X)
    plt.hist(X)
    plt.show()
Y = data[:,8]
print(Y)
plt.hist(Y)
plt.show()
