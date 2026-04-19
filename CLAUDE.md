# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

A Python/Pygame learning sandbox for mastering 2D graphics concepts before building a 3D game with Rust + WGPU. Each demo isolates one rendering concept.

## Commands

```bash
# Run the interactive demo app
uv run python main.py

# Install dependencies
uv sync

# Type-check
uv run pyright
```

**Controls:** Keys `1–8` switch demos, `Q`/`ESC` quits, hold left mouse button in demo 8 to draw.

## Architecture

Two files, no abstraction layers:

- **`main.py`** — Pygame init, 60 FPS event loop, tab-bar UI, routes `current_demo` via `match`/`case` to the appropriate demo function. Owns `anim_t` (accumulated seconds) and `mouse_trail` (list of positions), passing them into stateful demos.
- **`demos.py`** — All 8 demo functions. Each is `demo_*(surf, ...)` and renders directly to the surface passed in. Shared helpers: `_font()` (lazy font cache), `label()`, `title()`, `hint()`.

### Demo inventory

| Key | Demo | Core concept |
|-----|------|-------------|
| 1 | Primitives | `pygame.draw.*`, `pygame.gfxdraw` |
| 2 | Alpha | `set_alpha()`, `SRCALPHA`, HSV color |
| 3 | Surfaces | Multi-layer `blit()`, `SRCALPHA` compositing |
| 4 | Transforms | `scale`, `smoothscale`, `rotate`, `flip`, `chop` |
| 5 | Text | `SysFont`, anti-aliasing, `font.size()` |
| 6 | Animation | Delta-time clock, orbital particles, `math.tau` |
| 7 | Pixels | `surfarray.pixels3d()` → numpy uint8 array, sine plasma |
| 8 | Mouse | `set_clip()`, `MOUSEMOTION` trail |

### Adding a new demo

1. Add a `demo_name(surf, ...)` function to `demos.py`
2. Add its label to `DEMO_NAMES` in `main.py`
3. Add a `case N:` branch in the `match current_demo` block

## Graphics Roadmap (Pygame → Rust/WGPU)

### Phase 1 — 2D foundations (this repo)
- [x] Primitives, blending, surface compositing
- [x] Transforms, text, delta-time animation
- [x] Pixel-level manipulation (numpy surfarray)
- [ ] Sprite sheets & tile maps
- [ ] Camera / viewport scrolling
- [ ] Scene graph / dirty-rect rendering

### Phase 2 — Math & linear algebra
- Vectors, matrices, dot/cross products
- Homogeneous coordinates & affine transforms
- Quaternions for 3D rotation
- Resources: *3Blue1Brown Linear Algebra* series, *immersive-linear-algebra.com*

### Phase 3 — GPU pipeline concepts (no API yet)
- Rasterization pipeline: vertex → primitive assembly → fragment → framebuffer
- Depth buffer (z-buffer), back-face culling, winding order
- UV mapping & texture sampling, mipmaps
- Lighting: Phong model (ambient + diffuse + specular), normals
- Resources: *scratchapixel.com*, *learnopengl.com* (concepts transfer to WGPU)

### Phase 4 — Rust + WGPU basics
- WGPU device/queue/surface setup, swap-chain loop
- Vertex/index buffers, WGSL shaders
- Uniform buffers for camera (view/projection matrices)
- Texture loading & bind groups
- Resources: *sotrh/learn-wgpu* tutorial, *wgpu examples* in the repo

### Phase 5 — 3D rendering
- Perspective projection, model/view/projection (MVP) matrix
- OBJ/GLTF mesh loading
- Normal mapping, shadow mapping
- Instanced rendering for large scene counts

### Phase 6 — Simulation
- **Fluid (grid):** Euler grid, pressure solve, advection (Jos Stam "Stable Fluids")
- **Fluid (particles):** SPH (Smoothed Particle Hydrodynamics)
- **Rigid body:** AABB/SAT collision, impulse resolution
- GPU compute shaders via WGPU compute pipelines for parallel simulation
- Resources: *Ten Minute Physics* (YouTube), *pozero/fluid-sim* references
