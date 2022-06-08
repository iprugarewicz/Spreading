import pygame
import sys
import random
import math
import time


pygame.init()

sim_time = 0

element_count = 200
infected = 0
elements = []
v = 1
sizeX = 400
sizeY = 400

screen = pygame.display.set_mode((2*sizeX, sizeY))
pygame.display.set_caption('Virus spreading simulation')

def curve(alpha):
    return alpha + ((math.pi / 4) * ((random.randrange(101) + random.randrange(101)) / 201)) - (math.pi / 8)


def border(elem):
    if elem[0] >= sizeX - 1 or elem[0] <= 1:
        return math.pi - elem[2]
    elif elem[1] >= sizeY - 1:
        return 2 * math.pi - elem[2]
    elif elem[1] <= 1:
        return 2 * math.pi - elem[2]
    else:
        return elem[2]


for i in range(element_count):
    elements.append(
        [sizeX / 2, sizeY / 2, math.pi * 2 * i / element_count, False, (255, 255, 0)])
elements[0][3] = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,0,sizeX+3,sizeY))

    for i, j in zip(elements, range(len(elements))):

        # position
        elements[j][0] += v * math.cos(i[2])
        elements[j][1] += v * math.sin(i[2])

        # angle
        elements[j][2] = curve(elements[j][2]) % (math.pi * 2)

        # border bounce
        elements[j][2] = border(elements[j])

        # spreading
        if sim_time >= 100:
            for elem in elements:
                if i[3] == True and ((elem[0] - i[0]) ** 2) + ((elem[1] - i[1]) ** 2) <= 5:
                    if elements[elements.index(elem)][3]==False:
                        infected+=1
                    elements[elements.index(elem)][3] = True

        # coloring
        if i[3]:
            elements[j][4] = (255, 0, 0)

        pygame.draw.circle(screen, i[4], (int(i[0]), int(i[1])), 2)

    pygame.draw.circle(screen, (255,255,255), ((sizeX+(sim_time/5)%sizeX),sizeY- sizeY*(infected/element_count)),1)

    pygame.display.flip()
    time.sleep(0.01)
    sim_time+=1
