import matplotlib.pyplot as plt
from modeHandler import set_mode
from observer import Observer
import pygame


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FPS = 60

data = []

sun, planets = set_mode()
obs = Observer(pygame.Vector2(50, 50))
print(planets)
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simulation')

clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    for p in planets:
        p.update(sun)

    sun.draw(screen)

    for p in planets:
        p.draw(screen)

    obs.draw_tangents(screen, sun)

    light = 1

    for p in planets:
        light -= obs.get_light_percentage(sun, p)

    data.append(light)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

li = list(zip(range(0, len(data)), data))
plt.plot(*zip(*li))
plt.show()