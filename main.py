import pygame

# Khởi tạo
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rendering Playground")

# Màu sắc (R, G, B)
BLACK  = (0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255, 0,   0)
GREEN  = (0,   200, 100)
BLUE   = (50,  100, 255)

screen.fill(BLACK)

# Vẽ điểm
pygame.draw.circle(screen, WHITE, (100, 100), 3)

# Vẽ đường thẳng
pygame.draw.line(screen, RED, (50, 200), (250, 200), 2)

# Vẽ tam giác (polygon)
pygame.draw.polygon(screen, GREEN, [(300, 300), (400, 150), (500, 300)])

# Vẽ hình chữ nhật (outline)
pygame.draw.rect(screen, BLUE, (350, 50, 150, 100), 2)

pygame.display.flip()

# Giữ cửa sổ mở
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
