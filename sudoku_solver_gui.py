import pygame, sys
import numpy as np

pygame.font.init()


# constants and variables
width = 540
height = 540
height1 = 600

board_color = (255, 255, 255)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
line_color = (0, 0, 0)
line_tick = 1
border_thick = 4
rows = 9
cols = 9
# circle_radius = 60
# circle_width = 15
# cicle_color = (239, 231, 200)
# cross_width = 25
# cross_color = (66, 66, 66)
# cross_space = 55



# screen

screen = pygame.display.set_mode( (width, height1) )
pygame.display.set_caption("Sudoku solver from sai kumar adapa                    ")
screen.fill(white)

def draw_lines() :
    # pygame.draw.line(screen, line_color, (0,200), (600, 200), )
    gap = width / 9
    for i in range(9 + 1):
        if i % 3 == 0 and i != 0:
            thick = 4
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * gap), (width, i * gap), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * gap, 0), (i * gap, height), thick)


def show_numbers(row, col):

    fnt = pygame.font.SysFont("comicsans", 40)
    text = fnt.render(str(board[row][col]), 2, blue)
    if str(board[row][col]) != str(0):
        if int(board[row][col]) == int(board1[row][col]):
            if int(board1[row][col]) != 0:
                text = fnt.render(str(board[row][col]), 2, (0, 0, 0))
        screen.blit(text, (col * 60 + 15, row * 60))


def show_board() :
    for i in range(rows):
        for j in range(cols):
            fnt = pygame.font.SysFont("comicsans", 40)
            text = fnt.render(str(board[i][j]), 2, blue)
            if int(board[i][j]) == int(board1[i][j]) :
                if int(board1[i][j]) != 0:
                    text = fnt.render(str(board[i][j]), 2, (0, 0, 0))
            if str(board[i][j]) != str(0) :
                screen.blit(text, (j * 60 + 15, i * 60))




board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board2 =   [[1, 0, 5, 0, 0, 2, 0, 8, 4],
             [0, 0, 6, 3, 0, 1, 2, 0, 7],
             [0, 2, 0, 0, 5, 0, 0, 0, 0],
             [0, 9, 0, 0, 1, 0, 0, 0, 0],
             [8, 0, 2, 0, 3, 6, 7, 4, 0],
             [3, 0, 7, 0, 2, 0, 0, 9, 0],
             [4, 7, 0, 0, 0, 8, 0, 0, 1],
             [0, 0, 1, 6, 0, 0, 0, 0, 9],
             [2, 6, 9, 1, 4, 0, 3, 7, 0]
             ]



def solve(bo):
    find = find_empty(bo)
    if not find:
        show_board()
        return True

    else:
        row, col = find
        show_numbers(row, col)

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
# solve(board)
show_board()
print("___________________")
print_board(board)


draw_lines()

#main loop
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                solve(board)

            if event.key == pygame.K_ESCAPE:
                sys.exit()


    pygame.display.update()