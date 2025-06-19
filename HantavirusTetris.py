# import the pygame module 
import pygame 
pygame.init()
import sys
import random
from pygame.locals import *
from pygame import Rect 
from pygame import *
# Define the background colour 
# using RGB color coding. 
background_colour = (255, 255, 255) 
  
# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((500, 600)) 
  
# Set the caption of the screen 
pygame.display.set_caption('TetrisGame') 
  
# Fill the background colour to the screen 
screen.fill(background_colour) 
  
# Update the display using flip 
pygame.display.flip() 

#DEFINE VARIABLES------------------------------------------------------------------------------------------------------------------------------------------------------------
Rectangle = Rect(130, 183, 150, 30)
Rectangle2 = Rect(345, 20, 5, 20)
Rectangle3 = Rect(359, 20, 5, 20)
Rectangle4 = Rect(350, 50, 200, 30)
Rectangle4_color = (0, 255, 0)
Rect_Color = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
teal = (0, 128, 128)
white = (255, 255, 255)
grey = (192, 192, 192)
X = 400
Y = 400
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Tetris Game')
font = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 15)
font3 = pygame.font.Font('freesansbold.ttf', 15)
font4 = pygame.font.Font('freesansbold.ttf', 15)
font5 = pygame.font.Font('freesansbold.ttf', 15)
font6 = pygame.font.Font('freesansbold.ttf', 17)
font7 = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('START', True, white)
text2 = font2.render('Click on the start button to start the game!', True, white)
#text3 = font2.render('Points:', True, white)
text4 = font7.render('GAME OVER!', True, black)
#text5 = font2.render('0', True, white)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)
textRect2 = text.get_rect()
textRect2.center = (80, 25)
textRect4 = text4.get_rect()
textRect5 = text.get_rect()
textRect5.center = (175, 275)
textRect4.center = (200, 225)
clock=pygame.time.Clock()
BUTTON_COOLDOWN = 500

# Variable to keep our game loop running 
running = True
  
# game loop 
while running: 
    #START CODING:-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    display_surface.fill(black)
    draw.rect(screen, Rect_Color, Rectangle)
    display_surface.blit(text, textRect)
    display_surface.blit(text2, textRect2)
    Rectangle_surface = pygame.Surface((150, 50))
    clock.tick(60)
    pygame.time.delay(BUTTON_COOLDOWN)
    
                    
# for loop through the event queue   
    for event in pygame.event.get(): 
        # Check for the mouse button down event
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #print("Hello")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Rectangle.collidepoint(event.pos):
                display_surface.fill(black)
    
                #TETRIS-----------------------------------------------------------------------------------------------------------------------------------------------------------

                
                colors = [
                    (0, 0, 0),
                    (120, 37, 179),
                    (255, 255, 0),
                    (80, 34, 22),
                    (80, 134, 22),
                    (255, 165, 0),
                    (180, 34, 122),
            ]


            class Figure:
                x = 0
                y = 0

                figures = [
                    [[1, 5, 9, 13], [4, 5, 6, 7]],
                    [[4, 5, 9, 10], [2, 6, 5, 9]],
                    [[6, 7, 9, 10], [1, 5, 6, 10]],
                    [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
                    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
                    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
                    [[1, 2, 5, 6]],
                ]

                def __init__(self, x, y):
                    self.x = x
                    self.y = y
                    self.type = random.randint(0, len(self.figures) - 1)
                    self.color = random.randint(1, len(colors) - 1)
                    self.rotation = 0

                def image(self):
                    return self.figures[self.type][self.rotation]

                def rotate(self):
                    self.rotation = (self.rotation + 1) % len(self.figures[self.type])


            class Tetris:
                def __init__(self, height, width):
                    self.level = 2
                    self.score = 0
                    self.state = "start"
                    self.field = []
                    self.height = 0
                    self.width = 0
                    self.x = 100
                    self.y = 60
                    self.zoom = 20
                    self.figure = None
                    self.figure2 = None
                    self.figure3 = None
                    
                
                    self.height = height
                    self.width = width
                    self.field = []
                    self.score = 0
                    self.state = "start"
                    for i in range(height):
                        new_line = []
                        for j in range(width):
                            new_line.append(0)
                        self.field.append(new_line)

                def new_figure(self):
                    self.figure = Figure(3, 0)
                    self.figure2 = Figure(4, 0)
                    self.figure3 = Figure(5, 0)

#NEW START FOR THE FLOOR-----------------------------------------------------------------------------------------------------------------------------------------------------
                def bottomBlocks(self):
                    self.bottomBlocks[
                        draw.rect(Rectangle4)
                    ]

                #This is when the block falls below and hits the ground
                def intersects(self):
                    intersection = False
                    for i in range(4):
                        for j in range(4):
                            if i * 4 + j in self.figure.image():
                                if i + self.figure.y > self.height - 1 or \
                                        j + self.figure.x > self.width - 1 or \
                                        j + self.figure.x < 0 or \
                                        self.field[i + self.figure.y][j + self.figure.x] > 0:
                                    intersection = True
                    for i in range(4):
                        for j in range(4):
                            if i * 4 + j in self.figure2.image():
                                if i + self.figure2.y > self.height - 1 or \
                                        j + self.figure2.x > self.width - 1 or \
                                        j + self.figure2.x < 0 or \
                                        self.field[i + self.figure2.y][j + self.figure2.x] > 0:
                                    intersection = True
                    for i in range(4):
                        for j in range(4):
                            if i * 4 + j in self.figure3.image():
                                if i + self.figure3.y > self.height - 1 or \
                                        j + self.figure3.x > self.width - 1 or \
                                        j + self.figure3.x < 0 or \
                                        self.field[i + self.figure3.y][j + self.figure3.x] > 0:
                                    intersection = True
                    return intersection

                def break_lines(self):
                    lines = 0
                    for i in range(1, self.height):
                        zeros = 0
                        for j in range(self.width):
                            if self.field[i][j] == 0:
                                zeros += 1
                        if zeros == 0:
                            lines += 1
                            for i1 in range(i, 1, -1):
                                for j in range(self.width):
                                    self.field[i1][j] = self.field[i1 - 1][j]
                    self.score += lines ** 2

                def go_space(self):
                    while not self.intersects():
                        self.figure.y += 1
                        #self.figure2.y += 1
                        #self.figure3.y += 1
                    self.figure.y -= 1
                    #self.figure2.y -= 1
                    #self.figure3.y -= 1
                    self.freeze()

                def go_down(self):
                    self.figure.y += 1
                    #self.figure2.y += 1
                    #self.figure3.y += 1
                    if self.intersects():
                        self.figure.y -= 1
                        #self.figure2.y -= 1
                        #self.figure3.y -= 1
                        self.freeze()

                def freeze(self):
                    for i in range(4):
                        for j in range(4):
                            if i * 4 + j in self.figure.image():
                                self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
                    #for i in range(4):
                        #for j in range(4):
                            #if i * 4 + j in self.figure2.image():
                                #self.field[i + self.figure2.y][j + self.figure2.x] = self.figure2.color
                    #for i in range(4):
                        #for j in range(4):
                            #if i * 4 + j in self.figure3.image():
                                #self.field[i + self.figure3.y][j + self.figure3.x] = self.figure3.color
                    self.break_lines()
                    self.new_figure()
                    if self.intersects():
                        self.state = "gameover"

                def go_side(self, dx):
                    old_x = self.figure.x
                    #old_x = self.figure2.x
                    #old_x = self.figure3.x
                    self.figure.x += dx
                    #self.figure2.x += dx
                    #self.figure3.x += dx
                    if self.intersects():
                        self.figure.x = old_x
                        #self.figure2.x = old_x
                        #self.figure3.x = old_x

                def rotate(self):
                    old_rotation = self.figure.rotation
                    #old_rotation = self.figure2.rotation
                    #old_rotation = self.figure3.rotation
                    self.figure.rotate()
                    #self.figure2.rotate()
                    #self.figure3.rotate()
                    if self.intersects():
                        self.figure.rotation = old_rotation
                        #self.figure2.rotation = old_rotation
                        #self.figure3.rotation = old_rotation


            # Initialize the game engine
            pygame.init()

            # Define some colors
            BLACK = (0, 0, 0)
            WHITE = (255, 255, 255)
            GRAY = (128, 128, 128)

            size = (400, 500)
            screen = pygame.display.set_mode(size)

            # Loop until the user clicks the close button.
            done = False
            clock = pygame.time.Clock()
            fps = 25
            game = Tetris(22, 10)
            counter = 0

            pressing_down = False

            while not done:
                if game.figure is None:
                    game.new_figure()
                counter += 1
                #if counter > 100000:
                    #counter = 0

                if counter % (fps // game.level // 2) == 0 or pressing_down:
                    if game.state == "start":
                        game.go_down()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            game.rotate()
                        if event.key == pygame.K_DOWN:
                            pressing_down = True
                        if event.key == pygame.K_LEFT:
                            game.go_side(-1)
                        if event.key == pygame.K_RIGHT:
                            game.go_side(1)
                        if event.key == pygame.K_SPACE:
                            game.go_space()
                        if event.key == pygame.K_ESCAPE:
                            game.__init__(20, 10)

                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            pressing_down = False
                
                #Defining all of the things for second screen--------------------------------------------------------------------------------------------------------------------
                screen.fill(black)
                CircleEND = pygame.draw.circle(screen, grey, [355,30], 20)
                CircleEND_pos = (355,30)
                CircleEND_radius = 20
                draw.rect(screen, white, Rectangle2)
                draw.rect(screen, white, Rectangle3)
                #display_surface.blit(text3, (20, 10))
                #display_surface.blit(text5, (80, 11))
                

                
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #Calculate the distance between the mouse and the circle center
                    mouse_pos = pygame.mouse.get_pos()
                    dist_x = mouse_pos[0] - CircleEND_pos[0]
                    dist_y = mouse_pos[1] - CircleEND_pos[1]
                    distance = (dist_x ** 2 + dist_y ** 2) ** 0.5  

                    # Check if the mouse is within the circle
                    if distance <= CircleEND_radius:
                        screen.fill(black)
                    
    
                #The lines so it is clear where the blocks are-------------------------------------------------------------------------------------------------------------------
                #THIS IS WHERE I WANT THE FLOOR TO BE----------------------------------------------------------------------------------------------------------------
                
                BlockforFall = [


                                    ]
                
                for i in range(game.height):
                    for j in range(game.width):
                        pygame.draw.rect(screen, red, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                        if game.field[i][j] > 0:
                            pygame.draw.rect(screen, colors[game.field[i][j]],
                                            [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])
                

                
                
                for i in range(game.height -4):
                    for j in range(game.width):
                        pygame.draw.rect(screen, grey, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                        if game.field[i][j] > 0:
                            pygame.draw.rect(screen, colors[game.field[i][j]],
                                            [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

                #Created the blocks here------------------------------------------------------------------------------------------------------------------------------------------
                if game.figure is not None:
                    for i in range(4):
                        for j in range(4):
                            p = i * 4 + j
                            if p in game.figure.image():
                                pygame.draw.rect(screen, colors[game.figure.color],
                                                [game.x + game.zoom * (j + game.figure.x) + 1,
                                                game.y + game.zoom * (i + game.figure.y) + 1,
                                                game.zoom, game.zoom]) # ADD -2 after game.zoom if you want the lines between the blocks when falling
                if game.figure2 is not None:
                    for i in range(4):
                        for j in range(4):
                            p = i * 4 + j
                            if p in game.figure2.image():
                                pygame.draw.rect(screen, colors[game.figure.color],
                                                [game.x + game.zoom * (j + game.figure.x) + 1,
                                                game.y + game.zoom * (i + game.figure.y) + 1,
                                                game.zoom, game.zoom]) 
                if game.figure3 is not None:
                    for i in range(4):
                        for j in range(4):
                            p = i * 4 + j
                            if p in game.figure3.image():
                                pygame.draw.rect(screen, colors[game.figure.color],
                                                [game.x + game.zoom * (j + game.figure.x) + 1,
                                                game.y + game.zoom * (i + game.figure.y) + 1,
                                                game.zoom, game.zoom]) 


                #font = pygame.font.SysFont('Calibri', 25, True, False)
                #font1 = pygame.font.SysFont('Calibri', 65, True, False)
                text = font6.render("Score:" + str(game.score), True, white)

                screen.blit(text, [0, 0])
                #This is what happens after game is over-------------------------------------------------------------------------------------------------------------------------
                if game.state == "gameover":
                    display_surface.fill(teal)
                    display_surface.blit(text4, textRect4)
                    text = font6.render("Total Score:" + str(game.score), True, black)
                    display_surface.blit(text, textRect5)

                pygame.display.flip()
                clock.tick(fps)
                
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
    pygame.display.update()
    
        
     


    
