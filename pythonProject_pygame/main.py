import pygame


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Побег из тюрьмы')
pygame.display.set_icon(pygame.image.load('icon.png'))
speed = 5
p_movex = 150
p_movey = 600
bg_sound = pygame.mixer.Sound('sound/bg.mp3')
bg_sound.play()
bg = pygame.image.load('images/background.png')
walk = [
    pygame.image.load('images/go/go1.png'),
    pygame.image.load('images/go/go2.png'),
    pygame.image.load('images/go/go3.png'),
    pygame.image.load('images/go/go4.png'),
    pygame.image.load('images/go/go5.png'),
    pygame.image.load('images/go/go6.png'),
]
k = 0
bg_move = 0
running = True
jump = False
jump_count = 7
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (bg_move, 0))
    screen.blit(bg, (bg_move + 1920, 0))
    screen.blit(walk[k], (p_movex, p_movey))

    if k == 5:
        k = 0
    else:
        k += 1
    bg_move -= 2
    if bg_move == -1920:
        bg_move = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and p_movex > 50:
        p_movex += speed
    elif keys[pygame.K_a] and p_movey > 200:
        p_movex -= speed
        pygame.display.update()
    else:
        pass
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                p_movey -= jump_count ** 2 / 2
            else:
                p_movey += jump_count ** 2 / 2
            jump_count -= 1
        else:
            jump = False
            jump_count = 7
    pygame.display.flip()
    clock.tick(10)
pygame.quit()

