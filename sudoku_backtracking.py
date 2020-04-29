import pprint
import time


def findEmpty(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return i, j


def isSafe(board, pos, num):
    row, col = pos
    # checking row
    for i in range(0, 9):
        if board[row][i] == num:
            return False
    # checking column
    for i in range(0, 9):
        if board[i][col] == num:
            return False
    # checking box
    for i in range(row//3*3, row//3*3+3):
        for j in range(col//3*3, col//3*3+3):
            if board[i][j] == num:
                return False
    return True


def main(board):

    pos = findEmpty(board)

    if not(pos):
        return True

    for num in range(1, 10):

        if isSafe(board, pos, num):
            board[pos[0]][pos[1]] = num
            if main(board):
                return True
            board[pos[0]][pos[1]] = 0

    return False


if __name__ == "__main__":
    board = [[8, 5, 0, 0, 0, 2, 4, 0, 0],
             [7, 2, 0, 0, 0, 0, 0, 0, 9],
             [0, 0, 4, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 7, 0, 0, 2],
             [3, 0, 5, 0, 0, 0, 9, 0, 0],
             [0, 4, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 8, 0, 0, 7, 0],
             [0, 1, 7, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 3, 6, 0, 4, 0]]
    start = time.time()

    if main(board):
        end = time.time()
        pprint.pprint(board)
        print("Finished in", "%.3f" % (end-start), "seconds")
    else:
        print("No solutions found")
