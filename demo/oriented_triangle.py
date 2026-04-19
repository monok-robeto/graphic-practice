from utils import color
import utils.txt as text
import pygame
import const
import app
import math

NAME = "Oriented Triangle"
camera_depth = 1.5
rotate_speed = 0.5

CUBE_VERT = [
    # front face 
    (-0.5, -0.5,  0.5),
    ( 0.5, -0.5,  0.5),
    ( 0.5,  0.5,  0.5),
    (-0.5,  0.5,  0.5),

    # back face 
    (-0.5, -0.5,  -0.5),
    ( 0.5, -0.5,  -0.5),
    ( 0.5,  0.5,  -0.5),
    (-0.5,  0.5,  -0.5),
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
    sx = 0.0
    sy = 0.0
    
    # if x > 1: sx= const.HALF_W + x
    # else: sx = const.HALF_W + x * const.HALF_AXIS_LEN
    #
    # if y > 1: sy = const.HALF_H + y
    # else: sy = const.HALF_H - y * const.HALF_AXIS_LEN
    # sx= const.HALF_W + x
    # sy = const.HALF_H + y
    sx = const.HALF_W + x * const.HALF_AXIS_LEN

    sy = const.HALF_H - y * const.HALF_AXIS_LEN
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

def world_to_screen(x, y, z):
    angle = app.time * math.pi * rotate_speed
    x, y = screen(*project(*translate_z(*(rotate_x_z(x, y, z, angle)))))
    return (x, y)

def coordinate_x_y_z():
    min_x = (-1, 0, 0)
    max_x = (1, 0, 0)
    min_y = (0, -1, 0)
    max_y = (0, 1, 0)
    min_z = (0, 0, -1)
    max_z = (0, 0, 1)
    
    line(world_to_screen(*min_x), world_to_screen(*max_x), color.WHITE_0)
    line(world_to_screen(*min_y), world_to_screen(*max_y), color.WHITE_0)
    line(world_to_screen(*min_z), world_to_screen(*max_z), color.WHITE_0)

    sx_min_x, sy_min_x = world_to_screen(*min_x)
    sx_max_x, sy_max_x = world_to_screen(*max_x)
    
    sx_min_y, sy_min_y = world_to_screen(*min_y)
    sx_max_y, sy_max_y = world_to_screen(*max_y)

    sx_min_z, sy_min_z = world_to_screen(*min_z)
    sx_max_z, sy_max_z = world_to_screen(*max_z)

    text.label_bold("-X", (sx_min_x, sy_min_x), color.PINK_0)
    text.label_bold("X", (sx_max_x, sy_max_x), color.PINK_0)

    text.label_bold("Y", (sx_max_y, sy_max_y), color.YELLOW_0)
    text.label_bold("-Y", (sx_min_y, sy_min_y), color.YELLOW_0)

    text.label_bold("-Z", (sx_min_z, sy_min_z), color.BLUE_0)
    text.label_bold("Z", (sx_max_z, sy_max_z), color.BLUE_0)
    horizontal_coordinate()
    vertical_coordinate()
    depth_coordinate()

def depth_coordinate():
    width = const.COORDINATE_UNIT_SEGMENT_LEN / const.HALF_AXIS_LEN
    unit_amount = const.COORDINATE_UNIT_AMOUNT
    segment_length = 1 / unit_amount
    offset_label_x = -10
    offset_label_y = 30
    for i in range(-1 * unit_amount, unit_amount + 1, 1):
        # a = (-width, 0, i * segment_length)
        # b = (+width, 0,i * segment_length)
        a = (0, -width, i * segment_length)
        b = (0, +width,i * segment_length)
        screen_a = world_to_screen(*a)
        text.label(f"{-1*i}", (screen_a[0] + offset_label_x, screen_a[1] - offset_label_y))
        line(screen_a, world_to_screen(*b), color.WHITE_0)
        

def horizontal_coordinate():
    width = const.COORDINATE_UNIT_SEGMENT_LEN/ const.HALF_AXIS_LEN
    unit_amount = const.COORDINATE_UNIT_AMOUNT
    segment_length = 1 / unit_amount
    offset_label = 10
    for i in range(-1 * unit_amount, unit_amount + 1, 1):
        a = ( i * segment_length, -width, 0)
        b = (i * segment_length, width, 0)
        screen_a = world_to_screen(*a)
        text.label(f"{i}", (screen_a[0] - width, screen_a[1] + offset_label))
        line(screen_a, world_to_screen(*b), color.WHITE_0)

def vertical_coordinate():
    width = const.COORDINATE_UNIT_SEGMENT_LEN / const.HALF_AXIS_LEN
    unit_amount = const.COORDINATE_UNIT_AMOUNT
    segment_length = 1 / unit_amount
    offset_label_x = 13
    offset_label_y = 11
    for i in range(-1 * unit_amount, unit_amount + 1, 1):
        a = (- width, i * segment_length, 0)
        b = (+ width, i * segment_length, 0)
        
        screen_a = world_to_screen(*a)
        text.label(f"{i*-1}", (screen_a[0] + offset_label_x, screen_a[1] - offset_label_y))
        line(screen_a, world_to_screen(*b), color.WHITE_0)

def run():
    angle = app.time * math.pi * rotate_speed
    
    for p in CUBE_VERT:
        draw_point(*screen(*project(*translate_z(*rotate_x_z(*p, angle)))))

    for a, b in CUBE_INDICES:
        line(screen(*project(*translate_z(*rotate_x_z(*CUBE_VERT[a], angle)))),
             screen(*project(*translate_z(*rotate_x_z(*CUBE_VERT[b], angle))))
             )
    
    coordinate_x_y_z()
    hints = [
            "",
            "",
            ]
    for i, l in enumerate(hints):
        text.label(l, (1, const.SCREEN_H - (len(hints) - i) * 24))

