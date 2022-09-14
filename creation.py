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