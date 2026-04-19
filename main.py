import pygame
import utils.color as color
SCREEN_W, SCREEN_H = 1280, 720
DEMO_SECTIONS = ["pygame feautures", "My Demo"]

POINT_COL = color.GREEN_1
POINT_RADIUS = 3
POINT_WIDTH = 3
CENTER_W = SCREEN_W/2
CENTER_H = SCREEN_H/2
running = True
current_section = 0

pygame.init()
default_font = pygame.font.match_font('monospace')
text = pygame.font.SysFont(default_font, 24)
surface = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Rendering Demo")

def draw_section_tabs(surf, active):
    tab_w = SCREEN_W // len(DEMO_SECTIONS)
    tab_h = text.get_height() + 4
    for i, name in enumerate(DEMO_SECTIONS):
        is_active = i == active
        x = i * tab_w
        pygame.draw.rect(surf, color.GREEN_0 if is_active else color.GREY_1, (x, 0, tab_w, tab_h))
        label = text.render(name, True, color.WHITE_0 if is_active else color.GREY_0)
        lx = x + (tab_w - label.get_width()) // 2
        ly = (tab_h - label.get_height()) // 2
        surf.blit(label, (lx, ly))

def handle_events(currentSectionVal):
    keep_running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_q, pygame.K_ESCAPE):
                keep_running = False
            elif event.key == pygame.K_TAB:
                currentSectionVal = (currentSectionVal + 1) % len(DEMO_SECTIONS)
    return keep_running, currentSectionVal

def draw_point( x, y, z):
    pygame.draw.circle(surface, POINT_COL, (x, y), POINT_RADIUS, POINT_WIDTH)

def to_screen(x, y, z):
    sx = CENTER_W + x * CENTER_W
    sy = CENTER_H - y * CENTER_H
    return sx, sy, z

def project(x, y, z):
    px = x/z
    py = y/z
    return px, py, z

def vector(x, y, z):
    return x, y, z

CUBE_VERT = [
    # front face  (z = 1)
    vector(-0.25, -0.25,  1),
    vector( 0.25, -0.25,  1),
    vector( 0.25,  0.25,  1),
    vector(-0.25,  0.25,  1),
    # back face   (z = 1.5)
    vector(-0.25, -0.25,  1.5),
    vector( 0.25, -0.25,  1.5),
    vector( 0.25,  0.25,  1.5),
    vector(-0.25,  0.25,  1.5),
]

CUBE_INDICES = [
    # front face
    (0, 1), (1, 2), (2, 3), (3, 0),
    # back face
    (4, 5), (5, 6), (6, 7), (7, 4),
    # connecting edges
    (0, 4), (1, 5), (2, 6), (3, 7),
]

while running == True:
    running, current_section = handle_events(current_section)
    draw_section_tabs(surface, current_section)
    for p in CUBE_VERT:
        draw_point(*to_screen(*project(*p)))
    for a, b in CUBE_INDICES:
        ax, ay, _ = to_screen(*project(*CUBE_VERT[a]))
        bx, by, _ = to_screen(*project(*CUBE_VERT[b]))
        pygame.draw.line(surface, POINT_COL, (ax, ay), (bx, by))
    pygame.display.flip()
    


pygame.quit()
