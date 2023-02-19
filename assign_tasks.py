#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 19:21:40 2023

@author: victoriashi
"""


# import pygame

# pygame.init()

def assignTask(pygame, screen, fileName):
    
    pygame.font.init()

    # Set font
    font = pygame.font.SysFont("monospace", 30)

    # Set screen size
    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Set background color
    # background_color = (255, 255, 255)
    bg = pygame.image.load(fileName)
    bg = pygame.transform.scale(bg, screen.get_size())
    screen.blit(bg, (0, 0))
    result = None

    def assign_tasks():
        
        tasks = ["Initial Setup", "Development", "Integration and Testing"]
        candidates = ["", "", ""]
        candidate_positions = [(130, 320), (130, 550), (130, 780)]
        num_names_entered = 0

        # Loop for input
        for i, task in enumerate(tasks):
            # Loop for input
            input_complete = False
            while not input_complete:
                for event in pygame.event.get():
                    # if event.type == pygame.QUIT:
                        # pygame.quit()
                        # quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            input_complete = True
                            num_names_entered += 1
                            if num_names_entered == 3:
                                break
                        elif event.key == pygame.K_BACKSPACE:
                            candidates[i] = candidates[i][:-1]
                        else:
                            candidates[i] += event.unicode

                # Render candidate text
                candidate_text_renders = [font.render(candidate, True, (0, 0, 0)) for candidate in candidates]

                # Draw background and text
                # screen.fill(background_color)
                screen.blit(bg, (0, 0))
                for j, candidate_text_render in enumerate(candidate_text_renders):
                    screen.blit(candidate_text_render, candidate_positions[j])

                pygame.display.update()

            # Set position for next candidate
            # if i < len(tasks) - 1:
            #     candidate_positions[i+1] = (candidate_positions[i][0], candidate_positions[i][1] + 150)

        # Return final candidates list 
        return candidates
    result = assign_tasks()
    return result
    # final_candidates = assign_tasks()
    # print(final_candidates)

    # pygame.quit()

    # assign_tasks()
