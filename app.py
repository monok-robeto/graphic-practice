import pygame
import const
pygame.init()
surface = pygame.display.set_mode((const.SCREEN_W, const.SCREEN_H))
pygame.display.set_caption(const.SURFACE_TITLE)
clock = pygame.time.Clock()

delta_time = 0
time = 0
fps = 0

def tick():
    global delta_time, fps, time
    delta_time = clock.tick(60) / 1000.0
    time += delta_time
    fps = clock.get_fps()
