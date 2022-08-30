"""
1. make sure all of these are in the same file as your .py file i.e. this file
2. work through the code below they are numbered and have sub numbers work in order of number than decimal
3. Try Running after every step after 3
4. Don't delete comments that you have finished
"""

import pygame
import numpy as np
import traceback

# 0. initiate pygame
pygame.init()


try:
    # 1 initiate a pygame window name it screen remember it looks like 
    screen = pygame.display.set_mode((800,230)) #make it 800 x 230
    

    # 1.2 set up a variable for the while loop = running set FPS (try 60 to start)
    running = True
    FPS = 60
    
    #initiating clock
    clock = pygame.time.Clock()
    
    # 4. Set the caption name pygame.display.set_caption()
    pygame.display.set_caption("Dino Jump")
    # 5.1 load your background image call it background pygame.image.load("name.png")
    
    background = pygame.image.load("ground.png")
    
    """ Player """
    # 6.1 uncomment next 4 lines upload your player image to player
    player = pygame.image.load("dino.png")
    playerX = 20
    playerY = 170
    player = pygame.transform.scale(player, (44,48))
    
    # 8.1 read the names of next 4 variables think about how they will be used then uncomment them
    gravity = -0.25
    play_up = 7
    jumping = False
    j_time = 0
    
    #8.2 this is your player hitbox, uncomment next line (variables are tested to work)
    player_hitbox = pygame.Rect(playerX+5,playerY, 29, 43)
    
    
    # 8.3 uncomment these next 2 functions deal with the players jump, they
    # may be a little hard to understand. It is ok if you don't get them
    # They will be commented to help you understand them if you are curious

    
    # This function is called to initialize a player jump 
    def jump():
        global playerY, jumping, j_time, play_up, gravity
        # Moves the player up on the screen
        playerY -= play_up
        #Lets program know the character is jumping
        jumping = True
        
    #This updates the players position and hitbox
    def update_player():
        global playerX, playerY, jumping, j_time, play_up, gravity, player_hitbox
        #checks if player is in the middle of jump and continues the jump
        if playerY < 170:
            #calculates velocity from V0, acceleration, and time
            play_up = play_up + j_time * gravity
            # adds player velocity to position
            playerY -= play_up
            #adds to amount of time of the jump
            j_time += 0.15
        
        #checks if jump is finished then resets the jump if it has
        if playerY > 170:
            playerY = 170
            j_time = 0
            play_up = 7
            jumping = False
        
        #updates platers hitbox
        player_hitbox = pygame.Rect(playerX+5,playerY, 29, 43)
        


    """ Cactus """
    
    # 7.1 load your food image add a vaiable for it's X position and Yposition
    # use pygame.image.load("name.png") to load your cactus image and uncomment next 4/5 lines
    cactus = pygame.image.load("cacti.png")
    cactus = pygame.transform.scale(cactus, (45,44))
    cactusX = np.random.randint(800, 1200)
    cactusY = 170
    cactus_speed = 4
    
    # set up the cactus_hitbox with w=45, h=44
    cactus_hitbox = pygame.Rect(cactusX,cactusY, 45, 44)


    
    def update_cactus():
        global cactusX, cactus_speed, cactus_hitbox
        # 7.3 subtact cactus_speed from cactusX to move the catus to the left
        cactusX-= cactus_speed
        # 7.4 check if cactus has hit left side of screen i.e. cactusX<-30 give it random X val from 800-1200
        if cactusX < -30:
            cactusX = np.random.randint(800,1200)
            
        # 7.5 update cactus hitbox
        cactus_hitbox = pygame.Rect(cactusX,cactusY, 45, 44)
        
            
    
    """ Scores """
    font = pygame.font.Font("freesansbold.ttf", 20)
    score_value = 0
    highscore_value = 0
    
    # This function updates the scores if you have time read over it at the time
    def update_scores(collision):
        global score_value, highscore_value, score
        if collision:
            score_value = 0
        score = font.render("Score: " + str(int(score_value)), True, (200, 200, 200))
        score_value += 0.25
        highscore_value = max(highscore_value, score_value)
        high_score = font.render("High Score: " + str(int(highscore_value)), True, (200, 200, 200))
        screen.blit(score, (650, 30))
        screen.blit(high_score, (450, 30))


    #  6/7 blit in cactus and player
    def drawall():
        global screen
        screen.blit(player,(playerX,playerY))
        screen.blit(cactus,(cactusX,cactusY))


    # 2.1 Start your while loop with runing as a variable
    while running:
        clock.tick(FPS) # Controlling Frames Per Second
        # 5.2 blit your background uncomment next 2 lines
        screen.fill((255,255,255))
        screen.blit(background, (0, 200))

        # 3.1 check each event with a for loop pygame.event.get() gives you a list of events
        for event in pygame.event.get():
            # 3.2 end the while loop if the event.type is pygame.QUIT if so set running = False
            if event.type == pygame.QUIT:
                running = False
            # 9.1 make an if statement to check if event.type is a pygame.KEYDOWN event
            if event.type == pygame.KEYDOWN:
                # 9.2 check what key event.key is check if it is pygame.K_SPACE
                #run jump() function if true
                if event.key == pygame.K_SPACE:
                    jump()
                


        # 10 use colliderect()  to find out if the player collided with cactus then uncomment update_scores
        collision = player_hitbox.colliderect(cactus_hitbox)
        update_scores(collision)
        
        
        # you will build these functions above
        # 6.2 uncomment next line
        update_player()
        
        
        # 7. uncomment next line
        update_cactus()
        
        drawall()

        # 2.2 start updating your pygame display pygame.display.update()
        pygame.display.update()
        
        
except:
    # your traceback call
    traceback.print_exc()

finally:
    # add in your quit statements
    pygame.display.quit()
    pygame.quit()