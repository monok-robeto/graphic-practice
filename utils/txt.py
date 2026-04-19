import pygame
import app
import const
import utils.color as color
# ---------------------------------------------------------------------------
# Shared font helpers (initialized lazily after pygame.init())
# ---------------------------------------------------------------------------
_fonts = {}
default_font = const.DEFAULT_FONT

def _font(name, size, bold=False, italic=False):
    key = (name, size, bold, italic)
    if key not in _fonts:
        _fonts[key] = pygame.font.SysFont(name, size, bold=bold, italic=italic)
    return _fonts[key]

def label(text, pos, color= color.GREY_0):
    app.surface.blit(_font(default_font, 16).render(text, True, color), pos)

def title(text):
    app.surface.blit(_font(default_font, 22, bold=True).render(text, True, color.WHITE_0), (20, 25))

def hint(text):
    H = app.surface.get_height()
    app.surface.blit(_font(default_font, 16).render(text, True, color.WHITE_1), (20, H - 24))



