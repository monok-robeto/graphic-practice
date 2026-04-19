import math
import pygame
import pygame.gfxdraw
import numpy as np

# ---------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------
BG      = (15,  15,  25)
WHITE   = (255, 255, 255)
GRAY    = (120, 120, 130)
RED     = (220,  60,  60)
GREEN   = ( 60, 200, 100)
BLUE    = ( 60, 120, 255)
CYAN    = (  0, 220, 220)
YELLOW  = (255, 210,  50)
ORANGE  = (255, 140,  30)
MAGENTA = (200,  60, 200)

# ---------------------------------------------------------------------------
# Shared font helpers (initialized lazily after pygame.init())
# ---------------------------------------------------------------------------
_fonts = {}

def _font(name, size, bold=False, italic=False):
    key = (name, size, bold, italic)
    if key not in _fonts:
        _fonts[key] = pygame.font.SysFont(name, size, bold=bold, italic=italic)
    return _fonts[key]

def label(surf, text, pos, color=GRAY):
    surf.blit(_font("monospace", 16).render(text, True, color), pos)

def title(surf, text):
    surf.blit(_font("monospace", 22, bold=True).render(text, True, WHITE), (20, 16))

def hint(surf, text):
    H = surf.get_height()
    surf.blit(_font("monospace", 16).render(text, True, GRAY), (20, H - 24))


# ===========================================================================
# Demo 1 — Drawing Primitives
# ===========================================================================
def demo_primitives(surf):
    title(surf, "1 · Drawing Primitives")
    hint(surf, "pygame.draw.*  — the basic building blocks")

    for i in range(5):
        pygame.draw.circle(surf, WHITE, (80 + i * 6, 90), 1)
    label(surf, "pixels (circle r=1)", (60, 100))

    pygame.draw.line(surf, RED, (60, 160), (260, 160), 3)
    label(surf, "line (width=3)", (60, 168))

    pygame.draw.aaline(surf, CYAN, (60, 200), (260, 185))
    label(surf, "aaline (anti-aliased)", (60, 205))

    pts = [(300 + i * 30, 150 + int(40 * math.sin(i))) for i in range(8)]
    pygame.draw.lines(surf, YELLOW, False, pts, 2)
    label(surf, "lines (polyline)", (300, 205))

    pygame.draw.rect(surf, BLUE, (60, 250, 140, 80))
    label(surf, "rect (filled)", (60, 338))

    pygame.draw.rect(surf, ORANGE, (230, 250, 140, 80), 3)
    label(surf, "rect (outline w=3)", (230, 338))

    pygame.draw.rect(surf, GREEN, (400, 250, 140, 80), border_radius=20)
    label(surf, "rect (border_radius)", (400, 338))

    pygame.draw.circle(surf, MAGENTA, (630, 290), 50)
    label(surf, "circle filled", (595, 348))

    pygame.draw.circle(surf, CYAN, (750, 290), 50, 3)
    label(surf, "circle outline", (715, 348))

    pygame.draw.ellipse(surf, YELLOW, (60, 400, 180, 90))
    label(surf, "ellipse", (120, 500))

    poly = [(310, 490), (360, 400), (410, 430), (430, 490)]
    pygame.draw.polygon(surf, RED, poly)
    label(surf, "polygon", (340, 500))

    pygame.draw.arc(surf, ORANGE, (500, 400, 160, 100), 0, math.pi, 4)
    label(surf, "arc (half circle)", (510, 510))

    pygame.gfxdraw.aacircle(surf, 760, 450, 50, CYAN)
    pygame.gfxdraw.filled_circle(surf, 760, 450, 50, (0, 200, 200, 80))
    label(surf, "gfxdraw aacircle", (710, 508))


# ===========================================================================
# Demo 2 — Colors & Alpha / Transparency
# ===========================================================================
def demo_alpha(surf):
    title(surf, "2 · Colors & Alpha / Transparency")
    hint(surf, "Surface.set_alpha()  and  SRCALPHA surfaces")

    label(surf, "Surface.set_alpha(0..255):", (40, 60))
    for i in range(10):
        s = pygame.Surface((60, 60))
        s.fill(BLUE)
        s.set_alpha(int(255 * (i + 1) / 10))
        surf.blit(s, (40 + i * 68, 80))

    label(surf, "SRCALPHA surface (per-pixel alpha):", (40, 170))
    for i in range(10):
        s = pygame.Surface((60, 60), pygame.SRCALPHA)
        s.fill((220, 60, 60, int(255 * (i + 1) / 10)))
        surf.blit(s, (40 + i * 68, 190))

    label(surf, "Overlapping transparent shapes:", (40, 280))
    for i, c in enumerate([RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]):
        s = pygame.Surface((120, 120), pygame.SRCALPHA)
        pygame.draw.circle(s, (*c, 100), (60, 60), 60)
        surf.blit(s, (40 + i * 55, 300))

    for i, line in enumerate([
        "RGB  = (R, G, B)          — no transparency",
        "RGBA = (R, G, B, A)        — A=0 invisible, A=255 opaque",
        "set_alpha(a)               — applies to whole surface",
        "SRCALPHA flag              — enables per-pixel alpha",
        "pygame.Color(r,g,b,a)      — color object with helpers",
    ]):
        label(surf, line, (40, 440 + i * 22), WHITE)

    c = pygame.Color(0)
    c.hsva = (200, 80, 100, 100)
    pygame.draw.circle(surf, c, (800, 460), 55)
    label(surf, "Color via HSV", (757, 520))


# ===========================================================================
# Demo 3 — Surfaces & Blitting
# ===========================================================================
def demo_surfaces(surf):
    title(surf, "3 · Surfaces & Blitting (Layer Compositing)")
    hint(surf, "Surface  =  an image buffer. blit() paints one onto another.")

    bg = pygame.Surface((860, 480))
    bg.fill((20, 30, 60))
    pygame.draw.rect(bg, (30, 50, 100), (0, 0, 860, 480), 6)
    label(bg, "Layer 0: background surface", (10, 10), GRAY)

    mid = pygame.Surface((400, 240), pygame.SRCALPHA)
    mid.fill((0, 0, 0, 0))
    pygame.draw.ellipse(mid, (*GREEN, 180), (0, 0, 400, 240))
    label(mid, "Layer 1: translucent ellipse (SRCALPHA)", (30, 100), WHITE)

    top = pygame.Surface((180, 180), pygame.SRCALPHA)
    sz = 20
    for row in range(9):
        for col in range(9):
            color = (255, 210, 50, 200) if (row + col) % 2 == 0 else (0, 0, 0, 0)
            pygame.draw.rect(top, color, (col * sz, row * sz, sz, sz))
    label(top, "Layer 2", (4, 4), WHITE)

    bg.blit(mid, (220, 120))
    bg.blit(top, (580, 150))
    surf.blit(bg, (20, 80))

    pygame.draw.rect(surf, RED, (20, 80, 200, 100), 2)
    label(surf, "<-- subsurface (red border)", (230, 118), RED)
    label(surf, "subsurface() — a zero-copy view into a region:", (20, 570), WHITE)


# ===========================================================================
# Demo 4 — Transforms
# ===========================================================================
def demo_transforms(surf, t):
    title(surf, "4 · Transforms  (scale · rotate · flip)")
    hint(surf, "pygame.transform.*  — non-destructive image transforms")

    src = pygame.Surface((120, 80), pygame.SRCALPHA)
    src.fill((0, 0, 0, 0))
    pygame.draw.rect(src, BLUE, (0, 0, 120, 80), border_radius=12)
    pygame.draw.rect(src, CYAN, (10, 10, 100, 60), border_radius=8)
    label(src, "SOURCE", (28, 28), WHITE)

    surf.blit(src, (60, 90))
    label(surf, "original  120x80", (55, 180))

    surf.blit(pygame.transform.scale(src, (240, 160)), (220, 90))
    label(surf, "scale  240x160", (220, 265))

    surf.blit(pygame.transform.smoothscale(src, (60, 40)), (500, 110))
    label(surf, "smoothscale  60x40", (487, 165))

    angle = (t * 90) % 360
    rotated = pygame.transform.rotate(src, angle)
    rw, rh = rotated.get_size()
    surf.blit(rotated, (660 - rw // 2, 160 - rh // 2))
    label(surf, f"rotate {angle:.0f}°  (animated)", (620, 240))

    surf.blit(pygame.transform.flip(src, True,  False), (60,  340))
    surf.blit(pygame.transform.flip(src, False, True),  (240, 340))
    surf.blit(pygame.transform.flip(src, True,  True),  (420, 340))
    label(surf, "flip horizontal", (48,  430))
    label(surf, "flip vertical",   (240, 430))
    label(surf, "flip both",       (432, 430))

    surf.blit(pygame.transform.chop(src, pygame.Rect(0, 0, 40, 40)), (620, 340))
    label(surf, "chop (crop top-left)", (600, 430))


# ===========================================================================
# Demo 5 — Text Rendering
# ===========================================================================
def demo_text(surf):
    title(surf, "5 · Text Rendering")
    hint(surf, "pygame.font  — system fonts, TTF fonts, anti-aliasing")

    y = 70
    for size, name in [(18, "small 18px"), (28, "medium 28px"), (42, "large 42px"), (64, "huge 64px")]:
        surf.blit(_font("monospace", size).render(name, True, WHITE), (40, y))
        y += size + 14

    f = _font("serif", 36)
    surf.blit(f.render("Anti-aliased (True)",  True,  CYAN),   (40, 310))
    surf.blit(f.render("Aliased (False)",       False, RED),    (40, 355))

    txt_surf = _font("monospace", 28).render("  text with bg color  ", True, BG, YELLOW)
    surf.blit(txt_surf, (40, 408))

    surf.blit(_font("serif", 32, bold=True).render("Bold text",   True, ORANGE),  (40,  458))
    surf.blit(_font("serif", 32, italic=True).render("Italic text", True, MAGENTA), (220, 458))

    f3 = _font("monospace", 20)
    msg = "Measured string — width fits a box"
    tw, th = f3.size(msg)
    box = pygame.Rect(480, 300, tw + 20, th + 12)
    pygame.draw.rect(surf, GREEN, box, 2)
    surf.blit(f3.render(msg, True, GREEN), (box.x + 10, box.y + 6))
    label(surf, f"font.size() = {tw}x{th}px", (480, 340))

    label(surf, "pygame.font.get_fonts()  — lists all system font names",  (480, 380), GRAY)
    label(surf, "pygame.font.Font('file.ttf', size)  — load TTF file",     (480, 402), GRAY)


# ===========================================================================
# Demo 6 — Animation Loop & Clock
# ===========================================================================
def demo_animation(surf, t, fps):
    title(surf, "6 · Animation Loop & Clock  (delta time)")
    hint(surf, "clock.tick(fps) → dt_ms   Use dt to decouple speed from framerate.")

    W, H = surf.get_size()
    cx, cy = W // 2, H // 2

    label(surf, f"FPS: {fps:.1f}   time: {t:.2f}s", (20, 50), YELLOW)

    for i in range(6):
        angle = t * (0.8 + i * 0.15) + i * (math.tau / 6)
        radius = 80 + i * 28
        x = int(cx + radius * math.cos(angle))
        y = int(cy + radius * math.sin(angle))
        r = 10 + i * 4
        c = pygame.Color(0)
        c.hsva = ((i / 6 * 360) % 360, 90, 100, 100)
        pygame.draw.circle(surf, c, (x, y), r)
        for j in range(1, 6):
            ta = angle - j * 0.15
            tx = int(cx + radius * math.cos(ta))
            ty = int(cy + radius * math.sin(ta))
            tc = pygame.Color(0)
            tc.hsva = ((i / 6 * 360) % 360, 90, 100, 100)
            tr = max(1, r - j * 2)
            s = pygame.Surface((tr * 2, tr * 2), pygame.SRCALPHA)
            pygame.draw.circle(s, (*tc[:3], max(0, 40 - j * 6)), (tr, tr), tr)
            surf.blit(s, (tx - tr, ty - tr))

    pulse_r = int(30 + 15 * math.sin(t * 3))
    pygame.draw.circle(surf, WHITE, (cx, cy), pulse_r)
    pygame.draw.circle(surf, BG,    (cx, cy), pulse_r - 4)

    bx = int((t * 120) % W)
    by = int(cy - 200 + 60 * abs(math.sin(t * 2)))
    pygame.draw.rect(surf, ORANGE, (bx - 15, by - 15, 30, 30))
    label(surf, "bouncing rect", (bx - 35, by + 20), ORANGE)

    for i, line in enumerate([
        "clock = pygame.time.Clock()",
        "dt = clock.tick(60)   # ms since last frame",
        "speed = 200  # px/s",
        "x += speed * dt / 1000  # framerate-independent",
    ]):
        label(surf, line, (20, H - 120 + i * 22), GRAY)


# ===========================================================================
# Demo 7 — Pixel Manipulation
# ===========================================================================
def demo_pixels(surf, t):
    title(surf, "7 · Pixel Manipulation  (pygame.surfarray + numpy)")
    hint(surf, "surfarray gives a numpy view of raw pixel data — no copy.")

    pw, ph = 512, 400
    pixel_surf = pygame.Surface((pw, ph))
    arr = pygame.surfarray.pixels3d(pixel_surf)

    xs = np.arange(pw)
    ys = np.arange(ph)
    xx, yy = np.meshgrid(xs, ys, indexing='ij')

    v = (
        np.sin(xx / 30 + t * 2) +
        np.sin(yy / 30 + t * 1.5) +
        np.sin((xx + yy) / 40 + t) +
        np.sin(np.sqrt((xx - pw/2)**2 + (yy - ph/2)**2) / 20 - t * 2)
    ) / 4

    arr[:, :, 0] = ((np.sin(v * math.pi)         + 1) * 127).astype(np.uint8)
    arr[:, :, 1] = ((np.sin(v * math.pi + 2.094) + 1) * 127).astype(np.uint8)
    arr[:, :, 2] = ((np.sin(v * math.pi + 4.189) + 1) * 127).astype(np.uint8)
    del arr

    surf.blit(pixel_surf, (20, 80))

    for i, line in enumerate([
        "arr = pygame.surfarray.pixels3d(surf)   # numpy uint8 array (W,H,3)",
        "arr[:,:,0] = red_values                 # set all red channels",
        "del arr                                 # release pixel lock!",
        "pygame.surfarray.blit_array(surf, arr)  # alternative path",
    ]):
        label(surf, line, (548, 200 + i * 24), GRAY)


# ===========================================================================
# Demo 8 — Mouse Drawing & Clipping
# ===========================================================================
def demo_mouse(surf, trail):
    title(surf, "8 · Mouse Drawing + Clipping")
    hint(surf, "Hold left mouse button to draw. Clipping restricts rendering to the green box.")

    H = surf.get_height()
    clip_rect = pygame.Rect(200, 80, 500, 440)
    pygame.draw.rect(surf, GREEN, clip_rect, 2)
    label(surf, "clip region", (clip_rect.right - 90, clip_rect.top + 4), GREEN)

    surf.set_clip(clip_rect)
    if len(trail) >= 2:
        pygame.draw.lines(surf, CYAN, False, trail, 3)
    for i, (px, py) in enumerate(trail):
        r = max(2, 8 - int(8 * i / max(len(trail), 1)))
        c = pygame.Color(0)
        c.hsva = ((i * 4) % 360, 90, 100, 100)
        pygame.draw.circle(surf, c, (px, py), r)
    surf.set_clip(None)

    for i, line in enumerate([
        "surf.set_clip(rect)   # restrict drawing to rect",
        "surf.set_clip(None)   # remove clip",
        "pygame.mouse.get_pos()   # (x, y)",
        "pygame.mouse.get_pressed()  # (L, M, R)",
        "event.type == pygame.MOUSEMOTION",
        "event.type == pygame.MOUSEBUTTONDOWN",
    ]):
        label(surf, line, (20, H - 150 + i * 22), GRAY)







