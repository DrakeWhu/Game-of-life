# This file creates the initial distribution of 1s and 0s
import matplotlib.pyplot as plt
import numpy as np
import random

def random(N):
    arr = np.random.rand(N,N)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i,j]<0.5:
                arr[i,j]=0
            else:
                arr[i,j]=1
    
    return arr

def frog(N):
    arr = np.zeros((N,N))

    arr[0,1] = 1
    arr[1,2] = 1
    arr[2,0] = 1
    arr[2,1] = 1
    arr[2,2] = 1

    return arr    
