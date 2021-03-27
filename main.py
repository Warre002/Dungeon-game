import pygame, random, time
from player import Player
from monster import Monster

pygame.init()

#player stats 
tutorial = False
start = True
Help = False

health = 10
strenght = 1
defensePlr = False
Played = False
level = 0

#Other stats
attackm = 0
healthm = 3
defenseM = False
healthm2 = healthm

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
              if start == True:
                  if SCREENWIDTH/2 <= mouse[0] <= SCREENWIDTH/2+90 and SCREENHEIGHT/2 <= mouse[1] <= SCREENHEIGHT/2+40:  
                    start = False 
                    screen.fill(GREY)
                    pygame.display.flip()
                  if SCREENWIDTH/2 <= mouse[0] <= SCREENWIDTH/2+90 and SCREENHEIGHT/2+30 <= mouse[1] <= SCREENHEIGHT/2+70: 
                    start = False
                    Help = True
                    screen.fill(GREY)
                    pygame.display.flip()
              if Help == True:
                  if 260 <= mouse[0] <= 380 and 380 <= mouse[1] <= 470:
                    Help = False
                    Start = True
                    screen.fill(GREY)
                    pygame.display.flip()
                  

        keys = pygame.key.get_pressed()

        #Naar links
        if keys[pygame.K_a]:
          if stappen > -200: 
            stappen -= 5
            PlayerChar.moveLeft(5, stappen)

        #Naar rechts
        if keys[pygame.K_d]:
          if stappen < 450:
            stappen += 5
            PlayerChar.moveRight(5, stappen)
          elif stappen >= 450:
            if healthm <= 0:
              print("Next level")
              PlayerChar.rect.x = 100
              PlayerChar.rect.y = 300
              stappen = 0
              Monster1 = Monster("Green", 40, 60, attackm, healthm)
              Monster1.rect.x = 500
              Monster1.rect.y = 300
              all_sprites_list.add(Monster1)
              nextarrow = myfont.render(" ", False, (0, 0, 0))
              screen.blit(nextarrow,(500,300))
              
              level += 1
              strenght += 1
              healthm = healthm2*2
              healthm2 = healthm
              attackm += 1
                    

        #Attack (Q)
        if keys[pygame.K_q]: 
          if Played == False:
            if healthm > 0:
              Played = True

              #Attack
              print("Je valt het monster aan!")
              ultra = random.randint(1,10)
              defense = random.randint(1,10)
              if ultra == 3: 
                damage = strenght + strenght
                print("\n"+"Je deed meer schade dan normaal!")
              else:
                damage = strenght

              if defenseM == False:
                if defense == 3:
                  damage = 0
                  print("Het monster ontweek je aanval")
                else:
                  damage = damage
                  healthm -= damage
              else:
                if defense <= 3:
                  damage = 0
                  print("Het monster ontweek je aanval")
                else:
                  damage = damage
                  healthm -= damage
              
              if healthm > 0:
                print("Het monster heeft nog "+str(healthm)+" levens.")            
                healthm = int(healthm)
              else:
                print("Het monster is dood")
            
            

        if keys[pygame.K_w]:
          defensePlr = True
          print("Je hebt meer kans dat je de volgende aanval ontwijkt")
          Played = True
        
        screen.fill(GREY)

        if start == True:
          text = myfont.render("Start", False, (0,0,0))
          texthelp = myfont.render("Help", False, (0,0,0))
          screen.blit(text , (SCREENWIDTH/2,SCREENHEIGHT/2))
          screen.blit(texthelp , (SCREENWIDTH/2,SCREENHEIGHT/2+30))

        if Help == True:
          text = myfont.render("", False, (0,0,0))
          texthelp = myfont.render("", False, (0,0,0))
          screen.blit(text , (SCREENWIDTH/2,SCREENHEIGHT/2))
          screen.blit(texthelp , (SCREENWIDTH/2,SCREENHEIGHT/2+30))


          helptop = myfont.render("Hier vind je informatie over de controles en het doel van het spel", False, (0, 0, 0))

          #Controles help
          helpcontroles = myfont.render("Controles/Toetsen:", False, (0, 0, 0))
          help1 = myfont.render("A: Loop naar links", False, (0, 0, 0))
          help2 = myfont.render("D: Loop naar rechts", False, (0, 0, 0))
          help3 = myfont.render("Q: Val het monster aan (Het monster kan het afwijken)", False, (0, 0, 0))
          help4 = myfont.render("W: Verdedig, je hebt een grote kans dat je geen levens verliest", False, (0, 0, 0))

          #Info Game
          helpgame = myfont.render("Info over het spel:", False, (0, 0, 0))
          help5 = myfont.render("Je moet monsters vermoorden zodat je sterken wordt en naar ", False, (0, 0, 0))
          help6 = myfont.render("het volgend level kan gaan.", False, (0, 0, 0))
          help7 = myfont.render("Je wint het spel wanneer je level 20 behaald hebt, ", False, (0, 0, 0))
          help8 = myfont.render("je verliest wanneer je health 0 is.", False, (0, 0, 0))
          helpback = myfont.render("START GAME", False, (0, 0, 0))

          #Zet op scherm
          screen.blit(helptop,(25,25))
          
          screen.blit(helpcontroles,(250,70))
          screen.blit(help1,(40,120))
          screen.blit(help2,(40,150))
          screen.blit(help3,(40,180))
          screen.blit(help4,(40,210))
         
          screen.blit(helpgame,(250,260))
          screen.blit(help5,(40,290))
          screen.blit(help6,(40,320))
          screen.blit(help7,(40,360))
          screen.blit(help8,(40,390))
          
          screen.blit(helpback,(290,450))

        if start == False and Help == False:
          textplrstats = myfont.render("PLAYER STATS: ", False, (0, 0, 0))
          textsurface = myfont.render("HEALTH: "+str(health), False, (0, 0, 0))
          textsurface2 = myfont.render("STRENGHT: "+str(strenght), False, (0, 0, 0))
          textlevel = myfont.render("LEVEL: "+str(level), False, (0, 0, 0))
          textattack = myfont.render("|Q: Attack|", False, (0, 0, 0))
          textdefend = myfont.render("|W: Defend|", False, (0, 0, 0))

          screen.blit(textplrstats,(0,0))
          screen.blit(textsurface,(0,20))
          screen.blit(textsurface2,(0,40))
          screen.blit(textlevel,(310,0))
          screen.blit(textattack,(240,450))
          screen.blit(textdefend,(350,450))

          text = myfont.render("", False, (0,0,0))
          screen.blit(text , (SCREENWIDTH/2,SCREENHEIGHT/2))
          texthelp = myfont.render("", False, (0,0,0))
          screen.blit(texthelp , (SCREENWIDTH/2,SCREENHEIGHT/2+30))
          all_sprites_list.update()
          all_sprites_list.draw(screen)

        if Played == True:
          if healthm > 0:
            time.sleep(1)
            attack_or_defend_m = random.choice(["valt aan", "verdedigd"])
            if attack_or_defend_m == "valt aan":
              #Dit is gewoon voor de speler meer kans te geven
              isittrue = random.choice(["valt aan", "verdedigd"])
              attack_or_defend_m = isittrue

            #print wat het monster doet
            print("\n"+"Het monster "+attack_or_defend_m+"\n")

            #Het monster valt aan
            if attack_or_defend_m == "valt aan":
              defenserandom = random.randint(1,10)
              if defensePlr == True:  
                if defenserandom != 1:
                  print("Je hebt de aanval kunnen ontwijken!")
                if defenserandom == 1:
                  health -= attackm
                  attackm = str(attackm)
                  print("Het monster heeft je kunnen aanvallen! Je verliest "+attackm)
                  attackm = int(attackm)

              if defensePlr == False:  
                if defenserandom <= 4:
                  print("Je hebt de aanval kunnen ontwijken!")
                if defenserandom > 4:
                  health -= attackm
                  attackm = str(attackm)
                  print("Het monster heeft je kunnen aanvallen! Je verliest "+attackm)
                  attackm = int(attackm)
                defensePlr = False

            if attack_or_defend_m == "verdedigd":
              defenseM = True
          Played = False

        if healthm <= 0:
          pygame.sprite.Sprite.kill(Monster1) #Verwijderd monster

          #verandert stats


          #arrow
          nextarrow = myfont.render("Next level --> ", False, (0, 0, 0))
          screen.blit(nextarrow,(500,300))


        mouse = pygame.mouse.get_pos()  

        #Refresh Screen
        pygame.display.flip()

        #Frames per second
        clock.tick(30)
        
  carryOn = False
pygame.quit()