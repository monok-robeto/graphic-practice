import utils.txt as text
import pygame
import const
import app
import math

NAME = "Rotation Cube"
NOTES = [
    "<b>Rotation Cube</b>",
    "",
    "Pipeline: <b>rotate Y → translate Z → project → screen</b>",
    "",
    "<b>rotate_x_z</b> — xoay quanh trục Y trong mặt phẳng X-Z:",
    "  x&#39; = cos(β)·x − sin(β)·z",
    "  z&#39; = sin(β)·x + cos(β)·z",
    "",
    "<b>translate_z</b> — đẩy scene ra xa camera +1.5",
    "",
    "<b>project</b> — perspective divide:",
    "  px = x / z,  py = y / z",
    "",
    "<b>screen</b> — sang tọa độ pixel:",
    "  sx = W/2 + px · scale",
    "  sy = H/2 − py · scale",
]
camera_depth = 1.5
CUBE_VERT = [
    # front face 
    (-0.25, -0.25,  0.25),
    ( 0.25, -0.25,  0.25),
    ( 0.25,  0.25,  0.25),
    (-0.25,  0.25,  0.25),
    # back face 
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
"""
x2​=cosβ⋅x1​−sinβ⋅y1​
y2=sin⁡β⋅x1+cos⁡β⋅y1
"""
def rotate_x_z(x, y, z, angle):
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)
    new_x = cos_angle * x - sin_angle * z
    new_z = sin_angle * x + cos_angle * z
    return new_x, y, new_z

def translate_z(x, y, z):
    return x, y, z + camera_depth

def run():
    rotate_speed = 0.5
    angle = app.time * math.pi * rotate_speed
    
    for p in CUBE_VERT:
        draw_point(*screen(*project(*translate_z(*rotate_x_z(*p, angle)))))

    for a, b in CUBE_INDICES:
        line(screen(*project(*translate_z(*rotate_x_z(*CUBE_VERT[a], angle)))),
             screen(*project(*translate_z(*rotate_x_z(*CUBE_VERT[b], angle))))
             )
    







