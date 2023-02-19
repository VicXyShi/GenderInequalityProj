import pygame
def showScore(score, fileName):
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    font = pygame.font.Font(None, 100)
    text = font.render(str(score), True, (0, 0, 0))
    run = True
    while run:
        bg = pygame.image.load(fileName)
        # x, y = screen.get_size()
        bg = pygame.transform.scale(bg, screen.get_size())
        screen.blit(bg, (0, 0))
        # bg_rect = bg.get_rect()
        screen.blit(text, (800, 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                run = False