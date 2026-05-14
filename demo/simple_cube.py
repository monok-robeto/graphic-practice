import utils.txt as text
import pygame
import const
import app

NAME = "3d Cube"
NOTES = [
    "<b>3D Cube — Static</b>",
    "<font color='#727272'>Tọa độ [0,1] theo tỉ lệ màn hình, chưa phải world space thực.</font>",
    "",
    "Pipeline: <b>translate Z → project → screen</b>",
    "",
    "<b>translate_z</b> — đẩy scene ra xa camera +1.5",
    "  tránh chia cho 0 trong bước project.",
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
    

