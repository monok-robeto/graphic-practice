import pygame
import const
import app


surface = app.surface
def project(x, y, z):
    px = x/z
    py = y/z
    return px, py, z

def screen(x, y, z):
    sx = const.CENTER_W + x * const.CENTER_W
    sy = const.CENTER_H - y * const.CENTER_H
    return sx, sy, z


def vector(x, y, z):
    return x, y, z

def point(x, y, z):
    sx, sy, _= screen(*project(x, y, z))
    pygame.draw.circle(surface, const.POINT_COL, (sx, sy), const.POINT_RADIUS, const.POINT_RADIUS)

def line(start_pos, end_pos):
    ax, ay, _ = screen(*project(*start_pos))
    bx, by, _ = screen(*project(*end_pos))  
    pygame.draw.line(surface, const.LINE_COL, (ax, ay), (bx, by))
