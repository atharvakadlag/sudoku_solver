import pygame
import sys


def colour_board(x, y, color):
    pygame.draw.rect(screen, color, [
                     (MARGIN + WIDTH) * x + MARGIN, (MARGIN + HEIGHT) * y + MARGIN, WIDTH, HEIGHT], 3)


def text_objects(text, font):
    textSurface = font.render(str(text), True, WHITE)
    return textSurface, textSurface.get_rect()


def display_text(x, y, text):
    font = pygame.font.Font('freesansbold.ttf', WIDTH*3//5)
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = ((MARGIN + WIDTH) * x + MARGIN +
                       WIDTH/2, (MARGIN + HEIGHT) * y + MARGIN+HEIGHT/2)
    screen.blit(TextSurf, TextRect)


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
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:
            sys.exit()  # If user clicked close

    screen.fill(BLACK)

    for row in range(9):
        for column in range(9):
            colour_board(column, row, RED)
            if board[row][column] > 0:
                display_text(row, column, board[row][column])

    pygame.display.update()

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

    # colors
    WHITE = (225, 225, 225)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    # the main window
    WINDOW_SIZE = (490, 490)
    WIDTH = 50
    HEIGHT = 50
    MARGIN = 10
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Sudoku Solver")

    if main(board):
        end = time.time()
        pprint.pprint(board)
        print("Finished in", "%.3f" % (end-start), "seconds")
    else:
        print("No solutions found")
