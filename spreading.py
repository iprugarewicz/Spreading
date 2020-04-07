import pygame
import sys
import random
import math
import time

pygame.init()

angle = 0
elements = 100
els = []
v = 0.5
sizex = 500
sizey = 500
screen = pygame.display.set_mode((sizex, sizey))

for i in range(elements):
    els.append(
        [sizex / 2, sizey / 2, v * math.cos(i * 2 * math.pi / elements), v * math.sin(i * 2 * math.pi / elements),
         False])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
    screen.fill((0, 0, 0))
    for i, j in zip(els, range(len(els))):
        pygame.draw.circle(screen, (255, 255, 0), (int(i[0]), int(i[1])), 2)
        els[j][0] += i[2]
        els[j][1] += i[3]

    pygame.display.flip()
    time.sleep(0.011)
