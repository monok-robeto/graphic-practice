from utils import color
import utils.txt as text
import pygame
import const
import app
import math

NAME = "Oriented Triangle"
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

def line(start_pos, end_pos, col = const.LINE_COL):
    pygame.draw.line(app.surface, col, start_pos, end_pos)
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

def coordinate_x_y_z():
    min_x = (0, const.HALF_H)
    max_x = (const.SCREEN_W, const.HALF_H)
    min_y = (const.HALF_W, 0)
    max_y = (const.HALF_W, const.SCREEN_H)
    line(min_x, max_x, color.WHITE_0)
    line(min_y, max_y, color.WHITE_0)
    horizontal_coordinate()
    vertical_coordinate()

def horizontal_coordinate():
    width = const.COORDINATE_UNIT_SEGMENT_LEN
    unit_amount = const.COORDINATE_UNIT_AMOUNT
    segment_length = int(const.HALF_AXIS_LEN // unit_amount)
    offset_label = 10
    for i in range(-1 * unit_amount, unit_amount, 1):
        a = (const.HALF_W + i * segment_length, const.HALF_AXIS_LEN - width)
        b = (const.HALF_W + i * segment_length, const.HALF_AXIS_LEN + width)
        text.label(f"{i}", (a[0] - width, a[1] + offset_label))
        line(a, b, color.WHITE_0)

def vertical_coordinate():
    width = const.COORDINATE_UNIT_SEGMENT_LEN
    unit_amount = const.COORDINATE_UNIT_AMOUNT
    segment_length = int(const.HALF_AXIS_LEN // unit_amount)
    offset_label_x = 13
    offset_label_y = 11
    for i in range(-1 * unit_amount, unit_amount, 1):
        a = (const.HALF_W - width, const.HALF_AXIS_LEN + i * segment_length)
        b = (const.HALF_W + width, const.HALF_AXIS_LEN + i * segment_length)
        
        text.label(f"{i*-1}", (a[0] + offset_label_x, a[1] - offset_label_y))
        line(a, b, color.WHITE_0)

def run():
    rotate_speed = 0.5
    angle = app.time * math.pi * rotate_speed
    
    for p in CUBE_VERT:
        draw_point(*screen(*project(*translate_z(*rotate_x_z(*p, angle)))))

    for a, b in CUBE_INDICES:
        line(screen(*project(*translate_z(*rotate_x_z(*CUBE_VERT[a], angle)))),
             screen(*project(*translate_z(*rotate_x_z(*CUBE_VERT[b], angle))))
             )
    
    coordinate_x_y_z()
    hints = [
            "Pipeline: rotate (Y - axis) -> translate Z -> perspective divide -> screen map",
            "rotate_x_z: x'= cos(angle) - sin(angle) * z,  z' = sin(angle) * x + cos(angle) * z",
            "project:    px = x/z,  py = y/z   (perspective divide)",
            "screen:     sx = W/2 + px * scale,  sy = H / 2 − py * scale",
            ]
    for i, l in enumerate(hints):
        text.label(l, (1, const.SCREEN_H - (len(hints) - i) * 24))

