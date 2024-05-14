import math, sys, os 

import pygame
# from print_tricks import pt
# from ursina import *
# from icecream import ic

print('inside test.py')

var = math.pi
print(var)

# pt(var)

# ic(var)

# app = Ursina()
# Entity(model='cube', color=color.rgba(1, 0, 0, 1), rotation=(44, 44, 44))
# EditorCamera()
# app.run()



import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))

    rect_surface = pygame.Surface((100,50))
    rect_surface.fill((255, 255, 255))  # Fill the rectangle surface with white color

    size = 0
    while True:
        screen.fill((0, 0, 0))
        size += .1  
        new_rect = pygame.transform.rotate(rect_surface, size)
        screen.blit(new_rect, (0,0))
        pygame.display.flip()

if __name__ == '__main__':
    main()
