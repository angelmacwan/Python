import pygame
import random

HEIGHT, WIDTH = 250, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game 02")

# font = pygame.font.SysFont('Century', 24)

run = True

class obstacle:
    def __init__(self):
        self.x = WIDTH
        self.y = HEIGHT - random.random() * 50
        self.height = HEIGHT - self.y
        self.width = 30
        self.vel = 2

    def show(self):
        if(self.y < 20):
            self.y = 20
            self.height = HEIGHT - self.y

        pygame.draw.rect(WIN, (255, 0, 0), (self.x, self.y, self.width, self.height))


    def update(self):
        self.x -= self.vel

        if(self.x+self.width < 0):
            self.x = WIDTH
            self.y = HEIGHT - random.random() * 50
            self.height = HEIGHT - self.y
            return 1
        return 0

    def colide(self, other):
        if(self.x <= other.x + other.width
                and self.x + self.width >= other.x + other.width
                and self.y <= other.y + other.height):
            self.vel = 0


class player:

    def __init__(self):
        self.height = 30
        self.width = 30
        self.x = 100
        self.y = HEIGHT-self.height - 50
        self.vel = 0
        self.jump = False
        self.jumpDist = 10
        self.GRAV = 0.75
        self.score = 0

    def show(self):
        pygame.draw.rect(WIN, (0, 255, 0), (self.x, self.y, self.width, self.height))
        if(self.y > HEIGHT-self.height):
            self.y = HEIGHT-self.height

    def showScore(self):
        scoreText = font.render(self.score, True, (0,255,255))
        WIN.blit(scoreText, (20, 20))

    def update(self):
        if(self.y < HEIGHT-self.height or self.jump):
            self.vel += self.GRAV
            self.y += self.vel
        else:
            self.vel = 0

        if(self.jump and self.jumpDist >= -15):
            self.GRAV = -0.4
            self.jumpDist -= 1
        else:
            self.jump = False
            self.jumpDist = 5
            self.GRAV = 0.4


player = player()
obs = obstacle()

while run:
    pygame.time.delay(10)
    WIN.fill((0, 0, 0))
    player.show()
    player.update()
    obs.show()
    player.score += obs.update()
    obs.colide(player)
    # player.showScore()

    for e in pygame.event.get():
        if(e.type == pygame.QUIT):
            run = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                player.jump = True

    pygame.display.update()

pygame.quit()
