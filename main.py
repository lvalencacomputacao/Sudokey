import pygame
from pygame.locals import *
from board import Board
from button import Button 

# Initialization and screen surface loading
pygame.init()
screen = pygame.display.set_mode((1366, 768))
screenSize = pygame.display.get_surface().get_size()
width = screenSize[0]
height = screenSize[1]
print(width, height)
pygame.display.set_caption("Sudokey: Sudoku's Solver")

# Image and music loading
bgMenu = pygame.image.load("background/sudokey2Menu.png")
bgMenu = pygame.transform.scale(bgMenu, (width, height - 30))
bgStart = pygame.image.load("background/sudokeyCustom.png")
bgStart = pygame.transform.scale(bgStart, (width - 40, height - 55))
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.mixer.music.load("musica/lullabyGhostInYourPiano.mp3")
pygame.mixer.music.play(-1)
click = pygame.mixer.Sound("sons/click.ogg")

# Default screen and game state
running = 1
menu = 1
start = 0
credit = 0

# Mouse logic to detect click
currentSquare = (9, 9)
clickedCell = None

# Creating board using class "Board"
tabuleiro = Board()

# Creating menu buttons using class "Button"
buttonStart = Button(400, 186, 530, 90)
buttonTutorial = Button(400, 325, 530, 90)
buttonOptions = Button(400, 464, 530, 90)
buttonCredits = Button(400, 603, 530, 90)

# Creating start buttons using class "Button"
buttonSolve = Button(898, 40, 380, 80)
buttonReset = Button(898, 159, 380, 80)
buttonGoBack = Button(898, 279, 380, 80)
buttonOptionsStart = Button(898, 398, 380, 80)

# Font loading
font = pygame.font.Font("FreeSansBold.ttf", 30)


# Visually updates the board
def drawGrid(board):
    for i in range(9):
        for j in range(9):
            if (board[i][j]):
                text = font.render(str(board[i][j]), True, (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (j * 90 + 45, i * 80 + 45)
                screen.blit(text, textRect)

# Plays music based on input
def jukebox(number):
    if number == 0:
        pygame.mixer.music.stop()
    elif number == 1:
        pygame.mixer.music.load("musica/lullabyGhostInYourPiano.mp3")
        pygame.mixer.music.play(-1)
    elif number == 2:
        pygame.mixer.music.load("musica/adventureGhostInYourPiano.mp3")
        pygame.mixer.music.play(-1)
    elif number == 3:
        pygame.mixer.music.load("musica/liebestrau.mp3")
        pygame.mixer.music.play(-1)
    elif number == 4:
        pygame.mixer.music.load("musica/Kiss_the_Sky.mp3")
        pygame.mixer.music.play(-1)
    elif number == 5:
        pygame.mixer.music.load("musica/Lullaby.mp3")
        pygame.mixer.music.play(-1)
    elif number == 6:
        pygame.mixer.music.load("musica/Gentle_Breeze.mp3")
        pygame.mixer.music.play(-1)
    elif number == 7:
        pygame.mixer.music.load("musica/Eternal_Hope.mp3")
        pygame.mixer.music.play(-1)
    elif number == 8:
        pygame.mixer.music.load("musica/Pressure.mp3")
        pygame.mixer.music.play(-1)
    elif number == 9:
        pygame.mixer.music.load("musica/01 To the Moon - Main Theme.mp3")
        pygame.mixer.music.play(-1)

def setVolume(command):
    volumeAtual = pygame.mixer.music.get_volume()
    print(volumeAtual)
    if command == pygame.K_UP and volumeAtual < 1.0:
        pygame.mixer.music.set_volume(min(volumeAtual + 0.25, 1.0))
        print(volumeAtual)
    elif command == pygame.K_DOWN and volumeAtual > 0.0:
        pygame.mixer.music.set_volume(max(volumeAtual - 0.25, 0.0))


while running:
    while menu:
        pygame.display.flip()
        screen.blit(bgMenu, (0, 0))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = 0
                menu = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                start = 1
                menu = 0
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()

                if buttonStart.isOn(x, y):
                    #click.play()
                    #click.stop()

                    print(x, y)
                    menu = 0
                    start = 1

                elif buttonTutorial.isOn(x, y):
                    print(x, y)
                    print('tutorial')
                    menu = 0
                    start = 1

                elif buttonOptions.isOn(x, y):
                    print(x, y)
                    print('Options')
                    menu = 0
                    start = 1

                elif buttonCredits.isOn(x, y):
                    print(x, y)
                    print('Credits')
                    menu = 0
                    start = 1

            if (event.type == pygame.KEYDOWN):
                if (pygame.K_0 <= event.key <= pygame.K_9):
                    number = int(event.unicode)
                    jukebox(number)
                if (event.key == pygame.K_UP or pygame.K_DOWN):
                    setVolume(event.key)

    while start:
        pygame.display.flip()
        screen.blit(bgStart, (0, 0))
        drawGrid(tabuleiro.tabuleiro)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('stopping')
                running = 0
                start = 0

            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_m or event.key == pygame.K_ESCAPE):
                start = 0
                menu = 1

            if (event.type == pygame.MOUSEBUTTONUP):
                coords = pygame.mouse.get_pos()
                col = coords[1] // 80
                line = coords[0] // 90
                clickedCell = (line, col)

            if (event.type == pygame.KEYDOWN):
                if (clickedCell != None):
                    if (pygame.K_0 <= event.key <= pygame.K_9):
                        line = clickedCell[1]
                        col = clickedCell[0]
                        number = int(event.unicode)
                        if 0 <= line <= 8 and 0 <= col <= 8:
                            tabuleiro.setCell(line, col, number)
                            clickedCell = None

            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_s:
                    tabuleiro.findFirst()
                    tabuleiro.solve()
                elif event.key == pygame.K_r:
                    tabuleiro.reset()
                elif (event.key == pygame.K_UP or pygame.K_DOWN):
                    setVolume(event.key)


            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                print(x, y)

                if buttonSolve.isOn(x, y):
                    print('solving')
                    tabuleiro.solve()

                elif buttonReset.isOn(x, y):
                    tabuleiro.reset()
                    tabuleiro.show()

                elif buttonGoBack.isOn(x, y):
                    start = 0
                    menu = 1

                elif buttonOptionsStart.isOn(x, y):
                    start = 0
                    menu = 1

pygame.quit()
