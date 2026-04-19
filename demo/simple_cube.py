import app
import math
import utils.draw as draw
import utils.txt as text
import utils.color as color
import pygame
surf = app.surface
CUBE_VERT = [
    # front face  (z = 1)
    (-0.25, -0.25,  1),
    ( 0.25, -0.25,  1),
    ( 0.25,  0.25,  1),
    (-0.25,  0.25,  1),
    # back face   (z = 1.5)
    (-0.25, -0.25,  1.5),
    ( 0.25, -0.25,  1.5),
    ( 0.25,  0.25,  1.5),
    (-0.25,  0.25,  1.5),
]

CUBE_INDICES = [
    # front face
    (0, 1), (1, 2), (2, 3), (3, 0),
    # back face
    (4, 5), (5, 6), (6, 7), (7, 4),
    # connecting edges
    (0, 4), (1, 5), (2, 6), (3, 7),
]
def run():
    text.title("Simple Cube 3D")
    text.label(f"FPS: {app.fps:.1f}   time: {app.time:.2f}s", (20, 50), color.GREEN_0)
    text.hint(f"Đây là simple cube được vẽ từ một screen(project(point))")

    for p in CUBE_VERT:
        draw.point(*p)
    for a, b in CUBE_INDICES:
        draw.line(CUBE_VERT[a], CUBE_VERT[b])









