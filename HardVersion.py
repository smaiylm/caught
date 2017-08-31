import pygame
import random
import time
import os, sys
import keyboard
import math
from PIL import Image
#import display_surf
'''
image_surf = pygame.image.load("one_big_file.bmp").convert()
# ........
# and for drawing only  part of it:
display_surf.blit(image_surf, (0,0) , rect_containing_coordinates_to_draw)
'''
pygame.init() #Initialize pygame

red = (255, 0, 0)
yellow = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0) #Color Optimizations

width_screen = 600
height_screen = 600 #Screen size variables

x_rect = 300
y_rect = 500
width_rect = 50
height_rect = 15 #Pong Rectangle position and measurements

y_circle = 350.0
x_circle = 300.0
width_circle = 20 #Pong Ball position and measurements

y_player = 100.0
x_player = 100.0

y_hoop = 200.0
x_hoop = 300.0

y_monster = 350.0
x_monster = 300.0
width_monster = 20

x_gameover = 80.0
y_gameover = 80.0

x_background = 0.0
y_background = 0.0

score = 0
dy = -0.1
dx = random.uniform(-0.05,0.05) #Other Variables

screen = pygame.display.set_mode((width_screen, height_screen))

def rect (x,y):
    '''
    image_surf = pygame.image.load().convert()
    pygame.image.load("Hoop.png")
    screen.blit(self.image, (self.x, self.y))
    
    screen.blit(self.image, (self.x, self.y))
    '''
    #carImg = pygame.image.load('Hoop.png')
    #screen.blit(carImg, (x,y))

    
    pygame.draw.rect(screen, blue, (x,y,width_rect,height_rect), 0)
'''def hoop (x,y, height, width):
    carImg = pygame.image.load('30-second-timer.gif')'''
    
def circle(x,y):
    #pygame.draw.ellipse(screen, yellow, (x,y,width_circle,width_circle), 0)
    carImg = pygame.image.load('monster.jpg')
    screen.blit(carImg, (x,y))
def direction(x_circle,y_circle,dx, dy):
    return x_circle + dx, y_circle + dy
def player(x,y):
    carImg = pygame.image.load('cross.png')
    screen.blit(carImg, (x,y))

def timer (x,y):
    Image.open("30-second-timer.gif").show()
    #carImg = pygame.image.load('30-second-timer.gif')
    #screen.blit(carImg, (x,y))

def monster (x,y):
    carImg = pygame.image.load('monster2.png')
    screen.blit(carImg, (x,y))

def gameover (x,y):
    carImg = pygame.image.load('Game_Over.jpg')
    screen.blit(carImg, (80,80))

def background (x,y):
    carImg = pygame.image.load('background.jpg')
    screen.blit(carImg, (0,0))

game_done = False
end = False         #Flags for loops or test statements
start_time = time.time()
start_time2 = start_time
timer(0,0)
exists = True
shoot = False
while game_done == False:
    screen.fill(blue)
    background(x_background, y_background)
    if time.time() - start_time > 2:
       start_time = time.time()
       x_circle,y_circle = random.randint(0,600), random.randint(0,600)
       x_monster,y_monster = random.randint(0,600), random.randint(0,600)
    
    if not end:
        x_circle,y_circle = x_circle + dx, y_circle+dy
        x_monster,y_monster = x_monster + dx, y_monster+dy
        if exists:
            circle(x_circle, y_circle)
        player(x_player, y_player)
        monster(x_monster, y_monster)
        
    
    
        
    
    if time.time() - start_time2 > 30:
        gameover(x_gameover, y_gameover)
        pygame.mixer.music.load('gameover.wav')
        pygame.mixer.music.play(0)
    if time.time() - start_time2 > 32:
        print("Game Over! Great job. Your score was: " + str(score))
        print()
        pygame.quit()
        sys.exit()
       
    
    if y_circle > y_player - 20 and x_circle > x_player - 35 and x_circle < x_player + 35 or y_monster > y_player - 20 and x_monster > x_player - 35 and x_monster < x_player + 35:
        print(y_circle > y_rect - 20, x_circle > x_rect - 35,x_circle < x_rect + 35) 
        print(y_monster > y_rect - 20, x_monster > x_rect - 35,x_monster < x_rect + 35)
        if shoot:
            exists = True
            print("Shoot!")
            score +=1
            pygame.mixer.music.load('shoot.wav')
            pygame.mixer.music.play(0)
            x_circle,y_circle = random.randint(0,600), random.randint(0,600)
            x_monster,y_monster = random.randint(0,600), random.randint(0,600)
    '''
    if y_circle > y_rect - 20 and x_circle > x_rect - 35 and x_circle < x_rect + 35:
            dx = random.uniform(-0.3,0.3)  #Changing the direction of the ball
            dy = -dy    #Derivatives
            score += 1
            dy *= 1.02
    '''
    if dy > 20:
        dy = 20.0
    if dy < -20:
        dy = -20.0
    #dy += float(abs(dy/2))
    #dy += float(abs(600 - y_circle))/600.0
    dy += 0.01
    if y_circle < 5 or y_circle > 575:
        dy = -dy
    if x_circle > 590 or x_circle < 2:
        dx = -dx

    if y_monster < 5 or y_monster > 575:
        dy = -dy
    if x_monster > 590 or x_monster < 2:
        dx = -dx
    '''
    #if y_circle > 560:
        #game_done = True
        #end = True          #Ball goes below the paddle
    '''                  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                #x_rect +=32
                x_player += 10
            if event.key ==pygame.K_LEFT:
                #x_rect -=32              #Key clicking events
                x_player -= 10
            if event.key ==pygame.K_UP:
                y_player -=20
            if event.key ==pygame.K_DOWN:
                y_player +=20              #Key clicking events
            if event.key == pygame.K_w:
                y_player -=20

            if event.key == pygame.K_s:
                y_player +=20
            if event.key == pygame.K_a:
                x_player -= 10
            if event.key == pygame.K_d:
                x_player += 10

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key ==pygame.K_KP_ENTER:
                shoot = True
                
                
                exists= True
            else:
                shoot = False
                

            

        
                

    pygame.display.update()     #Updating the display
    pygame.display.set_caption(str(score)) #Points system

pygame.display.update()
time.sleep(3)
pygame.quit()

