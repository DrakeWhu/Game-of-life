# This file is given an array and checks how many nearest neighbours are alive for each cell
import numpy as np
import scipy.ndimage as ndimage

def alive_neighbours(arr,N):
    alive = np.zeros((N,N))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == N-1 and j == N-1:
                s = arr[i-1,j] + arr[0,j] + arr[i,0] + arr[i,j-1]
            elif i == N-1 and j != N-1:
                s = arr[i-1,j] + arr[0,j] + arr[i,j+1] + arr[i,j-1]   
            elif i != N-1 and j == N-1:
                s = arr[i-1,j] + arr[i+1,j] + arr[i,0] + arr[i,j-1] 
            elif i != N-1 and j != N-1:
                s = arr[i-1,j] + arr[i+1,j] + arr[i,j+1] + arr[i,j-1]
            else:
                print("Algo ha salido mal")
                break
            alive[i,j] = s
    return alive

            