#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 18:18:02 2023

@author: victoriashi
"""

import pygame

def write_review(candidate):
    # print("write function called ----------------------")
    # initialize pygame and clock
    pygame.init()
    clock = pygame.time.Clock()
    
    # set up screen and font
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    base_font = pygame.font.Font(None, 32)
    
    # set up input box
    input_rect = pygame.Rect(200, 200, 140, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    active = False
    
    # set up instruction text
    instruction_text = base_font.render(f"Please write your review for {candidate}", True, (225, 225, 225))
    instruction_rect = instruction_text.get_rect(center=(300, 100))
    
    # set up review text
    review_text = ''
    
    pygame.init()
    while True:
        # print("into while loop ========================")
        # handle events
        for event in pygame.event.get():
            # print("into for loop ------=-=-=-=-=-------------=-=-=-=-==")
            if event.type == pygame.QUIT:
                # print("into py.quit branch =======================---")
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    review_text = review_text[:-1]
                else:
                    review_text += event.unicode
        
        # update screen
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(review_text, True, (0, 0, 0))
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text_surface.get_width()+10)
        pygame.draw.rect(screen, (0, 0, 0), instruction_rect)
        screen.blit(instruction_text, instruction_rect)
        pygame.display.flip()
        clock.tick(60)
        
        # check if user has submitted review
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            with open("reviews.txt", "a") as file:
                file.write(f"Review for {candidate}: {review_text}\n")
            return review_text