import numpy as np

import nearest_neighbours as nn


def step(grid, boundary: str = "dead"):
    neighbours = nn.alive_neighbours(grid, boundary=boundary)

    alive = grid == 1
    survives = alive & ((neighbours == 2) | (neighbours == 3))
    born = ~alive & (neighbours == 3)

    return (survives | born).astype(np.uint8)
