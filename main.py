import pygame, random, time
from player import Player
from monster import Monster

pygame.init()

#player stats 
tutorial = False#True#False
start = True

health = 10
strenght = 1
defensePlr = False
Played = False
level = 0

#Other stats
attackm = 0
healthm = 3

#gameinfo
RED = (255, 0, 0)
GREY = (179, 179, 204)
SCREENWIDTH=700
SCREENHEIGHT=500

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.font.init()
myfont = pygame.font.SysFont('Corbel', 30)

pygame.display.set_caption("Dungeon")

carryOn = True
clock = pygame.time.Clock()


print('\033c')
if tutorial == True:
  print("Welkom avonturier!")
  naam = input("Ik ben Warre en ik ga je begeleiden in de tutorial! Wat is je naam? ")
  time.sleep(.5)
  char = input("Wil je een ridder (1), een donkere ridder (2) of een goude ridder (3) zijn?(Geef het nummer in)  ")

  print()
  print("Oke welkom "+naam+", burgers van onze stad hoorde rare geluiden van uit de grotten dicht bij de stad en we vermoeden dat er monsters in de grotten zitten! Kan jij ze gaan tegen houden?"+"\n")
  time.sleep(2)
  print("Je start met 10 levens en 1 strenght punten je kan strenght punten verdienen door monsters te vermoorden en betere wapens te krijgen, 1 strenght punt is gelijk aan 1 leven damage dat je doet.")
  time.sleep(2)
if tutorial == False:
  name = "Warre"
  char = "1"

all_sprites_list = pygame.sprite.Group()

PlayerChar = Player(char, 40, 60, 70)
PlayerChar.rect.x = 100
PlayerChar.rect.y = 300
stappen = 0

Monster1 = Monster("Green", 40, 60, attackm, healthm)
Monster1.rect.x = 500
Monster1.rect.y = 300

all_sprites_list.add(PlayerChar)
all_sprites_list.add(Monster1)

mouse = pygame.mouse.get_pos() 

while carryOn:
  while health > 0:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                     health = 0
                     carryOn=False
            if event.type == pygame.MOUSEBUTTONDOWN: 
              if SCREENWIDTH/2 <= mouse[0] <= SCREENWIDTH/2+90 and SCREENHEIGHT/2 <= mouse[1] <= SCREENHEIGHT/2+40:  
                  start = False 
                  screen.fill(GREY)
                  pygame.display.flip()

        keys = pygame.key.get_pressed()
        #Naar links
        if keys[pygame.K_a]:
            stappen -= 5
            PlayerChar.moveLeft(5, stappen)
            if stappen < -200:
              print("max")
        #Naar rechts
        if keys[pygame.K_d]:
            stappen += 5
            PlayerChar.moveRight(5, stappen)
            if healthm <= 0:
              if stappen > 450:
                PlayerChar.moveLeft(450, stappen)
                stappen = 0
                healthm = 10
                Monster1 = Monster("Green", 40, 60, attackm, healthm)
                Monster1.rect.x = 500
                Monster1.rect.y = 300
                all_sprites_list.add(Monster1)
                nextarrow = myfont.render(" ", False, (0, 0, 0))
                screen.blit(nextarrow,(500,300))
                level += 1
            if stappen > 450:
              print("max")

                

        #Attack (Q)
        if keys[pygame.K_q]: 
          if Played == False:
            if healthm > 0:
              Played = True

              #Attack
              print("Je valt het monster aan!")
              ultra = random.randint(1,10)
              defense = random.randint(1,5)
              if ultra == 3: 
                damage = strenght + strenght
                print("\n"+"Je deed meer schade dan normaal!"+"\n")
              else:
                damage = strenght

              if defense == 3:
                damage = 0
                print("Het monster ontweek je aanval")
              else:
                damage = damage
              healthm -= damage
              
              if healthm > 0:
                print(healthm)
              else:
                print("Het monster is dood")
            
            

        if keys[pygame.K_f]:
          defensePlr = True
          print("Je hebt meer kans dat je de volgende aanval ontwijkt")
          Played = True
        
        screen.fill(GREY)

        if start == True:
          text = myfont.render("Start", False, (0,0,0))
          screen.blit(text , (SCREENWIDTH/2,SCREENHEIGHT/2))

        if start == False:
          textsurface = myfont.render("HEALTH: "+str(health), False, (0, 0, 0))
          textsurface2 = myfont.render("STRENGHT: "+str(strenght), False, (0, 0, 0))
          textlevel = myfont.render("LEVEL: "+str(level), False, (0, 0, 0))
          textattack = myfont.render("|Q: Attack|", False, (0, 0, 0))
          textdefend = myfont.render("|W: Defend|", False, (0, 0, 0))

          screen.blit(textsurface,(0,0))
          screen.blit(textsurface2,(0,20))
          screen.blit(textlevel,(350,0))
          screen.blit(textattack,(240,450))
          screen.blit(textdefend,(350,450))

          text = myfont.render("Started", False, (GREY))
          screen.blit(text , (SCREENWIDTH/2,SCREENHEIGHT/2))

          all_sprites_list.update()
          all_sprites_list.draw(screen)

        if Played == True:
          if healthm > 0:
            time.sleep(1)
            attack_or_defend_m = random.choice(["valt aan", "verdedigd"])
            print("\n"+"Het monster "+attack_or_defend_m+"\n")
          Played = False

        if healthm <= 0:
          pygame.sprite.Sprite.kill(Monster1) #Verwijderd monster

          #verandert stats
          strenght += 1
          healthm = health*2
          attackm += 1

          #arrow
          nextarrow = myfont.render("Next --> ", False, (0, 0, 0))
          screen.blit(nextarrow,(500,300))


        mouse = pygame.mouse.get_pos()  

        #Refresh Screen
        pygame.display.flip()

        #Frames per second
        clock.tick(30)
        
  carryOn = False
pygame.quit()