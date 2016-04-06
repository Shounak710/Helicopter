import pygame
import time
import random
pygame.init()
display_width=800
display_height=700
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Helicopter')
clock=pygame.time.Clock()
copterImg=pygame.image.load('helicopter.gif')

def obst_miss(missed):
    font = pygame.font.SysFont(None,25)
    text=font.render("Score: "+str(missed),True,(255,0,0))
    gameDisplay.blit(text,(0,0))
    
def copter(x,y):
    gameDisplay.blit(copterImg,(x,y))

def obst(obstx,obsty,obstw,obsth,color):
    pygame.draw.rect(gameDisplay,color,[obstx,obsty,obstw,obsth])

def text_objects(text,font):
    textSurface=font.render(text,True,(255,0,0))
    return textSurface,textSurface.get_rect()

def display(text):
    Text=pygame.font.Font('freesansbold.ttf',100)
    TextSurf,TextRect =text_objects(text,Text)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(3)
    
    game_loop()

def crash():
    display('Game Over')

copter_height=91

def game_loop():    
    x=(display_width*0.10)
    y=(display_height*0.35)
    
    y_change = 0
    
    obst_speed=-8
    obst_width=100
    obst_height=200
    obst_startx=100
    obst_starty=random.randrange(-display_height+obst_height,0)

    missed=0
    

    
    gameExit=False

    while not gameExit:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_DOWN:
                   y_change=5
               if event.key==pygame.K_UP:
                   y_change=-5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_DOWN or event.key==pygame.K_UP:
                   y_change==0                                            

        y+=y_change
            
        gameDisplay.fill((0,0,0))
        obst(obst_startx,obst_starty,obst_width,obst_height,(196,234,255))
        obst_startx+=obst_speed
        copter(x,y)
        
        obst_miss(missed)
        
        if y<0 or y>display_height-copter_height:
            crash()

        if obst_startx<0:
            obst_startx=display_width
            obst_starty=random.randrange(0,display_height-obst_height)
            missed+=1
            obst_speed-=0.5

        if x + 295>obst_startx and x+295<obst_startx+obst_width and y+copter_height>obst_starty and y+copter_height<obst_starty+obst_height:
            crash()
        
        pygame.display.update()
        clock.tick(60)
        

game_loop()
pygame.quit()
quit()
