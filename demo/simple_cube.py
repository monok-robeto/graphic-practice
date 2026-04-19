

import utils.txt as text
import pygame
import const
import app
import math

NAME = "3d Cube"
camera_depth = 1.5
CUBE_VERT = [
    # front face  (z = 1)
    (-0.25, -0.25,  0.25),
    ( 0.25, -0.25,  0.25),
    ( 0.25,  0.25,  0.25),
    (-0.25,  0.25,  0.25),
    # back face   (z = 1.5)
    (-0.25, -0.25,  -0.25),
    ( 0.25, -0.25,  -0.25),
    ( 0.25,  0.25,  -0.25),
    (-0.25,  0.25,  -0.25),
]

CUBE_INDICES = [
    # front face
    (0, 1), (1, 2), (2, 3), (3, 0),
    # back face
    (4, 5), (5, 6), (6, 7), (7, 4),
    # connecting edges
    (0, 4), (1, 5), (2, 6), (3, 7),
]

def project(x, y, z):
    px = x/z
    py = y/z
    return px, py, z

def screen(x, y, z):
    sx = const.HALF_W + x * const.MAX_AXIS_LEN
    sy = const.HALF_H - y * const.MAX_AXIS_LEN
    return sx, sy


def vector(x, y, z):
    return x, y, z

def draw_point(x, y):
    pygame.draw.circle(app.surface, const.POINT_COL, (x, y), const.POINT_RADIUS, const.POINT_RADIUS)

def line(start_pos, end_pos):
    pygame.draw.line(app.surface, const.LINE_COL, start_pos, end_pos)


def translate_z(x, y, z):
    return x, y, z + camera_depth

def run():
    for p in CUBE_VERT:
        draw_point(*screen(*project(*translate_z(*p))))
    for a, b in CUBE_INDICES:
        line(screen(*project(*translate_z(*CUBE_VERT[a]))),
             screen(*project(*translate_z(*CUBE_VERT[b])))
             )
    
    hints = [
            "Pipeline: translate Z → perspective divide → screen map",
            "project:    px=x/z,  py=y/z   (perspective divide)",
            "screen:     sx=W/2+px·scale,  sy=H/2−py·scale",
            ]
    for i, l in enumerate(hints):
        text.label(l, (1, const.SCREEN_H - (len(hints) - i) * 24))













