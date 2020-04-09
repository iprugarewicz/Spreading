import pygame
import sys
import random
import math
import time

pygame.init()

elements = 1000
els = []
v = 1
sizex = 500
sizey = 700
screen = pygame.display.set_mode((sizex, sizey))
pygame.display.set_caption('Virus spreading simulation')

def curve(alpha):
    return alpha + ((math.pi / 4) * ((random.randrange(101) + random.randrange(101)) / 201)) - (math.pi / 8)


def border(elem):
    if elem[0] >= sizex - 1:
        return (math.pi - elem[2])
    elif elem[0] <= 1:
        return (math.pi - elem[2])
    elif elem[1] >= sizey - 1:
        return 2 * math.pi - elem[2]
    elif elem[1] <= 1:
        return 2 * math.pi - elem[2]
    else:
        return elem[2]



for i in range(elements):
    els.append(
        [sizex / 2, sizey / 2, math.pi * 2 * i / elements, False, (255, 255, 0)])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
    screen.fill((0, 0, 0))
    for i, j in zip(els, range(len(els))):
        pygame.draw.circle(screen, i[4], (int(i[0]), int(i[1])), 2)
        els[j][0] += v * math.cos(i[2])
        els[j][1] += v * math.sin(i[2])

        els[j][2] = curve(els[j][2]) % (math.pi * 2)

        els[j][2] = border(els[j])

    pygame.display.flip()
    time.sleep(0.01)
