# This file is given an array and checks how many nearest neighbours are alive for each cell
import numpy as np
import scipy.ndimage as ndimage

def alive_neighbours(grid):
    kern = ndimage.generate_binary_structure(2, 2)
    kern[1][1] = False
    arr = ndimage.convolve(grid, kern, mode='constant', cval=0)
    return arr
