import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        '''Intitializes a Hero object
      args: self, name (str), x (int), y(int), img_file (str)'''
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name
        self.speed = 3
        self.health = 3
        self.height = self.image.get_height()
        self.width = self.image.get_width()

    #methods to make moving our hero easier
    def move_up(self):
        '''moves hero up'''
        self.rect.y -= self.speed
    def move_down(self):
        '''moves hero down'''
        self.rect.y += self.speed
    def move_left(self):
        '''moves hero left'''
        self.rect.x -= self.speed
    def move_right(self):
        '''moves hero right'''
        self.rect.x += self.speed

    def fight(self, opponent):
        '''fight between hero and enemy
      args: self (Hero object), opponent (Enemy object)'''
        if(random.randrange(3)):
            self.health -= 1
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
        return True
    def heal(self):
      '''gives the hero an extra life
      args: self'''
      self.health += 1
      print(f"Healed. Remaining Health: {self.health} ")
