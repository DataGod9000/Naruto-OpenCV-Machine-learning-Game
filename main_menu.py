import pygame
import math
import button
from states.main import game
import os
import time

def main_menu():
    pygame.init()
    pygame.mixer.init()
    
    clock = pygame.time.Clock()
    fps = 60
    
    #create game window
    bottom_panel = 150
    screen_width = 800
    screen_height = 400 + bottom_panel
    
    #create game window
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Naruto OpenCV Machine-Learning Battle")
    
    #load image
    naruto_icon = pygame.image.load('files/Icons/naruto_logo.png').convert_alpha()
    menu_background = pygame.image.load('files/Background/bg2.png').convert_alpha()
    play_img = pygame.image.load('files/Icons/play.png').convert_alpha()
    load_img = pygame.image.load('files/Icons/load.png').convert_alpha()
    bg_width = menu_background.get_width()
    bg_rect = menu_background.get_rect()
    
    #load sounds
    click = pygame.mixer.Sound('files/Sounds/click.ogg')
    battle_theme = pygame.mixer.music.load(os.path.join('files/Sounds', 'menu_music.mp3'))  
    pygame.mixer.music.play(-1, 0.0) 
    
    #define game variables
    scroll = 0
    play = False
    tiles = math.ceil(screen_width / bg_width) + 1
    current_fighter = 1
    total_fighters = 3
    action_cooldown = 0
    action_wait_time = 90
    
    #function to control characters actions
    class Fighter():
        def __init__(self, x, y, name):
            self.name = name
            self.animation_list = []
            self.frame_index = 0
            self.action = 0#0:idle, 1:attack, 2:hurt, 3:dead
            self.update_time = pygame.time.get_ticks()
            #load idle images
            temp_list = []
            for i in range(6):
                img = pygame.image.load(f'files/{self.name}/Run/{i}.png')
                img = pygame.transform.scale(img, (img.get_width() * 2.7, img.get_height() * 2.7))
                temp_list.append(img)
            self.animation_list.append(temp_list)
    
    
        def update(self):
            animation_cooldown = 100
            #handle animation
            #update image
            self.image = self.animation_list[self.action][self.frame_index]
            #check if enough time has passed since the last update
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            #if the animation has run out then reset back to the start
            if self.frame_index >= len(self.animation_list[self.action]):
                if self.action == 3:
                    self.frame_index = len(self.animation_list[self.action]) - 1
                else:
                    self.idle()
                    
        def draw(self):
            screen.blit(self.image, (0,380))
            
        def idle(self):
            #set variables to idle animation
            self.action = 0
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
            
    Sasuke = Fighter(200, 270, 'Sasuke')
    play_button = button.Button(screen, 335, 230, play_img, 150, 57)
    load_button = button.Button(screen, 335, 280, load_img, 150, 57)
    
    #game loop
    run = True
    while run:
    
        clock.tick(fps)    
          
        #draw scrolling background
        for i in range(0, tiles):
          screen.blit(menu_background, (i * bg_width + scroll, 0))
        
        #scroll background
        scroll -= 5
          
        #reset scroll
        if abs(scroll) > bg_width:
          scroll = 0
          
        screen.blit(naruto_icon, (200, 20))
        Sasuke.update()
        Sasuke.draw()
        
        if play_button.draw():
            play = True
    
        if load_button.draw():
            load = True
        
        if play == True:
            click.play()
            time.sleep(2)   
            game()
            
        #event handler
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            run = False
            
          if event.type == pygame.MOUSEBUTTONDOWN:
              clicked = True
          else:
              clicked = False
        pygame.display.update()
    
    pygame.quit()
    
main_menu()