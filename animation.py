# Main animation file
import matplotlib.pyplot as plt
import creation
from step import step

N = 75 #Size of the grid
frames = 500

arr = creation.random(N) #Creation of the initial array

for _ in range(frames):
    arr = step(arr)
    
    plt.imshow(arr)
    plt.pause(0.01)
    plt.clf()

plt.show()
    