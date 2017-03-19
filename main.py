import pygame
from appJar import gui

def musicButtons(btnName):
    if btnName == "15 minutes of Jeopardy think music":
        pygame.mixer.Sound(file="15mins_jeopardy.mp3")
        pygame.mixer.Sound.play()
    elif btnName == "1 hour of Jeopardy think music":
        pygame.mixer.Sound(file="1hr_jeopardy.mp3")
        pygame.mixer.Sound.play()
    elif btnName == "1 hour of elevator music":
        pygame.mixer.Sound(file="1hr_elevator.mp3")
        pygame.mixer.Sound.play()
    elif btnName == "Stop Music":
        pygame.mixer.Sound.stop()

app = gui()
pygame.mixer.init()
app.addButton("15 minutes of Jeopardy think music")
app.addButton("1 hour of Jeopardy think music")
app.addButton("1 hour of elevator music")
app.addButton("Stop Music")

app.go()