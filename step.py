# Input: A NxN grid with 1s and 0s
# Output: A new NxN grid with 1s and 0s after doing one step of the game of life
import nearest_neighbours as nn

def step(arr,N):
    alive_neighbours = nn.alive_neighbours(arr,N)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i,j] == 1:
                if alive_neighbours[i,j] < 2:
                    arr[i,j] = 0
                if alive_neighbours[i,j] > 3:
                    arr[i,j] = 0
            if arr[i,j] == 0:
                if alive_neighbours[i,j] == 3:
                    arr[i,j] = 1

    
    return arr
    
    