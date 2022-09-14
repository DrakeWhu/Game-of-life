# Main animation file
import matplotlib.pyplot as plt
import creation
from step import step

N = 100 #Size of the grid
frames = 25

arr = creation.random(N) #Creation of the initial array

for _ in range(frames):
    step(arr,N)
    
    plt.imshow(arr)
    plt.pause(0.1)

plt.show()
    