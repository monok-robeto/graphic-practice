import pygame
import pygame_gui
import const
import os

PANEL_W = 420
PADDING = 12
_THEME_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "scroller_theme.json")

class TextScroller:
    def __init__(self, manager: pygame_gui.UIManager):
        self.manager = manager
        self.visible = False
        self._lines: list[str] = []
        self._box: pygame_gui.elements.UITextBox | None = None

    def set_lines(self, lines: list[str]):
        """lines: list of HTML strings, e.g. '<b>Title</b>', '<i>note</i>', plain text, or unicode math."""
        self._lines = lines
        if self._box is not None:
            self._rebuild()

    def toggle(self):
        self.visible = not self.visible
        if self.visible:
            self._rebuild()
        else:
            self._destroy()

    def _destroy(self):
        if self._box is not None:
            self._box.kill()
            self._box = None

    def _rebuild(self):
        self._destroy()
        x = const.SCREEN_W - PANEL_W - PADDING
        y = 40
        h = const.SCREEN_H - y - PADDING
        html = "<br>".join(self._lines) if self._lines else "<i>no notes</i>"
        self._box = pygame_gui.elements.UITextBox(
            html_text=html,
            relative_rect=pygame.Rect(x, y, PANEL_W, h),
            manager=self.manager,
        )

    def process_event(self, event: pygame.Event):
        self.manager.process_events(event)

    def update(self, delta_time: float):
        if self.visible:
            self.manager.update(delta_time)

    def draw(self):
        if self.visible:
            self.manager.draw_ui(pygame.display.get_surface())
