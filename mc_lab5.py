from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import  numpy as np
import random as rand
from math import log, exp
from scipy.stats import norm
from scipy.stats.distributions import chi2

x = np.random.normal(0,1,10000)
y = np.random.normal(0,1,10000)
z = np.random.normal(0,1,10000)
fig1 = plt.figure(1)
ax1=fig1.add_subplot(111,projection='3d')
ax1.scatter(x,y,z)

norm = np.sqrt(x ** 2 + y ** 2 + z ** 2)
x = x/norm
y = y/norm
z = z/norm

fig1 = plt.figure(2)
ax1=fig1.add_subplot(111,projection='3d')
ax1.scatter(x,y,z)

fig1 = plt.figure(3)
ax1=fig1.add_subplot(111,projection='3d')



# R liczba replikacji w warstwie
R = 1000
K = 100
for i in range(4):
    #punkty
    x = np.random.normal(0,1,R)
    y = np.random.normal(0,1,R)
    z = np.random.normal(0,1,R)
    norm = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    x = x/norm
    y = y/norm
    z = z/norm
    #promien
    v = np.random.uniform(0,1,R)
    v = v/4 + i/4
    D2 = np.sqrt(chi2.ppf(v,df=3))
    x = x*D2
    y = y*D2
    z = z*D2
    ax1.scatter(x, y, z,label=i,s=1)

#plt.show()
fig1 = plt.figure(4)
ax1=fig1.add_subplot(111,projection='3d')
R = 1000
S = []
for i in range(1, 4):
    s_temp = []
    for j in range(1, 4):
        s_temp.append(1 / 3 * min(i, j))
    S.append(s_temp)
A = np.linalg.cholesky(S)
Z = np.zeros((3, R))
# Y to est ze strata
Y = []
for i in range(4):
    #punkty
    x = np.random.normal(0,1,R)
    y = np.random.normal(0,1,R)
    z = np.random.normal(0,1,R)
    norm = np.sqrt(x ** 2 + y ** 2 + z ** 2)
    x = x/norm
    y = y/norm
    z = z/norm
    #promien
    v = np.random.uniform(0,1,R)
    v = v/4 + i/4
    D2 = np.sqrt(chi2.ppf(v,df=3))
    x = x*D2
    y = y*D2
    z = z*D2
    Z[0, :] = x
    Z[1, :] = y
    Z[2, :] = z
    B = np.dot(A, Z)
    # wyliczamy estymatory
    r = 0.05
    s = 0.25
    s1 = 100 * np.exp((r - s ** 2 / 2) * 1 / 3 + s * B[0,:])
    s2 = 100 * np.exp((r - s ** 2 / 2) * 2 / 3 + s * B[1,:])
    s3 = 100 * np.exp((r - s ** 2 / 2) + s * B[2,:])
    print(s1.shape)
    #ax1.scatter(B[0,:],B[1,:],B[2,:],label=i,s=1)
    ax1.scatter(s1, s2, s3, label=i, s=1)
    # estymacja w danej warstwie
    Y.append(np.mean(np.maximum(1/3*(s1+s2+s3)-K,0)))

print(np.mean(Y))
#fig1 = plt.figure(5)
#ax1=fig1.add_subplot(111,projection='3d')


plt.show()



