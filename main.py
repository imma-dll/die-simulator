import pygame    #importing module
from random import randint  #for generating random integer
pygame.init()    #intializes all pygame modules

#specs for display window
display_height=600
display_width = 800

all_fonts=pygame.font.get_fonts() #all available fonts enumerated in all_fonts list
faces=[pygame.image.load('images/x1.png'),pygame.image.load("images/x2.png"),pygame.image.load("images/x3.png"),pygame.image.load("images/x4.png"),pygame.image.load("images/x5.png"),pygame.image.load("images/x6.png")]
#color tuples
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
light_blue = (0,0,100)
blue=(0,0,255)
green=(0,255,0)
light_red=(100,0,0)

space=False
clock = pygame.time.Clock()     #pygame's clock
screen = pygame.display.set_mode((display_width,display_height)) #Generates a 'screen' window
pygame.display.set_caption('Die Simulator')                      #object with given specs and title

############################################

def text_objects(text,font,color):
    textSurface=font.render(text,True,color)
    return textSurface,textSurface.get_rect()

def message_display(text,color):
    largeText=pygame.font.SysFont(all_fonts[6],50)
    TextSurf,TextRect=text_objects(text,largeText,color)
    TextRect.center=((display_width/2),(display_height/2))
    screen.blit(TextSurf,TextRect)
    pygame.display.update()

############################################

def button(message,x,y,w,h,ic,ac):  #ic=inactive color; ac=active color
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            action()

    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    smallText=pygame.font.SysFont(all_fonts[7],14)
    textSurf,textRect=text_objects(message,smallText,black)
    textRect.center=((x+(w/2)),(y+(h/2)))
    screen.blit(textSurf,textRect)

############################################

def action():
    game_loop()

############################################

def rolling_dice():
    n=randint(0, 5)
    screen.fill(light_red)
    screen.blit(faces[n], (display_width / 2, display_height / 2))
    pygame.display.flip()
    return n

############################################

def game_intro():
    intro = True  # variable for intro loop
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # checking if user want to end the program
                intro = False  # breaks the loop

        screen.fill(white)  #fill screen with white color
        message_display('Die Simulator',red)        #function to display a message
        button("Press to roll the dice",(display_width/2-100),(display_height/2+60),200,34,light_blue,blue) #creating button
        pygame.display.flip()  # flip() updates the whole screen
        clock.tick(15)  #sets fps=60

    pygame.quit()  # exits pygame
    quit()  # exits python

############################################

def game_loop():
    roll = True
    running = True  # variable for controlling game loop
    while running:
        for event in pygame.event.get():    #emptying event queue
            if event.type == pygame.QUIT:  # checking if user want to end the program
                running = False  # breaks the loop
        if roll:
            for time_delay in range(1,30):
                num=rolling_dice()
                pygame.time.delay((time_delay**2)//2)
        roll=False
        screen.fill(white)
        message_display('You have got a '+str(num+1)+' !',green)
        screen.blit(faces[num], (display_width / 2, display_height / 2))
        pygame.display.flip()  # flip() updates the whole screen
        clock.tick(60)  # sets fps=60

    pygame.quit()  # exits pygame
    quit()  # exits python

############################################

game_intro()           #calling intro loop