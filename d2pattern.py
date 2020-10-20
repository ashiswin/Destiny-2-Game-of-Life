from PIL import Image
from gameoflife import GameOfLife
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

im = Image.open("destiny pattern.png")
pix = im.load()

state = []
for i in range(0, im.size[0], 3):
    state.append([])
    for j in range(0, im.size[1], 3):
        if pix[i, j] > 0:
            state[i // 3].append(1)
        else:
            state[i // 3].append(0)

im.close()

board = GameOfLife(np.asarray(state, dtype=int))
for i in range(7778):
    board.saveBoard(f"boards/{i}.tiff")
    board = board.getNextBoard()