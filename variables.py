WIDTH = 800
HEIGHT = 500
GRID_SIZE = 7
CELL_COUNT = GRID_SIZE**2
MINES = CELL_COUNT // 4


def width_percentage(percentage):
    return WIDTH * percentage / 100


def height_percentage(percentage):
    return HEIGHT * percentage / 100


if __name__ == "__main__":
    print(width_percentage(25))
