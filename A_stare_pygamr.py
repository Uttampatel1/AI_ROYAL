import pygame
from pygame.locals import *

# define a window size

WIDTH = 600
# HEIGHT
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)

# function area

class Node():
    def __init__(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = GREEN
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.width))

def make_grid(rows,width):
    grid = []
    node_width = width // rows
    for i in range(rows):
        temp = []
        for j in range(rows):
            node = Node(i, j, node_width, rows)      
            temp.append(node)
        grid.append(temp)
    return grid

def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap))      # drawing 6 horizontal lines if rows = 6
        for j in range(rows):
            pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, width))  # drawing 6 vertical lines if rows = 6

def draw(window, grid,rows,width):
    window.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(window)
    draw_grid(window, rows, width)
    pygame.display.update()


def main(width,window):
    ROWS = 8
    grid = make_grid(ROWS, width)
    start = None
    end = None

    running = True
    started = False

    while True:
        draw(window,grid,ROWS,width)

main(WIDTH, WINDOW)

