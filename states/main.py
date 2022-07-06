# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:14:58 2022

@author: get gd nub
"""
from states.fireballjitsu import fireball_handsign
from states.chidori import chidori_handsign
from states.amatersu import amatersu_handsign
import pygame
import random
import button
import os
import time


def game():
#---------------------------------pygame SET UP --------------------------------------------------------------------------------------------------
    pygame.init()
    pygame.mixer.init()
    
    
    clock = pygame.time.Clock()
    fps = 60
    
    #create game window
    bottom_panel = 150
    screen_width = 800
    screen_height = 400 + bottom_panel
    
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Naruto OPENCV MACHINE LEARNING battle')
    
    #define game variables
    current_fighter = 1
    total_fighters = 3
    action_cooldown = 0
    action_wait_time = 90
    fireball = False
    chidori = False
    sharingan = False
    attack = False
    potion = False
    
    potion_effect = 15
    clicked = False
    game_over = 0
    
    #define sounds
    click = pygame.mixer.Sound('files/Sounds/click.ogg')
    heal = pygame.mixer.Sound('files/Sounds/heal.mp3')
    sasuke_kick = pygame.mixer.Sound('files/Sounds/sasuke_kick.mp3')
    enemy_attack = pygame.mixer.Sound('files/Sounds/enemy_attack.mp3')
    battle_theme = pygame.mixer.music.load(os.path.join('files/Sounds', 'battle_theme.mp3'))  
    pygame.mixer.music.play(-1, 0.0) 
    
    #define fonts
    font = pygame.font.Font('files/Font/Eight-Bit Madness.ttf', 26)
    
    #define colours
    red = (255, 0, 0)
    green = (0, 255, 0)
    
    #load images
    #background image
    background_img = pygame.image.load('files/Background/background.jpg').convert_alpha()
    #panel image
    panel_img = pygame.image.load('files/Icons/panel.png').convert_alpha()
    #button images
    potion_img = pygame.image.load('files/Icons/potion2.png').convert_alpha()
    fire_img = pygame.image.load('files/Icons/flame.png').convert_alpha()
    eye_img = pygame.image.load('files/Icons/eye.png').convert_alpha()
    lightning_img = pygame.image.load('files/Icons/lightning.png').convert_alpha()
    restart_img = pygame.image.load('files/Icons/restart.png').convert_alpha()
    #load victory and defeat images

    victory_img = pygame.image.load('files/Icons/victory.png').convert_alpha()
    defeat_img = pygame.image.load('files/Icons/defeat.png').convert_alpha()
    #kunai image
    kunai_img = pygame.image.load('files/Icons/kunai.png').convert_alpha()
    
        
    def draw1(self):
        screen.blit(self.image, self.rect)
        
    def draw2(self):
       screen.blit(self.image, self.rect)
    
    #create function for drawing text
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        
        screen.blit(img, (x, y))
    
    
    #function for drawing background
    def draw_bg():
        screen.blit(background_img, (0, 0))
    
    
    #function for drawing panel
    def draw_panel():
        #draw panel rectangle
        screen.blit(panel_img, (0, screen_height - bottom_panel))
        #show Sasuke stats
        draw_text(f'{Sasuke.name}  HP {Sasuke.hp}/100', font, (255,255,255) , 100, screen_height - bottom_panel + 15)
        for count, i in enumerate(bandit_list):
            #show name and health
            draw_text(f'{i.name}  HP {i.hp}/20', font, (255,255,255), 500, (screen_height - bottom_panel + 15) + count * 60)
    
    #function to control characters actions
    class Fighter():
        def __init__(self, x, y, name, max_hp, strength, potions):
            self.name = name
            self.max_hp = max_hp
            self.hp = max_hp
            self.strength = strength
            self.start_potions = potions
            self.potions = potions
            self.alive = True
            self.animation_list = []
            self.frame_index = 0
            self.action = 0#0:idle, 1:attack, 2:hurt, 3:dead
            self.update_time = pygame.time.get_ticks()
            #load idle images
            temp_list = []
            for i in range(8):
                img = pygame.image.load(f'files/{self.name}/Idle/{i}.png')
                img = pygame.transform.scale(img, (img.get_width() * 2.7, img.get_height() * 2.7))
                temp_list.append(img)
            self.animation_list.append(temp_list)
            #load attack images
            temp_list = []
            for i in range(9):
                img = pygame.image.load(f'files/{self.name}/Attack/{i}.png')
                img = pygame.transform.scale(img, (img.get_width() * 2.7, img.get_height() * 2.7))
                temp_list.append(img)
            self.animation_list.append(temp_list)
            #load hurt images
            temp_list = []
            for i in range(4):
                img = pygame.image.load(f'files/{self.name}/Hurt/{i}.png')
                img = pygame.transform.scale(img, (img.get_width() * 2.7, img.get_height() * 2.7))
                temp_list.append(img)
            self.animation_list.append(temp_list)
            #load death images
            temp_list = []
            for i in range(10):
                img = pygame.image.load(f'files/{self.name}/Death/{i}.png')
                img = pygame.transform.scale(img, (img.get_width() * 2.7, img.get_height() * 2.7))
                temp_list.append(img)
            self.animation_list.append(temp_list)
            self.image = self.animation_list[self.action][self.frame_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
    
    
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
    
        
        def idle(self):
            #set variables to idle animation
            self.action = 0
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    
    
        def attack(self, target):
            #deal damage to enemy
            rand = random.randint(-5, 5)
            damage = self.strength + rand
            target.hp -= damage
            #run enemy hurt animation
            target.hurt()
            #check if target has died
            if target.hp < 1:
                target.hp = 0
                target.alive = False
                target.death()
            damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
            damage_text_group.add(damage_text)
            #set variables to attack animation
            self.action = 1
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
            
        def jitsu(self, target1, target2):
            #deal damage to enemy
            rand = random.randint(8, 10)
            damage = self.strength + rand
            target1.hp -= damage
            target2.hp -= damage
            #run enemy hurt animation
            target1.hurt()
            target2.hurt()
            #check if target1 has died
            if target1.hp < 1:
                target1.hp = 0
                target1.alive = False
                target1.death()
            damage_text = DamageText(target1.rect.centerx, target1.rect.y, str(damage), red)
            damage_text_group.add(damage_text)
            #check if target2 has died
            if target2.hp < 1:
                target2.hp = 0
                target2.alive = False
                target2.death()
            damage_text = DamageText(target2.rect.centerx, target2.rect.y, str(damage), red)
            damage_text_group.add(damage_text)
            #set variables to attack animation
            self.action = 1
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    
        def hurt(self):
            #set variables to hurt animation
            self.action = 2
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    
        def death(self):
            #set variables to death animation
            self.action = 3
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    
    
        def reset (self):
            self.alive = True
            self.potions = self.start_potions
            self.hp = self.max_hp
            self.frame_index = 0
            self.action = 0
            self.update_time = pygame.time.get_ticks()
    
    
        def draw(self):
            screen.blit(self.image, self.rect)
    
    
    #function to draw healthbar
    class HealthBar():
        def __init__(self, x, y, hp, max_hp):
            self.x = x
            self.y = y
            self.hp = hp
            self.max_hp = max_hp
    
    
        def draw(self, hp):
            #update with new health
            self.hp = hp
            #calculate health ratio
            ratio = self.hp / self.max_hp
            pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
            pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))
    
    
    #funciton to draw damage text
    class DamageText(pygame.sprite.Sprite):
        def __init__(self, x, y, damage, colour):
            pygame.sprite.Sprite.__init__(self)
            self.image = font.render(damage, True, colour)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.counter = 0
    
    
        def update(self):
            #move damage text up
            self.rect.y -= 1
            #delete the text after a few seconds
            self.counter += 1
            if self.counter > 30:
                self.kill()
    
    
    
    damage_text_group = pygame.sprite.Group()
    
    
    Sasuke = Fighter(200, 270, 'Sasuke', 100, 10, 3)
    bandit1 = Fighter(550, 270, 'Bandit', 20, 6, 1)
    bandit2 = Fighter(700, 270, 'Bandit', 20, 6, 1)
    
    bandit_list = []
    bandit_list.append(bandit1)
    bandit_list.append(bandit2)
    
    Sasuke_health_bar = HealthBar(100, screen_height - bottom_panel + 40, Sasuke.hp, Sasuke.max_hp)
    bandit1_health_bar = HealthBar(500, screen_height - bottom_panel + 40, bandit1.hp, bandit1.max_hp)
    bandit2_health_bar = HealthBar(500, screen_height - bottom_panel + 100, bandit2.hp, bandit2.max_hp)
    
    #create buttons
    potion_button = button.Button(screen, 100, screen_height - bottom_panel + 70, potion_img, 64, 64)
    fireball_button = button.Button(screen, 170, screen_height - bottom_panel + 70, fire_img, 64, 64)
    chidori_button = button.Button(screen, 240, screen_height - bottom_panel + 70, lightning_img, 64, 64)
    sharingan_button = button.Button(screen, 310, screen_height - bottom_panel + 70, eye_img, 64, 64)
    restart_button = button.Button(screen, 330, 120, restart_img, 120, 30)
    
     
    #-----------------------------------------------play function ------------------------------------------------------------------------
    run = True
    while run:
        
        clock.tick(fps) 
        
        #draw background
        draw_bg()
    
        #draw panel
        draw_panel()
        Sasuke_health_bar.draw(Sasuke.hp)
        bandit1_health_bar.draw(bandit1.hp)
        bandit2_health_bar.draw(bandit2.hp)
    
        #draw fighters
        Sasuke.update()
        Sasuke.draw()
        for bandit in bandit_list:
            bandit.update()
            bandit.draw()
    
        #draw the damage text
        damage_text_group.update()
        damage_text_group.draw(screen)
    
        #control player actions
        #reset action variables
        attack = False
        potion = False
        fireball = False
        chidori = False
        sharingan = False
        target = None
        #make sure mouse is visible
        pygame.mouse.set_visible(True)
        pos = pygame.mouse.get_pos()
        for count, bandit in enumerate(bandit_list):
            if bandit.rect.collidepoint(pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show kunai in place of mouse cursor
                screen.blit(kunai_img, pos)
                if clicked == True and bandit.alive == True:
                    attack = True
                    target = bandit_list[count]
        
        #Jutsu Buttons
        if potion_button.draw():
            potion = True
        #show number of potions remaining
        draw_text(str(Sasuke.potions), font, (255,255,255), 145, screen_height - bottom_panel + 75)
        
        #Flame Ball jutsu
        if fireball_button.draw():
            fireball = True
            click.play()
        
        #Chidori jutsu
        if chidori_button.draw():
            chidori = True
            click.play()
        
        #sharingan jutsu
        if sharingan_button.draw():
            sharingan = True
            click.play()
    
    #-----------------------------------------------player action------------------------------------------------------------------------
        if game_over == 0:
            #player action
            if Sasuke.alive == True:
                if current_fighter == 1:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        #look for player action
                        #attack
                        if attack == True and target != None:
                            Sasuke.attack(target)
                            sasuke_kick.play()
                            current_fighter += 1
                            action_cooldown = 0
    
                        #potion
                        if potion == True:
                            if Sasuke.potions > 0:
                                #check if the potion would heal the player beyond max health
                                if Sasuke.max_hp - Sasuke.hp > potion_effect:
                                    heal_amount = potion_effect
                                else:
                                    heal_amount = Sasuke.max_hp - Sasuke.hp
                                Sasuke.hp += heal_amount
                                heal.play()
                                Sasuke.potions -= 1
                                damage_text = DamageText(Sasuke.rect.centerx, Sasuke.rect.y, str(heal_amount), green)
                                damage_text_group.add(damage_text)
                                current_fighter += 1
                                action_cooldown = 0
                                
                        #fireball
                        if fireball == True :
                            fireball_handsign()                               
                            Sasuke.jitsu(bandit1, bandit2)
                            current_fighter += 1
                            action_cooldown = 0
    
                                                    
                        #chidori
                        if chidori == True :
                            chidori_handsign()
                            Sasuke.jitsu(bandit1, bandit2)
                            current_fighter += 1
                            action_cooldown = 0
                            
                        #sharingan
                        if sharingan == True :
                            amatersu_handsign()
                            Sasuke.jitsu(bandit1, bandit2)
                            current_fighter += 1
                            action_cooldown = 0
            else:
                game_over = -1
    
    #-----------------------------------------------enemy action------------------------------------------------------------------------
            #enemy action
            for count, bandit in enumerate(bandit_list):
                if current_fighter == 2 + count:
                    if bandit.alive == True:
                        action_cooldown += 1
                        if action_cooldown >= action_wait_time:
                            #check if bandit needs to heal first
                            if (bandit.hp / bandit.max_hp) < 0.5 and bandit.potions > 0:
                                #check if the potion would heal the bandit beyond max health
                                if bandit.max_hp - bandit.hp > potion_effect:
                                    heal_amount = potion_effect
                                else:
                                    heal_amount = bandit.max_hp - bandit.hp
                                bandit.hp += heal_amount
                                heal.play()
                                bandit.potions -= 1
                                damage_text = DamageText(bandit.rect.centerx, bandit.rect.y, str(heal_amount), green)
                                damage_text_group.add(damage_text)
                                current_fighter += 1
                                action_cooldown = 0
                            #attack
                            else:
                                bandit.attack(Sasuke)
                                enemy_attack.play()
                                current_fighter += 1
                                action_cooldown = 0
                    else:
                        current_fighter += 1
    
            #if all fighters have had a turn then reset
            if current_fighter > total_fighters:
                current_fighter = 1
    
    
        #check if all bandits are dead
        alive_bandits = 0
        for bandit in bandit_list:
            if bandit.alive == True:
                alive_bandits += 1
        if alive_bandits == 0:
            game_over = 1
    
    
        #check if game is over
        if game_over != 0:
            if game_over == 1:
                screen.blit(victory_img, (250, 50))
            if game_over == -1:
                screen.blit(defeat_img, (290, 50))
            if restart_button.draw():
                run = False
                game()
                #Sasuke.reset()
                #for bandit in bandit_list:
                    #bandit.reset()
                #current_fighter = 1
                #action_cooldown
                #game_over = 0
    
    
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False                
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked = False
                
    
        pygame.display.update()
    
    pygame.quit()
    

    
    
    
    
