import pygame
import random

pygame.init()

# Parameters you can change
# Resolution of the grid
size = 8
# Waiting period between frames
delay = 50


colBg = (50, 50, 50)
colA = (148, 54, 224)

Width, Height = 800,800
WIN = pygame.display.set_mode((Width, Height))
run = True

rows = int(Width / size)

# Initilizing the grid
grid = [[0 for i in range(rows)] for j in range(rows)]

for i in range(rows*4):
    grid[random.randint(0,rows-1)][random.randint(0,rows-1)] = 1

# grid 1 => Cell Alive, WHITE
# grid 0 => Cell Dead, BLACK (DONT DRAW A DEAD CELL)


# Function to count neighbours
def countNeighbours(arr, a, b):
    neighbours = 0
    for i in range(-1,2):
        for j in range(-1,2):
            try:
                neighbours += arr[a+i][b+j]
            except:
                pass

    neighbours -= arr[a][b]
    return neighbours

print("***************************************")
print("***************************************")
print("Press SPACEBAR to make a new Population")
print("***************************************")
print("***************************************")

while run:
    WIN.fill(colBg)
    pygame.time.delay(delay)

    # Draw the grid
    for i in range(rows):
        for j in range(rows):
            x=i*size
            y=j*size
            if(grid[i][j] == 1):
                #FILL WHITE FOR ALIVE CELLS
                # pygame.draw.circle(WIN, col, (x,y), size/2, 0)
                pygame.draw.rect(WIN, colA, (x,y,size, size), 0)
                temp = random.randint(0,5)
                      
    newgrid = grid

    # COUNTING THE NEIGHBOURS
    for i in range(rows):
        for j in range(rows):
            neighbours = countNeighbours(grid, i, j)
                       
            # Change state of the population
            state = grid[i][j]

            # Rules for Conway's Game Of Life => Cellular Automaton
            # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            # Any live cell with two or three live neighbours lives on to the next generation.
            # Any live cell with more than three live neighbours dies, as if by overpopulation.
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

            if(state == 1 and neighbours < 2):
                newgrid[i][j] = 0
            elif (state == 1 and neighbours in [2,3]):
                newgrid[i][j] = state
            elif(state == 1 and neighbours > 3):
                newgrid[i][j] = 0
            elif(state == 0 and neighbours == 3):
                newgrid[i][j] = 1

    # Updating the grid 
    grid = newgrid


    pygame.display.update()
    for e in pygame.event.get():
        if(e.type == pygame.QUIT):
            run = False
        
        # GENERATE A NEW RANFDOM POPULATION
        if (e.type == pygame.KEYDOWN):
            if e.key == pygame.K_SPACE:
                grid = [[0 for i in range(rows)] for j in range(rows)]
                for i in range(rows*5):
                    grid[random.randint(0,rows-1)][random.randint(0,rows-1)] = 1


pygame.quit()