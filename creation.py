import numpy as np


def normalize_shape(rows: int, cols: int | None = None) -> tuple[int, int]:
    if rows <= 0:
        raise ValueError("rows must be positive")

    if cols is None:
        cols = rows

    if cols <= 0:
        raise ValueError("cols must be positive")

    return rows, cols


def random_grid(
    rows: int,
    cols: int | None = None,
    density: float = 0.5,
    seed: int | None = None,
) -> np.ndarray:
    rows, cols = normalize_shape(rows, cols)

    if not 0.0 <= density <= 1.0:
        raise ValueError("density must be between 0 and 1")

    rng = np.random.default_rng(seed)
    return (rng.random((rows, cols)) < density).astype(np.uint8)


def empty_grid(rows: int, cols: int | None = None) -> np.ndarray:
    rows, cols = normalize_shape(rows, cols)
    return np.zeros((rows, cols), dtype=np.uint8)


def block(rows: int, cols: int | None = None) -> np.ndarray:
    grid = empty_grid(rows, cols)
    r = grid.shape[0] // 2
    c = grid.shape[1] // 2

    grid[r : r + 2, c : c + 2] = 1
    return grid


def blinker(rows: int, cols: int | None = None) -> np.ndarray:
    grid = empty_grid(rows, cols)

    if min(grid.shape) < 5:
        raise ValueError("grid must be at least 5x5")

    r = grid.shape[0] // 2
    c = grid.shape[1] // 2

    grid[r - 1 : r + 2, c] = 1
    return grid


def glider(rows: int, cols: int | None = None) -> np.ndarray:
    grid = empty_grid(rows, cols)

    if min(grid.shape) < 5:
        raise ValueError("grid must be at least 5x5")

    r = grid.shape[0] // 2
    c = grid.shape[1] // 2

    pattern = np.array(
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
        ],
        dtype=np.uint8,
    )

    grid[r : r + 3, c : c + 3] = pattern
    return grid


def frog(rows: int, cols: int | None = None) -> np.ndarray:
    grid = empty_grid(rows, cols)

    if grid.shape[0] < 3 or grid.shape[1] < 3:
        raise ValueError("grid must be at least 3x3")

    grid[0, 1] = 1
    grid[1, 2] = 1
    grid[2, 0] = 1
    grid[2, 1] = 1
    grid[2, 2] = 1

    return grid


def create_grid(
    pattern: str,
    rows: int,
    cols: int | None = None,
    density: float = 0.5,
    seed: int | None = None,
) -> np.ndarray:
    if pattern == "random":
        return random_grid(rows=rows, cols=cols, density=density, seed=seed)

    if pattern == "block":
        return block(rows, cols)

    if pattern == "blinker":
        return blinker(rows, cols)

    if pattern == "glider":
        return glider(rows, cols)

    if pattern == "frog":
        return frog(rows, cols)

    raise ValueError(f"unknown pattern: {pattern}")


# Backward-compatible alias for the original API.
random = random_grid
