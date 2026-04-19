"""
Pygame Rendering Feature Demo
==============================
Press 1-8 to switch between demos. Press Q or close window to quit.

1 - Drawing Primitives
2 - Colors & Alpha / Transparency
3 - Surfaces & Blitting (layering)
4 - Transforms (scale, rotate, flip)
5 - Text Rendering
6 - Animation Loop & Clock (delta time)
7 - Pixel Manipulation (surfarray)
8 - Mouse Drawing + Clipping
"""

import pygame
import pygame_features as demos

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------
pygame.init()
W, H = 900, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pygame Rendering Demo  |  Press 1-8 to switch")
clock = pygame.time.Clock()
font_sm = pygame.font.SysFont("monospace", 16)

# ---------------------------------------------------------------------------
# State
# ---------------------------------------------------------------------------
current_demo = 1
anim_t       = 0.0
mouse_trail  = []

# ---------------------------------------------------------------------------
# Tab bar
# ---------------------------------------------------------------------------
DEMO_NAMES = [
    "1:Primitives", "2:Alpha", "3:Surfaces", "4:Transforms",
    "5:Text", "6:Animation", "7:Pixels", "8:Mouse",
]

def draw_tabs(surf, active):
    tx = W - 10
    for i, name in reversed(list(enumerate(DEMO_NAMES))):
        is_active = (i + 1) == active
        ts = font_sm.render(
            f" {name} ", True,
            demos.BG    if is_active else demos.GRAY,
            demos.WHITE if is_active else (30, 30, 45),
        )
        tx -= ts.get_width() + 2
        surf.blit(ts, (tx, 0))

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
running = True
while running:
    dt = clock.tick(60) / 1000.0
    anim_t += dt
    fps = clock.get_fps()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_q, pygame.K_ESCAPE):
                running = False
            for key, num in [
                (pygame.K_1, 1), (pygame.K_2, 2), (pygame.K_3, 3), (pygame.K_4, 4),
                (pygame.K_5, 5), (pygame.K_6, 6), (pygame.K_7, 7), (pygame.K_8, 8),
            ]:
                if event.key == key:
                    current_demo = num
                    mouse_trail.clear()
        if current_demo == 8:
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                mouse_trail.append(event.pos)
                if len(mouse_trail) > 300:
                    mouse_trail.pop(0)
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_trail.clear()

    screen.fill(demos.BG)
    draw_tabs(screen, current_demo)

    match current_demo:
        case 1: demos.demo_primitives(screen)
        case 2: demos.demo_alpha(screen)
        case 3: demos.demo_surfaces(screen)
        case 4: demos.demo_transforms(screen, anim_t)
        case 5: demos.demo_text(screen)
        case 6: demos.demo_animation(screen, anim_t, fps)
        case 7: demos.demo_pixels(screen, anim_t)
        case 8: demos.demo_mouse(screen, mouse_trail)

    pygame.display.flip()

pygame.quit()
