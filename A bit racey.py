import pygame,time,random

pygame.init()

crash_sound = pygame.mixer.Sound('Crash.wav')
pygame.mixer.music.load('jazz.wav')

display_width = 800
display_height = 600
center_x = display_width/2
center_y = display_height/2

black = (0,0,0)
grey = (100,100,100)
light_grey = (200,200,200)
white = (255,255,255)
dark_red = (150,0,0)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
dark_yellow = (200,200,0)
orange = (255,128,0)

car_height = 90
car_width = 75

pause = False
lvl = 0
lvl_name = ""
dodged = 0
#crash = True
  
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("A Bit Racey")
clock = pygame.time.Clock()

carImg = pygame.image.load('race_car.png')
caricon = pygame.image.load('caricon.png')

pygame.display.set_icon(caricon)

def coin(coinx,coiny):
    pygame.draw.circle(gameDisplay,orange,[coinx,coiny],12)
    pygame.draw.circle(gameDisplay,yellow,[coinx,coiny],8)
    
def stats(count,text,y):
    font = pygame.font.SysFont(None,25)
    textsurf = font.render(text + str(count), True, green)
    gameDisplay.blit(textsurf, (0,y))
    
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y,img):
    gameDisplay.blit(img,(x,y))

def text_objects(text,font,color):
    textsurf = font.render(text, True, color)
    return textsurf, textsurf.get_rect()

def msg_display(msg,color,size,posx,posy):
    font = pygame.font.SysFont(None,size)
    textsurf, textrect = text_objects(msg, font, color)
    textrect.center = ((posx),(posy))
    gameDisplay.blit(textsurf, textrect)

    pygame.display.update()

def crash():
    global dodged
    
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again",100,350,260,100,bright_green,green,'again')
        button("Quit!",500,350,260,100,bright_red,red,'quit')
        button("Back",center_x-85,500,170,70,bright_green,green,"back")
        
        msg_display('You Crashed!!',dark_red,150,center_x,200)
        msg_display('Score='+str(dodged),black,100,center_x,100)
        
        clock.tick(15)

def button(msg,x,y,w,h,ac,dc,action=None):
    global lvl
    global lvl_name
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
            if click[0] == 1 and action != None:
                if action == "again":
                    game_loop()
                if action == 'play':
                    level_page()
                if action == 'quit':
                    pygame.quit()
                    quit()
                if action == "unpause":
                    unpause()
                if action == "help":
                    help_me()
                if action == "back":
                    game_intro()
                if action == 'easy':
                    lvl_name = 'easy'
                    lvl = 3
                    game_loop()
                if action == 'normal':
                    lvl_name = 'normal'
                    lvl = 2
                    game_loop()
                if action == 'hard':
                    lvl_name = 'hard'
                    lvl = 1
                    game_loop()
    else:
        pygame.draw.rect(gameDisplay,dc,(x,y,w,h))

    msg_display(msg,black,70,x+(w/2),y+(h/2))

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue",100,400,250,100,bright_green,green,"unpause")
        button("Quit!",500,400,250,100,bright_red,red,'quit')
        
        msg_display('Paused',black,200,center_x,200)
        clock.tick(15)

def help_me():

    gameDisplay.fill(grey)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Back",100,500,130,70,bright_green,green,"back")
        
        msg_display('Help',black,115,center_x,70)
        msg_display("Left arrow or A to go left",black,50,center_x,250-50)
        msg_display("Right arrow or D to go right",black,50,center_x,center_y-50)
        msg_display("Collect the yellow coins",black,50,center_x,center_y+50)
        msg_display("to avoid the blocks faster",black,50,center_x,center_y+90)
        clock.tick(15)

def level_page():
    global lvl
    global lvl_name

    gameDisplay.fill(grey)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        button('easy',display_width/4-85,300,170,100,bright_green,green,'easy')
        button('normal',display_width/2-85,300,170,100,bright_green,green,'normal')
        button('hard',display_width-display_width/4-85,300,170,100,bright_green,green,'hard')
        button("Back",center_x-85,500,170,70,bright_green,green,"back")
        
        msg_display('Levels',black,115,center_x,70)
        
        clock.tick(15)


def game_intro():
    

    intro = True
    gameDisplay.fill(grey)
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Go!!",100,400,200,100,bright_green,green,'play')
        button("Quit!",500,400,200,100,bright_red,red,'quit')
        button("help",0,0,110,90,bright_green,green,"help")
        
        msg_display('A Bit Racey',black,200,center_x,200)
        clock.tick(15)
    

def game_loop():
    global pause
    global lvl_name
    global dodged
    pygame.mixer.music.play(-1)
    

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_x = random.randrange(0,display_width)
    thing_y = -600
    thing_speed = 3
    thing_width = 100
    thing_height = 100

    thing_a=-120
    thing_b=0
    thing_c=120
    thing_d=240
    thing_e=360
    thing_f=480

    coin_x = random.randrange(10,display_height - 10)
    coin_y = -700

    car_speed = 3

    dodged = 0
    
    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -car_speed
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = car_speed
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
            

        x += x_change

        gameDisplay.fill(grey)

        #things(0,0,40,display_height,light_grey)

        things(display_width*0.45,thing_a,30,60,white)
        things(display_width*0.45,thing_b,30,60,white)
        things(display_width*0.45,thing_c,30,60,white)
        things(display_width*0.45,thing_d,30,60,white)
        things(display_width*0.45,thing_e,30,60,white)
        things(display_width*0.45,thing_f,30,60,white)

        thing_a+=thing_speed
        thing_b+=thing_speed
        thing_c+=thing_speed
        thing_d+=thing_speed
        thing_e+=thing_speed
        thing_f+=thing_speed
        
        things(thing_x,thing_y,thing_width,thing_height,dark_red)
        thing_y += thing_speed
        
        car(x,y,carImg)
        
        coin(coin_x,coin_y)
        coin_y += thing_speed
        
        stats(dodged,"Dodged=",0)
        stats(thing_speed,"Your speed=",20)
        stats(car_speed,"Avoiding speed=",40)
        stats(lvl_name,"level=",60)
        
        if x < 1: 
            x = 0
        if x > display_width - car_width - 1:
            x = display_width - car_width
        if y < thing_y + thing_height and thing_y < y + car_height:
            if x < thing_x + thing_width and x > thing_x:
                crash()
            if x + car_width < thing_x + thing_width and x + car_width > thing_x:
                crash()
        if coin_x < x + car_width and coin_x > x:
            if coin_y > y:
                car_speed += 1
                coin_y = -700
                coin_x = random.randrange(10,display_height - 10)

        if thing_a > display_height:
            thing_a = -120
        if thing_b > display_height:
            thing_b = -120
        if thing_c > display_height:
            thing_c = -120
        if thing_d > display_height:
            thing_d = -120
        if thing_e > display_height:
            thing_e = -120
        if thing_f > display_height:
            thing_f = -120

        if thing_y > display_height:
            thing_y = 0 - thing_height
            thing_x = random.randrange(0,display_width)
            dodged += 1
            if dodged % lvl == 0:
                thing_speed += 1
        if coin_y > display_height:
            coin_y = -700
            coin_x = random.randrange(10,display_height - 10)
            
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()            
