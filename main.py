import pygame
import pygame_gui
import utils.color as color
import utils.txt as text
import utils.scroller as scroller_mod
import const
import app
import demo

running = True
current_demo_idx = 0
is_pausing = False
tab_title = pygame.font.SysFont(const.DEFAULT_FONT, 24)

import os
_theme = os.path.join(os.path.dirname(__file__), "assets", "scroller_theme.json")
ui_manager = pygame_gui.UIManager((const.SCREEN_W, const.SCREEN_H), theme_path=_theme)
scroller = scroller_mod.TextScroller(ui_manager)

class Demo:
    def __init__(self, module):
        self.name = module.NAME
        self.execute = module.run
        self.notes = getattr(module, "NOTES", [])


demos = [Demo(m) for m in demo.modules]

scroller.set_lines(demos[current_demo_idx].notes)

def draw_section_tabs(active):
    tab_w = const.SCREEN_W // len(demos)
    tab_h = tab_title.get_height() + 4
    for i, d in enumerate(demos):
        is_active = i == active
        x = i * tab_w
        pygame.draw.rect(app.surface, color.GREEN_0 if is_active else color.GREY_1, (x, 0, tab_w, tab_h))
        label = tab_title.render(f"{i + 1}. {d.name}", True, color.WHITE_0 if is_active else color.GREY_0)
        lx = x + (tab_w - label.get_width()) // 2
        ly = (tab_h - label.get_height()) // 2
        app.surface.blit(label, (lx, ly))

def handle_events(currentSectionVal):
    global is_pausing
    keep_running = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_q, pygame.K_ESCAPE):
                keep_running = False
            elif event.key == pygame.K_TAB:
                currentSectionVal = (currentSectionVal + 1) % len(demos)
                scroller.set_lines(demos[currentSectionVal].notes)
            elif event.key == pygame.K_p:
                is_pausing = not is_pausing
            elif event.key == pygame.K_SPACE:
                scroller.toggle()
        scroller.process_event(event)
    return keep_running, currentSectionVal




while running == True:
    running, current_demo_idx = handle_events(current_demo_idx)
    app.tick(is_pausing)
    app.surface.fill(color.BLACK)
    draw_section_tabs(current_demo_idx)
    text.title(f"{current_demo_idx + 1}. {demos[current_demo_idx].name}")
    text.label(f"FPS: {app.fps:.1f}   time: {app.time:.2f}s", (20, 70), color.GREEN_0)
    text.hint("SPACE: notes   P: pause   TAB: next demo")
    demos[current_demo_idx].execute()
    scroller.update(app.delta_time)
    scroller.draw()
    pygame.display.flip()
    

pygame.quit()
