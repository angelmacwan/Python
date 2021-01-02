import pygame
import random

n = 100
speed = 60

WIDTH, HEIGHT = 600, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

run = True

arr = []
for i in range(n):
    arr.append([random.randint(0, HEIGHT), 0])


cur = -1
comparisions = 0
operations = 0

while run:
    width = WIDTH/n
    x = 0

    WIN.fill((255,255,255))

    print(f'Comparisions => {comparisions}, Operations => {operations}')

    for e in pygame.event.get():
        if(e.type == pygame.QUIT):
            run = False

    for a in range(len(arr)):
        if(arr[a][1] == 0):
            pygame.draw.rect(WIN, (0, 255, 255), (x, 0, width, arr[a][0]))
        elif(arr[a][1] == 1):
            pygame.draw.rect(WIN, (0, 255, 0), (x, 0, width, arr[a][0]))
            arr[a][1] = 0
        elif(arr[a][1] == 2):
            pygame.draw.rect(WIN, (255, 0, 0), (x, 0, width, arr[a][0]))
            arr[a][1] = 0

        x += width


    pygame.time.delay(100)
    for i in range(speed):
        comparisions+=1
        if(arr[cur][0] < arr[cur+1][0]):
            arr[cur+1][0], arr[cur][0] = arr[cur][0], arr[cur+1][0]
            arr[cur][1], arr[cur+1][1] = 1,2
            cur = -1
            operations += 1
        if(cur < len(arr)-2):
            cur += 1


    pygame.display.update()


pygame.quit()
