import numpy as np
from skimage import io

DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

class GameOfLife:

    def __init__(self, board: np.ndarray):
        self.board = board
    
    def getNextBoard(self):
        newBoard = np.zeros(self.board.shape, dtype=int)

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                neighbours = self.countNeighbours((i, j))

                if neighbours < 2:
                    newBoard[i, j] = 0
                elif neighbours == 2 and self.board[i, j] == 1:
                    newBoard[i, j] = 1
                elif neighbours == 3:
                    newBoard[i, j] = 1
                elif neighbours > 3:
                    newBoard[i, j] = 0

        return GameOfLife(newBoard)

    def countNeighbours(self, pos: tuple) -> int:
        neighbours = 0

        for d in DIRECTIONS:
            if pos[0] + d[0] < 0 or pos[1] + d[1] < 0 or pos[0] + d[0] >= self.board.shape[0] or pos[1] + d[1] >= self.board.shape[1]:
                continue

            neighbours += self.board[pos[0] + d[0], pos[1] + d[1]]

        return neighbours
    
    def saveBoard(self, filename: str):
        rows, cols = self.board.shape
        outputBoard = np.ndarray((rows * 3, cols * 3), dtype=int)
        for i in range(outputBoard.shape[0]):
            for j in range(outputBoard.shape[1]):
                outputBoard[i, j] = self.board[i //3, j // 3]

        io.imsave(filename, outputBoard.transpose().astype(np.uint8) * 255)