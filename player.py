import pygame
WHITE = (255, 255, 255)
class Player(pygame.sprite.Sprite):
    #This class represents a Player. It derives from the "Sprite" class in Pygame.


    def __init__(self,  char, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #Initialise attributes of the car.
        self.width = width
        self.height = height
        if char == "1":
          self.image = pygame.image.load("images/prins_idle.png").convert_alpha() #self.char = 
        elif char == "2":
          self.image = pygame.image.load("images/dark_idle.png").convert_alpha()
        elif char == "3":
          self.image = pygame.image.load("images/gold_idle.png").convert_alpha()
        
        self.speed = speed
 
        # Draw the knight

        #self.image = pygame.image.load("images/knight_walk.png").convert_alpha()
        #pygame.draw.rect(self.image, [0, 0, self.width, self.height], self.speed)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
 
    def moveRight(self, pixels, stappen):
      if stappen < 500:
        self.rect.x += pixels

    def moveLeft(self, pixels, stappen):
      if stappen > -200:
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
 
    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20
 
    def changeSpeed(self, speed):
        self.speed = speed
 
    def repaint(self, char):
        self.char = char
        pygame.draw.rect(self.image, self.char, [0, 0, self.width, self.height])