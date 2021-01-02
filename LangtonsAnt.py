import pygame as pg
import random
pg.init()

# At a white square, turn 90° clockwise, flip the color of the square, move forward one unit
# At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit

DIM  = (800,800)
WIN = pg.display.set_mode(DIM)
run = True

res = 8

rows = int(DIM[0]/res)

grid = [[0 for i in range(rows)] for j in range(rows)]

ax, ay = int(rows/2), int(rows/2)
grid[ax][ay] = 1

colBg = (50, 50, 50)
colVis = (148, 54, 224)
colAnt = (54, 255, 188)

up, right, down, left = 0, 1, 2, 3
antDir = up

WIN.fill(colBg)

while run:
    # pg.time.delay(10)

    for x in range(rows):
        for y in range(rows):
            # White
            if grid[x][y] == 1:
                pg.draw.rect(WIN, colVis, (x*res, y*res, res, res))            

            # Ant Pos
            if x == ax and y == ay:                
                pg.draw.rect(WIN, colAnt, (x*res, y*res, res, res))
    

    # Move Clockwise
    if grid[ax][ay] == 1:
        grid[ax][ay] = 0
        antDir += 1
    # Move Counter Clockwise
    elif grid[ax][ay] == 0:
        grid[ax][ay] = 1
        antDir -= 1

    if antDir > 3: antDir = 0
    elif antDir < 0: antDir = 3

    # Move Up
    if antDir == up: ay-=1
    # Move Right
    elif antDir == right: ax += 1
    # Move Down
    elif antDir == down: ay += 1
    # Move Left
    elif antDir == left: ax -= 1

    if ay > rows-1: ay = 0
    elif ay < 0: ay = rows-1
    
    if ax > rows-1: ax = 0
    elif ax < 0: ax = rows-1
    
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

    pg.display.update()


pg.quit()