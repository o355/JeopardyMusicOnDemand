# (c) 2017, o355 under the GNU GPL 3.0 license.
# version thereisnoversiontothisprogram

import pygame
from appJar import gui

def musicButtons(btnName):
    if btnName == "15 minutes of Jeopardy think music":
        pygame.mixer.music.load("15mins_jeopardy.mp3")
        pygame.mixer.music.play()
    elif btnName == "1 hour of Jeopardy think music":
        pygame.mixer.music.load("1hr_jeopardy.mp3")
        pygame.mixer.music.play()
    elif btnName == "1 hour of elevator music":
        pygame.mixer.music.load("1hr_elevator.mp3")
        pygame.mixer.music.play()
    elif btnName == "Stop Music":
        pygame.mixer.music.stop()

app = gui()
pygame.mixer.init()
app.addButton("15 minutes of Jeopardy think music", musicButtons)
app.addButton("1 hour of Jeopardy think music", musicButtons)
app.addButton("1 hour of elevator music", musicButtons)
app.addButton("Stop Music", musicButtons)

app.go()
