import sys
import pygame
import pprint
pygame.init()


def colour_board(x, y, color):
    pygame.draw.rect(screen, color, [
                     (MARGIN + WIDTH) * x + MARGIN, (MARGIN + HEIGHT) * y + MARGIN, WIDTH, HEIGHT], 3)


def text_objects(text, font):
    textSurface = font.render(str(text), True, WHITE)
    return textSurface, textSurface.get_rect()


def display_text(x, y, text):
    font = pygame.font.Font('freesansbold.ttf', WIDTH*3//5)
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = ((MARGIN + WIDTH) * y + MARGIN +
                       WIDTH/2, (MARGIN + HEIGHT) * x + MARGIN+HEIGHT/2)
    screen.blit(TextSurf, TextRect)


def clickbox(clickpos):
    col = clickpos[0]//(MARGIN+WIDTH)
    row = clickpos[1]//(MARGIN+HEIGHT)
    return row, col


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
    # checking col
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

    fixed = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                fixed.append((i, j))

    # colors
    WHITE = (225, 225, 225)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    # the main window
    WINDOW_SIZE = (500, 550)
    WIDTH = 50
    HEIGHT = 50
    MARGIN = 5
    clickpos = None

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                clickpos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Sudoku Solver")

        if keys[pygame.K_SPACE]:
            pygame.display.update()
            for (i, j) in fixed:
                board[i][j] = 0
            if main(board):
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()

                    screen.fill(BLACK)

                    for row in range(9):
                        for col in range(9):
                            colour_board(col, row, RED)
                            if board[row][col] > 0:
                                display_text(row, col, board[row][col])

                    pygame.display.update()

            else:
                print("No solutions found")
        else:
            display_text(9, 4, "Press 'SPACE' to see the solution")
            for row in range(9):
                for col in range(9):
                    colour_board(row, col, RED)
                    if board[row][col] > 0:
                        display_text(row, col, board[row][col])

            if clickpos:
                row, col = clickbox(clickpos)
                if (row, col) in fixed:
                    colour_board(col, row, GREEN)
                    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    for num in nums:
                        if keys[eval("pygame.K_"+str(num))]:
                            board[row][col] = num
                            display_text(row, col, num)

        pygame.display.update()
