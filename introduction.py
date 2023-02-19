def show(fileName, pygame, screen):
    run = True
    while run:
        introPage = pygame.image.load(fileName)
        x, y = screen.get_size()
        introPage = pygame.transform.scale(introPage, screen.get_size())
        screen.blit(introPage, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                run = False
  
def showCover(pygame, screen):
    show("Project_Leader_Pro_cover_2.jpg", pygame, screen)

def showIntroComp(pygame, screen):
    show("intro_Comp.jpg", pygame, screen)
    
def showIntroRoleAndGoal(pygame, screen):
    show("intro_role.jpg", pygame, screen)
    
    # run = True
    # while run:
    #     introPage = pygame.image.load("Project_Leader_Pro_cover_2.jpg")
    #     x, y = screen.get_size()
    #     introPage = pygame.transform.scale(introPage, screen.get_size())
    #     screen.blit(introPage, (0, 0))
    #     pygame.display.flip()
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             run = False
       