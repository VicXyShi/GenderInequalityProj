import pygame
import os

def showWords(inputText, screen, pygame):
    
    #Sets the width and height of the screen
    WIDTH, HEIGHT = screen.get_size();
    introComPage = pygame.image.load("introduction_company.jpg")
    introComPage = pygame.transform.scale(introComPage, screen.get_size())
    # screen.blit(introComPage, (0, 0))

    #Importing the external screen
    os.putenv('SDL_FBDEV', '/dev/fb1')
    os.putenv('SDL_MOUSEDRV', 'TSLIB')
    os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

    #Initializes the screen - Careful: all pygame commands must come after the init
    # pygame.init()
    clock = pygame.time.Clock()

    #Sets mouse cursor visibility
    pygame.mouse.set_visible(False)
    #Sets the screen note: must be after pygame.init()
    # screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


    class Board(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((WIDTH, HEIGHT))
            self.image.fill((1,13,13))
            self.image.set_colorkey((13,100,13))
            self.rect = self.image.get_rect()
            self.font = pygame.font.SysFont("monospace", 30) #font size

        def add(self, letter, pos):
            s = self.font.render(letter, 1, (255, 255, 0))
            self.image.blit(s, pos)

    class Cursor(pygame.sprite.Sprite):
        def __init__(self, board):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((100, 20))
            self.image.fill((0,255,0))
            self.text_height = 30 #space between lines
            self.text_width = 20 #space between words
            self.rect = self.image.get_rect(topleft=(self.text_width, self.text_height))
            self.board = board
            self.text = ''
            self.cooldown = 0
            self.cooldowns = {'.': 12,
                            '[': 18,
                            ']': 18,
                            ' ': 5,
                            '\n': 30}

        def write(self, text):
            self.text = list(text)

        def update(self):
            if not self.cooldown and self.text:
                letter = self.text.pop(0)
                if letter == '\n':
                    self.rect.move_ip((0, self.text_height))
                    self.rect.x = self.text_width
                else:
                    self.board.add(letter, self.rect.topleft)
                    self.rect.move_ip((self.text_width, 0))
                self.cooldown = self.cooldowns.get(letter, 8)

            if self.cooldown:
                self.cooldown -= 1

    all_sprites = pygame.sprite.Group()
    board = Board()
    cursor = Cursor(board)
    all_sprites.add(cursor, board)

    # text = """[i] Initializing ...
    # [i] Entering ghost mode ...

    # done ...

    # """

    cursor.write(inputText)
    sizeOfString = len(inputText)
    counter = 0

    #Main loop
    running = True
    while running:
        

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                running = False
        #     for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     run = False
        # if event.type == pygame.KEYDOWN:
        #     print(pygame.key.name(event.key))
        # if (counter > sizeOfString + 500):
            # running = False
        
        all_sprites.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(6000)
        # counter += 1;
        # print("counter: ", counter)
        # print("size: ", sizeOfString)
        # print("in the typing")
    # print("before for loop")
    # for i in range(0, sizeOfString*10):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                running = False
        #     for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     run = False
        # if event.type == pygame.KEYDOWN:
        #     print(pygame.key.name(event.key))
        # if (counter > sizeOfString + 500):
            # running = False
        
        all_sprites.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(600)
        # counter += 1;
        # print("counter: ", counter)
        # print("size: ", sizeOfString)
        # print("in the typing")
    # print("finished the loop")