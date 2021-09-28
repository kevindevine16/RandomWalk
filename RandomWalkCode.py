# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 17:48:23 2021

@author: Kevin.Devine
"""
import numpy as np
from matplotlib import rc
import matplotlib.pylab as plt

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

def ranWalk(start,n,color):
    rng = np.random
    x = start*np.ones((n,2))
    eps3 = rng.random((n,1))
    for i in range(1,n): 
        
        if eps3[i-1] <= 0.25:
            x[i,0] = x[i-1,0]+1
            x[i,1] = x[i-1,1]
            
        if eps3[i-1] > 0.25 and eps3[i-1] <= 0.4999:
            x[i,0] = x[i-1,0]-1
            x[i,1] = x[i-1,1]
            
        if eps3[i-1] > 0.4999 and eps3[i-1] <= 0.75:
            x[i,1] = x[i-1,1]+1
            x[i,0] = x[i-1,0]
            
        if eps3[i-1] > 0.75:
            x[i,1] = x[i-1,1]-1
            x[i,0] = x[i-1,0]
       
    fig = plt.figure(1,figsize=(4,4),dpi=180) 
    plt.scatter(x[:,0], x[:,1],c=color,alpha=0.55,s=0.15);
    plt.plot(x[:,0],x[:,1],c=color,alpha=0.55)
    plt.plot(x[0,0], x[0,1],c="black", marker='+')
    plt.plot(x[-1,0], x[-1,1],c='red', marker='o')
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
        
    plt.axes().set_aspect('equal', 'datalim')
    plt.title("Random Walk Starting at " + str(start)+" for "+str(n)+ " steps")
    # plt.patch.set_facecolor('#ababab')
    # plt.patch.set_alpha(0.5)
    # fig = plt.figure()
    # fig.patch.set_facecolor('black')
    # fig.patch.set_alpha(0.7)
    # ax = fig.add_subplot(111)
    # ax.patch.set_facecolor('black')
    # ax.patch.set_alpha(0.8)
    plt.show()
    return x
start = 10
n = 1000
colors = [['cyan', 'magenta','green']]
for i in range(0,len(colors[0])):
    ranWalk(start,n,colors[0][i])