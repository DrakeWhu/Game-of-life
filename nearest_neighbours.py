import scipy.ndimage as ndimage

_NEIGHBOUR_KERNEL = ndimage.generate_binary_structure(2, 2).astype(int)
_NEIGHBOUR_KERNEL[1, 1] = 0


def alive_neighbours(grid, boundary: str = "dead"):
    if boundary == "dead":
        mode = "constant"
        cval = 0
    elif boundary == "wrap":
        mode = "wrap"
        cval = 0
    else:
        raise ValueError("boundary must be 'dead' or 'wrap'")

    return ndimage.convolve(grid, _NEIGHBOUR_KERNEL, mode=mode, cval=cval)
