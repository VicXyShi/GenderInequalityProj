import pygame
import os
import introduction as intro
import printerEffect as typer
import assign_tasks as assign
import testPict as p

import input as reviewer

male = ["Daniel", "Michael", "James"]
female = ["Sarah", "Jessica", "Emily"]

print("test")
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

def show(fileName):
    intro.show(fileName, pygame, screen)

show("resources/cover.jpg")
show("resources/game_intro.jpg")
show("resources/goal.jpg")
show("resources/look_candidates.jpg")
show("resources/candidates1.jpg")
show("resources/candidates2.jpg")
show("resources/initialSetup.jpg")
show("resources/development.jpg")
show("resources/integrAndTest.jpg")
show("resources/startGame.jpg")
candidates = assign.assignTask(pygame, screen, "resources/assign_work.jpg")
show("resources/submittedBig.jpg")
import model as m
show("resources/resultComing.jpg")
show("resources/failed.jpg")

# final_candidates = assign_tasks()
review_text = " "

maleScore = 0
for candidate in candidates:
    if candidate in male:
        maleScore += 1

fScore = 0
for candidate in candidates:
    if candidate in female:
        fScore += 1
for candidate in candidates:
    print(candidate)
    review_text += reviewer.write_review(candidate)
    print("candidates---------------------------------------------" + review_text)
resultBia = m.getBias(review_text)
score = 100*(1 - resultBia)
font = pygame.font.Font(None, 36)
text = font.render(str(score), True, (0, 0, 0))
# text_rect = text.get_rect(center=(500, 500))

if maleScore == 3:
    show("resources/biasedToW.jpg")
elif fScore == 3:
    show("resources/biasedToM.jpg")
    
elif resultBia*100 > 50:
    p.showScore(score, "resources/BE.jpg")
    #Have bias
    # bg = pygame.image.load("resources/BE.jpg")
    # # x, y = screen.get_size()
    # bg = pygame.transform.scale(bg, screen.get_size())
    # screen.blit(bg, (0, 0))
    # # bg_rect = bg.get_rect()
    # screen.blit(text, (500, 500))
elif resultBia*100 <= 50:
    p.showScore(score, "resources/NDE.jpg")
    # #Bias Does Not Exist
    # bg = pygame.image.load("resources/NDE.jpg")
    # # x, y = screen.get_size()
    # bg = pygame.transform.scale(bg, screen.get_size())
    # screen.blit(bg, (0, 0))
    # screen.blit(text, (500, 500))
    
# pygame.display.update()
# resultBia = m.getBias(review_text)
# print("bias number: ---------------------------", resultBia)


#Last 5 pages
show("resources/conclusion1.jpg")
show("resources/conclusion2.jpg")
show("resources/conclusion3.jpg")
show("resources/conclusion4.jpg")
show("resources/conclusion5.jpg")