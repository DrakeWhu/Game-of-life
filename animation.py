import argparse
import itertools

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from creation import create_grid
from step import step

mpl.rcParams["toolbar"] = "None"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a Conway Game of Life simulation.")

    parser.add_argument("--n", type=int, default=None, help="Square grid size.")
    parser.add_argument("--rows", type=int, default=108, help="Number of grid rows.")
    parser.add_argument("--cols", type=int, default=192, help="Number of grid columns.")

    parser.add_argument(
        "--frames", type=int, default=0, help="Number of frames. Use 0 for infinite."
    )
    parser.add_argument("--fps", type=float, default=20.0, help="Target frames per second.")
    parser.add_argument("--density", type=float, default=0.3, help="Initial alive-cell density.")
    parser.add_argument("--seed", type=int, default=None, help="Random seed.")

    parser.add_argument(
        "--pattern",
        choices=["random", "block", "blinker", "glider", "frog"],
        default="random",
        help="Initial pattern.",
    )
    parser.add_argument(
        "--boundary",
        choices=["dead", "wrap"],
        default="wrap",
        help="Boundary condition.",
    )
    parser.add_argument(
        "--cmap",
        default="binary",
        help="Matplotlib colormap.",
    )
    parser.add_argument(
        "--fullscreen",
        action="store_true",
        help="Ask matplotlib backend for fullscreen mode.",
    )
    parser.add_argument(
        "--fill-screen",
        action="store_true",
        help="Stretch the image to fill the whole window.",
    )
    parser.add_argument(
        "--cell-size",
        type=int,
        default=None,
        help="Approximate visual cell size in screen pixels. Smaller means more cells.",
    )
    parser.add_argument("--screen-width", type=int, default=1920)
    parser.add_argument("--screen-height", type=int, default=1080)

    return parser.parse_args()


def configure_window(fig, ax, fullscreen: bool) -> None:
    fig.canvas.manager.set_window_title("Conway's Game of Life")

    # Remove all figure/axes padding.
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set_position([0, 0, 1, 1])
    ax.set_axis_off()

    if fullscreen:
        manager = plt.get_current_fig_manager()
        try:
            manager.full_screen_toggle()
        except Exception:
            # Some matplotlib backends do not support fullscreen.
            pass


def resolve_colormap(name: str):
    if name == "screensaver":
        return ListedColormap(["black", "white"])

    return name


def resolve_shape(
    n: int | None,
    rows: int,
    cols: int,
    cell_size: int | None,
    screen_width: int,
    screen_height: int,
) -> tuple[int, int]:
    if n is not None:
        return n, n

    if cell_size is not None:
        if cell_size <= 0:
            raise ValueError("cell-size must be positive")

        return max(1, screen_height // cell_size), max(1, screen_width // cell_size)

    return rows, cols


def run(
    rows: int,
    cols: int,
    frames: int,
    fps: float,
    density: float,
    seed: int | None,
    pattern: str,
    boundary: str,
    cmap: str,
    fullscreen: bool,
    fill_screen: bool,
) -> None:
    grid = create_grid(pattern=pattern, rows=rows, cols=cols, density=density, seed=seed)

    delay = 1.0 / fps if fps > 0 else 0.01

    fig, ax = plt.subplots()
    configure_window(fig, ax, fullscreen=fullscreen)

    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    image = ax.imshow(
        grid,
        cmap=resolve_colormap(cmap),
        interpolation="nearest",
        vmin=0,
        vmax=1,
        aspect="auto" if fill_screen else "equal",
    )

    running = {"value": True}

    def on_key_press(event):
        if event.key in {"escape", "q"}:
            running["value"] = False
            plt.close(fig)

    fig.canvas.mpl_connect("key_press_event", on_key_press)

    iterator = range(frames) if frames > 0 else itertools.count()

    for _ in iterator:
        if not running["value"] or not plt.fignum_exists(fig.number):
            break

        grid = step(grid, boundary=boundary)
        image.set_data(grid)
        plt.pause(delay)

    plt.show()


def main() -> None:
    args = parse_args()
    rows, cols = resolve_shape(
        n=args.n,
        rows=args.rows,
        cols=args.cols,
        cell_size=args.cell_size,
        screen_width=args.screen_width,
        screen_height=args.screen_height,
    )

    run(
        rows=rows,
        cols=cols,
        frames=args.frames,
        fps=args.fps,
        density=args.density,
        seed=args.seed,
        pattern=args.pattern,
        boundary=args.boundary,
        cmap=args.cmap,
        fullscreen=args.fullscreen,
        fill_screen=args.fill_screen,
    )


def screensaver() -> None:
    run(
        rows=270,
        cols=480,
        frames=0,
        fps=30.0,
        density=0.20,
        seed=None,
        pattern="random",
        boundary="wrap",
        cmap="screensaver",
        fullscreen=True,
        fill_screen=True,
    )


if __name__ == "__main__":
    main()
