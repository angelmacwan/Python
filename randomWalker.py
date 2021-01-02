import random
import pygame

pygame.init()
HEIGHT, WIDTH = 500,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Walker")

run = True

x = WIDTH / 2
y = HEIGHT / 2
r=20
g=30
b=10

stepSize = 1

while run:
    # pygame.time.delay(5)
    flag = random.randint(2,5)

    if(flag == 2):
        y-=stepSize
        r+=1
    elif(flag == 3):
        x+=stepSize
        g+=1
    elif(flag == 4):
        y+=stepSize
        b+=1
    elif(flag == 5):
        x-=stepSize
        
    if(x>WIDTH or x<0 or y>HEIGHT or y<0):
        x = WIDTH / 2
        y = HEIGHT / 2

    

    if(r>255):r=20
    if(g>255):g=30
    if(b>255):b=10

    

    for e in pygame.event.get():
        if(e.type == pygame.QUIT):
            run = False

    pygame.draw.rect(WIN, (r,g,b), (x,y,stepSize,stepSize))

    pygame.display.update()

pygame.quit()