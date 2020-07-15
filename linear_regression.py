#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 20:06:46 2020

@author: anandkadam
"""
import numpy as np
import matplotlib.pyplot as mp
import decimal as decimal


#X=np.array([[0],[1000],[1200],[800],[1500],[2000],[650]])

#Y=np.array([[0],[85],[86],[40],[110],[150],[25]])


from sklearn.datasets.samples_generator import make_regression
X, Y = make_regression(n_samples=200, n_features=1, n_informative=1, noise=6, bias=30, random_state=200)
m = 200

W=[[0],[0]]
Y_FINAL = np.empty([200], dtype=float)
SLOPE = W[0]
INTERCEPT = W[1]

m=len(X)

epocs = m
learning_rate=0.15

for i in range(epocs):
    Y_hat = SLOPE*X[i] + INTERCEPT
    
    Y_FINAL[i] = Y_hat 
    #print(Y_hat)
    
    #COST_J = (np.sum(np.square(Y_hat - Y)))*(1/(2*(m)))
    
    COST_J = Y[i] - Y_hat
    

    print (COST_J)
    
    
    #D_slope = np.sum(X[:,0]*(Y - Y_hat))*(-2/m)
    
    #D_intercept = np.sum(Y - Y_hat)*(-2/m)
    
    SLOPE = SLOPE + COST_J*X[i]*learning_rate
    INTERCEPT = INTERCEPT + COST_J*learning_rate
    #mp.plot(X,Y,'ro')
    #mp.plot(X[i], Y_hat)
    #mp.show()

#print(Y_hat)

#OP = SLOPE*1.5 + INTERCEPT
#print(SLOPE, INTERCEPT)
#print("%f" %OP)

NEW = SLOPE*1.5 + INTERCEPT
print(NEW)
NEWX=1.5
#mp.plot(X[199],Y_FINAL[199])
mp.plot(X,Y,'ro')
mp.plot([min(X), max(X)], [min(Y_FINAL), max(Y_FINAL)], color='blue')

mp.show()



