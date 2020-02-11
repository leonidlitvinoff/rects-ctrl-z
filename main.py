import pygame

pygame.init()
size = width, height = 501, 501
screen = pygame.display.set_mode(size)
coord = [250, 250]
target = [250, 250]
running = True
positions = []
rects = []
last = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color('black'))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z] and keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL] and keys[pygame.K_z]:
        last = 1
    else:
        if last == 1:
            last = 0
            if len(rects) > 0:
                del rects[-1]
    if pygame.mouse.get_pressed()[0]:
        positions.append(pygame.mouse.get_pos())
    else:
        if len(positions) != 0:
            rects.append([positions[0], positions[-1]])
            positions = []
    if len(positions) >= 2:
        pygame.draw.rect(screen, (255, 255, 255), (positions[0][0], positions[0][1], -(positions[0][0] - positions[-1][0]), -(positions[0][1] - positions[-1][1])), 5)
    for i in rects:
        pygame.draw.rect(screen, (255, 255, 255), (
        i[0][0], i[0][1], -(i[0][0] - i[-1][0]), -(i[0][1] - i[-1][1])),
                         5)
    pygame.display.flip()
pygame.quit()