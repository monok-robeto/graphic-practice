import pygame
import utils.color as color
import const
import app
import demo

running = True
current_demo_idx = 0
tab_title = pygame.font.SysFont(const.DEFAULT_FONT, 24)

class Demo:
    def __init__(self, name, execute):
        self.name = name
        self.execute = execute


demos = [
        Demo("Test", demo.simple_cube.run),
        Demo("Test2", demo.simple_cube.run),
         ]

def draw_section_tabs(active):
    tab_w = const.SCREEN_W // len(demos)
    tab_h = tab_title.get_height() + 4
    for i, d in enumerate(demos):
        is_active = i == active
        x = i * tab_w
        pygame.draw.rect(app.surface, color.GREEN_0 if is_active else color.GREY_1, (x, 0, tab_w, tab_h))
        label = tab_title.render(d.name, True, color.WHITE_0 if is_active else color.GREY_0)
        lx = x + (tab_w - label.get_width()) // 2
        ly = (tab_h - label.get_height()) // 2
        app.surface.blit(label, (lx, ly))

def handle_events(currentSectionVal):
    keep_running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_q, pygame.K_ESCAPE):
                keep_running = False
            elif event.key == pygame.K_TAB:
                currentSectionVal = (currentSectionVal + 1) % len(demos)
    return keep_running, currentSectionVal




while running == True:
    app.tick()
    running, current_demo_idx = handle_events(current_demo_idx)
    app.surface.fill(color.BLACK)
    draw_section_tabs(current_demo_idx)
    demos[current_demo_idx].execute()
    pygame.display.flip()
    

pygame.quit()
