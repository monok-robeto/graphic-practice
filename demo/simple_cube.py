import utils.draw as draw

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
    for p in CUBE_VERT:
        draw.point(*p)
    for a, b in CUBE_INDICES:
        draw.line(CUBE_VERT[a], CUBE_VERT[b])
