import color
import pygame
_cached_fonts = {}

def _font(name, size, bold=False, italic=False):
    key = (name, size, bold, italic)
    if key not in _cached_fonts:
        _cached_fonts[key] = pygame.font.SysFont(name, size, bold=bold, italic=italic)
    return _cached_fonts[key]

def label(surf, text, pos, color = color.WHITE_0):
    surf.blit(_font("monospace", 16).render(text, True, color), pos)

def title(surf, text):
    surf.blit(_font("monospace", 22, bold=True).render(text, True, color.WHITE_0), (20, 16))

def hint(surf, text):
    H = surf.get_height()
    surf.blit(_font("monospace", 16).render(text, True, color.WHITE_1), (20, H - 24))

