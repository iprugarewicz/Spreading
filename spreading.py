import pygame
import sys
import random
import math
import time

pygame.init()

angle = 0
elements = 100
els = []
v = 1
sizex = 500
sizey = 500
screen = pygame.display.set_mode((sizex, sizey))


def curve(alpha):
    return alpha + ((math.pi / 4) * ((random.randrange(101) + random.randrange(101)) / 201)) - (math.pi / 8)


def border(alpha):
    if (math.pi / 4) > alpha >= 0 or (2 * math.pi) > alpha >= (7 * math.pi / 8):
        return math.pi - alpha

    elif (3 * math.pi / 4) > alpha >= (math.pi / 4):
        return math.pi + (math.pi - alpha)

    elif (5 * math.pi / 4) > alpha >= (3 * math.pi / 4):
        return (3 * math.pi) - alpha

    elif (7 * math.pi / 8) > alpha >= (5 * math.pi / 4):
        return math.pi - alpha

for i in range(elements):
    els.append(
        [sizex / 2, sizey / 2, math.pi * 2 * i / elements, False])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
    screen.fill((0, 0, 0))
    for i, j in zip(els, range(len(els))):
        pygame.draw.circle(screen, (255, 255, 0), (int(i[0]), int(i[1])), 2)
        els[j][0] += v * math.cos(i[2])
        els[j][1] += v * math.sin(i[2])
        if els[j][0] <= 1 or els[j][0] >= sizex - 1 or els[j][1] <= 1 or els[j][1] >= sizey - 1:
            els[j][2] = border(els[j][2]) % (math.pi * 2)
            els[j][0] = els[j][0] % sizex
            els[j][1] = els[j][1] % sizey
        # els[j][2] = curve(els[j][2])%(math.pi*2)

    pygame.display.flip()
    time.sleep(0.011)
