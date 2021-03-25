import pygame
WHITE = (255, 255, 255)
 
class Monster(pygame.sprite.Sprite):
    #This class represents a Monster. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, color, width, height, attack, healthm):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the Monster, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        #Initialise attributes of the car.
        self.width=width
        self.height=height
        self.color = color
        self.attack = attack
        self.healtm = healthm
        #self.health = health
        
        
        self.image = pygame.image.load("images/ork_standing.png")#.convert_alpha()
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
       
        def update(self):
          self.kill() 
    
        if healthm <= 0:
          self.update()
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

         