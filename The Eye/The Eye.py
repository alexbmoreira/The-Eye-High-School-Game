white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
gold = (255, 215, 0)
gold2 = (231,195,1)
grey = (128,128,128)
skin = (255,238,204)
ground = (176,186,156)
wall = (99,77,77)
pink = (255,99,154)
lightBlue = (0,206,209)

gamestate = "Main Menu"

import pygame
import random

def collideRectRect (x1,y1,w1,h1,x2,y2,w2,h2):
    return x1 <= x2+w2 and x1+w1 >= x2 and y1 <= y2+h2 and y1+h1 >= y2


def collideRectRectLocation (x1,y1,w1,h1,x2,y2,w2,h2):
    if collideRectRect (x1,y1,w1,h1,x2,y2,w2,h2) == True:
        collisionLeft = x2 + w2 - x1
        collisionRight = x1 + w1 - x2
        collisionTop = y2 + h2 - y1
        collisionBottom = y1 + h1 - y2
        if (collisionLeft <= collisionBottom and collisionLeft <= collisionTop and collisionLeft <= collisionRight):
            return "left" 
        elif (collisionRight <= collisionBottom and collisionRight <= collisionTop and collisionRight <= collisionLeft):
            return "right" 
        elif (collisionTop <= collisionBottom and collisionTop <= collisionLeft and collisionTop <= collisionRight): 
            return "top" 
        elif (collisionBottom <= collisionTop and collisionBottom <= collisionLeft and collisionBottom <= collisionRight): 
            return "bottom" 
    else:
        return "none"

def mouseDown (mouseX, mouseY):
    print ("Mouse is down at " + str(mouseX) + ", " + str(mouseY))

def mouseUp (mouseX, mouseY):
    print ("Mouse is up at " + str(mouseX) + ", " + str(mouseY))

def keyDown (key):
    global keyW, keyA, keyS, keyD, gamestate, score, level, numEnemies, done, boss, killedBoss, keyDim, bossHits, hasKey, coin, boy, girl

    if gamestate == "Main Menu":
        if event.key == pygame.K_SPACE:
            gamestate = "Play"
            pygame.mixer.music.load('sounds/Lavender Town.ogg')
            pygame.mixer.music.play(-1)
            
        if event.key == pygame.K_h:
            gamestate = "How to Play"

        if event.key == pygame.K_g:
            player[6] = pink
            girl = True
            boy = False

        if event.key == pygame.K_b:
            player[6] = lightBlue
            boy = True
            girl = False
            
    if gamestate == "How to Play":
        if event.key == pygame.K_SPACE:
            gamestate = "Main Menu"

    if gamestate == "End Game":
        if event.key == pygame.K_SPACE:
            gamestate = "Main Menu"

    if gamestate == "Mid Level":
        if event.key == pygame.K_SPACE:
            score = score + 1000
            level = level + 1
            player[0] = 5
            player[1] = 20
            player[4] = 0
            player[5] = 0
            if level == 10:
                numEnemies = 15
            if level == 7:
                numEnemies = 15
                boss = [[random.randint(50,screen.get_width() - 80), random.randint(50,screen.get_height() - 95), 50, 50, random.randint(-5,-3), random.randint(-5,-3), blue]]
                killedBoss = [False]
                bossHits = [0]
            if level == 4 or level == 10:
                keyDim = [random.randint(50, 725), random.randint(15, 585 - 30), 25, 30, gold]
                hasKey = False
            if level == 2 or level == 5 or level == 8:
                coin = [700, 20, 25, 25, gold]

            if level < 4:
                numEnemies = numEnemies + 5
                for i in range(numEnemies):
                        #               0                                           1                             2   3             4                  5                 6
                        enemy = [random.randint(50,screen.get_width() - 30), random.randint(50,screen.get_height() - 30), 30, 30, random.randint(-3,-1), random.randint(-3,-1), blue]
                        enemies.append(enemy)
            if level == 6:
                numEnemies = 10
                for i in range(len(enemies)):
                    enemies[i][6] = grey
            if level != 6:
                for i in range(len(enemies)):
                    enemies[i][6] = blue
            for i in range(numEnemies):
                enemies[i][0] = random.randint(50,screen.get_width() - 30)
                enemies[i][1] = random.randint(15,screen.get_height() - 80)
                enemies[i][4] = random.randint(-3,-1)
                enemies[i][5] = random.randint(-3,-1)
            gamestate = "Play"

    if gamestate == "Play":
        if event.key == pygame.K_p:
            gamestate = "Pause"

        if bullet[0] > 800 or bullet[0] < 0 or bullet[1] > 600 or bullet[1] < 0:
            if event.key == pygame.K_w:
                bullet[0] = (player[0] + (player[2] / 2))
                bullet[1] = (player[1] + (player[3] / 2))
                bullet[2] = 5
                bullet[3] = 10
                bullet[4] = 0
                bullet[5] = -15
            if event.key == pygame.K_a:
                bullet[0] = (player[0] + (player[2] / 2))
                bullet[1] = (player[1] + (player[3] / 2))
                bullet[2] = 5
                bullet[2] = 10
                bullet[3] = 5
                bullet[4] = -15
                bullet[5] = 0
            if event.key == pygame.K_s:
                bullet[0] = (player[0] + (player[2] / 2))
                bullet[1] = (player[1] + (player[3] / 2))
                bullet[2] = 5
                bullet[2] = 5
                bullet[3] = 10
                bullet[4] = 0
                bullet[5] = 15
            if event.key == pygame.K_d:
                bullet[0] = (player[0])
                bullet[1] = (player[1] + (player[3] / 2))
                bullet[2] = 5
                bullet[2] = 10
                bullet[3] = 5
                bullet[4] = 15
                bullet[5] = 0
                    
                
        if event.key == pygame.K_UP:
            player[5] = -5
        elif event.key == pygame.K_LEFT:
            player[4] = -5
        elif event.key == pygame.K_DOWN:
            player[5] = 5
        elif event.key == pygame.K_RIGHT:
            player[4] = 5
        
    if gamestate == "Pause":
        if event.key == pygame.K_SPACE:
            gamestate = "Play"

def keyUp (key):

    if gamestate == "Play":
        if event.key == pygame.K_UP:
            player[5] = 0
        elif event.key == pygame.K_LEFT:
            player[4] = 0
        elif event.key == pygame.K_DOWN:
            player[5] = 0
        elif event.key == pygame.K_RIGHT:
            player[4] = 0


pygame.init()
screen = pygame.display.set_mode([800,650])
pygame.display.set_caption("The Eye")

#Global Variables      
player = [5, 20, 15, 30, 0, 0, lightBlue]
highScore = 0
boy = True
girl = False

#Game loop
while True:
    # ============================== HANDLE EVENTS ========================= #
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        elif event.type == pygame.KEYDOWN:
            keyDown (event.key)
        elif event.type == pygame.KEYUP:
            keyUp (event.key)
        
    if done == True:
       break
    
    # ============================== MOVE STUFF ============================ #

    if gamestate == "Main Menu":
        level = 1
        player[4] = 0
        player[5] = 0
        player[0] = 5
        player[1] = 20
        
        bullet = [10000, 10000, 10, 5, 0, 0, black]
        enemies = []
        walls = [[0, 65, 50, 535, wall], [0, 0, 800, 15, wall], [735, 0, 65, 535, wall], [0, 585, 800, 15, wall], [-10, 15, 10, 50, wall], [800, 585, 10, 50, wall]]
        startDoor = [47, 15, 3, 50, black]
        endDoor = [735, 535, 10, 50, black]
        coin = [700, 20, 25, 25, gold]
        keyDim = [random.randint(50, 725), random.randint(15, 585 - 30), 25, 30, gold]
        boss = [[random.randint(50,screen.get_width() - 80), random.randint(50,screen.get_height() - 95), 50, 50, random.randint(-5,-3), random.randint(-5,-3), blue]]
        theEye = [365, 265, 70, 70, blue]
        
        
        fontMenuTitle = pygame.font.SysFont(pygame.font.get_fonts()[40], 70)
        fontMenuPressStart = pygame.font.SysFont(pygame.font.get_fonts()[40], 30)
        fontEndReturnMenu = pygame.font.SysFont(pygame.font.get_fonts()[40], 30)
        fontEndScore = pygame.font.SysFont(pygame.font.get_fonts()[40], 50)
        fontGameScoreNum = pygame.font.SysFont(pygame.font.get_fonts()[40], 40)
        fontGameTexts = pygame.font.SysFont(pygame.font.get_fonts()[40], 30)
        fontSmallTexts = pygame.font.SysFont(pygame.font.get_fonts()[40], 15)


        invincible = False
        invincibleTime = 0
        powerupInv = [random.randint(50, 725), random.randint(15, 585 - 30), 20, 20, blue]

        eyeKilled = False
        eyeHits = 0
        eyeTime = 0

        killedEnemies = 0
        bossHits = [0]
        killedBoss = [False]

        hasKey = False
        invGraphic = 0
        coinFlip = 0
        time = 0
        timeSeconds = 0
        timeMinutes = 4
        score = 0
        livesLeft = 3
        openEndDoor = False

            
        numEnemies = 5
        for i in range(numEnemies):
            #                       0                                           1                             2   3             4                      5             6
            enemy = [random.randint(50,screen.get_width() - 80), random.randint(50,screen.get_height() - 95), 30, 30, random.randint(-3,-1), random.randint(-3,-1), blue]
            enemies.append(enemy)

    if gamestate == "Play":
        bullet[0] = bullet[0] + bullet[4]
        bullet[1] = bullet[1] + bullet[5]

        player[0] = player[0] + player[4]
        player[1] = player[1] + player[5]

        if level == 7 or level == 10:
            for i in range(len(boss)):
                boss[i][0] = boss[i][0] + boss[i][4]
                boss[i][1] = boss[i][1] + boss[i][5]

        for i in range(numEnemies):
            enemies[i][0] = enemies[i][0] + enemies[i][4]
            enemies[i][1] = enemies[i][1] + enemies[i][5]
            if enemies[i][0] >= endDoor[0] + 10 and enemies[i][0] <= screen.get_width() or enemies[i][0] <= 47 - enemies[i][2]:
                enemies[i][0] = random.randint(50, 750 - enemies[i][2])

        if player[0] <= (47 - player[2]) and player[1] <= (65 - player[3]) and startDoor[1] == -35:
            startDoor[1] = 15
            openStartDoor = False
        if player[0] >= 50:
            startDoor[1] = 15
            openStartDoor = False

        if player[0] + player[2] < endDoor[0]:
            endDoor[1] = 535

        if level == 1 or level == 4 or level == 7:
            walls = [[0, 65, 50, 535, wall], [0, 0, 800, 15, wall], [735, 0, 65, 535, wall], [0, 585, 800, 15, wall], [-10, 15, 10, 50, wall], [800, 585, 10, 50, wall]]
            levelWalls = []
            levelWalls = [[393, 165, 15, 265, wall], [200, 100, 15, 100, wall], [600, 100, 15, 100, wall], [200, 400, 15, 100, wall], [600, 400, 15, 100, wall]]
            for i in range(len(levelWalls)):
                walls.append(levelWalls[i])
        if level == 2 or level == 5 or level == 8:
            walls = [[0, 65, 50, 535, wall], [0, 0, 800, 15, wall], [735, 0, 65, 535, wall], [0, 585, 800, 15, wall], [-10, 15, 10, 50, white], [800, 585, 10, 50, wall]]
            levelWalls = []
            levelWalls = [[675, 15, 15, 200, wall], [200, 300, 400, 15, wall], [400, 150, 275, 15, wall], [175, 470, 450, 15, wall], [200, 100, 15, 100, wall]]
            for i in range(len(levelWalls)):
                walls.append(levelWalls[i])
        if level == 3 or level == 6 or level == 9:
            walls = [[0, 65, 50, 535, wall], [0, 0, 800, 15, wall], [735, 0, 65, 535, wall], [0, 585, 800, 15, wall], [-10, 15, 10, 50, wall], [800, 585, 10, 50, wall]]
            levelWalls = [[140, 115, 200, 15, wall], [340, 115, 15, 100, wall], [455, 115, 200, 15, wall], [440, 115, 15, 100, wall], [140, 450, 200, 15, wall], [340, 365, 15, 100, wall], [455, 450, 200, 15, wall], [440, 365, 15, 100, wall]]
            for i in range(len(levelWalls)):
                walls.append(levelWalls[i])

        if invincible == True:
            player[6] = white
            invincibleTime = invincibleTime + 1
            if invincibleTime >= 1000:
                if boy == True:
                    player[6] = lightBlue
                if girl == True:
                    player[6] = pink
                invincible = False

        time = time - 1
        if time <= 0:
            time = 100
            timeSeconds = timeSeconds - 1
        if timeSeconds <= 0:
            timeSeconds = 59
            timeMinutes = timeMinutes - 1
        if timeMinutes <= 0:
            gamestate = "End Game"
            pygame.mixer.music.load('Death Sound.ogg')
            pygame.mixer.music.play(1)

        if killedEnemies == 15:
            killedEnemies = 0
            livesLeft = livesLeft + 1

        if level == 10:
            if eyeKilled == False:
                eyeTime = eyeTime + 1
                theEye[4] = grey
                if eyeTime == 700:
                    for i in range(len(enemies)):
                        if enemies[i][0] >= screen.get_width():
                            enemies[i][0] = random.randint(theEye[0], theEye[0] + theEye[2])
                            enemies[i][1] = random.randint(theEye[1], theEye[1] + theEye[3])
                            enemies[i][4] = random.randint(-3,-1)
                            enemies[i][5] = random.randint(-3,-1)
                if eyeTime >= 700 and eyeTime < 1300:
                    theEye[4] = blue
                elif eyeTime == 1300:
                    eyeTime = 200
                    theEye[4] = grey

                
        
    # ============================== COLLISION ============================= #
    if gamestate == "Play":
        if bullet[0] > 800 or bullet[0] < -30 and bullet[1] > 600 or bullet[1] < -30:
            bullet[4] = 0
            bullet[5] = 0

        #Enemies -- Walls
        for i in range(numEnemies):
            for j in range(len(walls)):
                collisionResult = collideRectRectLocation (int(enemies[i][0]),int(enemies[i][1]),int(enemies[i][2]),int(enemies[i][3]),int(walls[j][0]),int(walls[j][1]),int(walls[j][2]),int(walls[j][3]))
                if collisionResult != "none" :
                    if collisionResult == "left" :
                        enemies[i][4] = random.randint(-3,3)
                        enemies[i][0] = walls[j][0] + walls[j][2]
                    elif collisionResult == "right" :
                        enemies[i][4] = random.randint(-3,3)
                        enemies[i][0] = walls[j][0] - enemies[i][2]
                    elif collisionResult == "top" :
                        enemies[i][5] = random.randint(-3,3)
                        enemies[i][1] = walls[j][1] + walls[j][3]
                    elif collisionResult == "bottom" :
                        enemies[i][5] = random.randint(-3,3)
                        enemies[i][1] = walls[j][1] - enemies[i][3]


        #Player -- Walls
        for j in range(len(walls)):
            collisionResult = collideRectRectLocation (int(player[0]),int(player[1]),int(player[2]),int(player[3]),int(walls[j][0]),int(walls[j][1]),int(walls[j][2]),int(walls[j][3]))
            if collisionResult != "none" :
                if collisionResult == "left" :
                    player[4] = 0
                    player[0] = walls[j][0] + walls[j][2]
                elif collisionResult == "right" :
                    player[4] = 0
                    player[0] = walls[j][0] - player[2]
                elif collisionResult == "top" :
                    player[5] = 0
                    player[1] = (walls[j][1] + walls[j][3]) + 1
                elif collisionResult == "bottom" :
                    player[5] = 0
                    player[1] = (walls[j][1] - player[3]) - 1

        #Player -- Starting Door
        collisionResult = collideRectRectLocation (int(player[0]),int(player[1]),int(player[2]),int(player[3]),int(startDoor[0]),int(startDoor[1]),int(startDoor[2]),int(startDoor[3]))
        if collisionResult != "none" :
            if collisionResult == "left" :
                player[0] = startDoor[0] + startDoor[2]
            elif collisionResult == "right" :
                startDoor[1] = -35
                player[0] = startDoor[0] - player[2]

        #Player -- Ending Door
        if collideRectRect (int(player[0]),int(player[1]),int(player[2]),int(player[3]),int(endDoor[0]),int(endDoor[1]),int(endDoor[2]),int(endDoor[3])) == True:
            if level == 4:
                player[0] = endDoor[0] - player[2]
                if hasKey == True:
                    endDoor[1] = 485
            elif level == 7:
                player[0] = endDoor[0] - player[2]
                for i in range(len(killedBoss)):
                    if killedBoss[i] == True:
                        endDoor[1] = 485
            elif level == 10:
                player[0] = endDoor[0] - player[2]
                if eyeKilled == True and hasKey == True:
                    endDoor[1] = 485
            elif level != 4 and level != 7 and level != 10:
                player[0] = endDoor[0] - player[2]
                endDoor[1] = 485

        #Player -- Key
        if level == 4 or level == 10:
            if collideRectRect(int(player[0]), int(player[1]), int(player[2]), int(player[3]), int(keyDim[0]), int(keyDim[1]), int(keyDim[2]), int(keyDim[3])) == True:
                    hasKey = True

        #Key -- Walls
        if level == 4 or level == 10:
            for i in range(len(walls)):
                collisionResult = collideRectRectLocation (int(keyDim[0]),int(keyDim[1]),int(keyDim[2]),int(keyDim[3]),int(walls[i][0]),int(walls[i][1]),int(walls[i][2]),int(walls[i][3]))
                if collisionResult != "none" :
                    keyDim = [random.randint(50, 725), random.randint(15, 585 - 30), 25, 30, gold]

        #Player -- Power Up
        if level == 9:
            if collideRectRect(int(player[0]), int(player[1]), int(player[2]), int(player[3]), int(powerupInv[0]), int(powerupInv[1]), int(powerupInv[2]), int(powerupInv[3])) == True:
                    invincible = True
                    powerupInv[0] = 1000

        #Power Up -- Walls
        if level == 9:
            for i in range(len(walls)):
                collisionResult = collideRectRectLocation (int(powerupInv[0]),int(powerupInv[1]),int(powerupInv[2]),int(powerupInv[3]),int(walls[i][0]),int(walls[i][1]),int(walls[i][2]),int(walls[i][3]))
                if collisionResult != "none" :
                    powerupInv = [random.randint(50, 725), random.randint(15, 585 - 30), 20, 20, blue]


        #Player -- Coin
        if level == 2 or level == 5 or level == 8:
            if collideRectRect(int(player[0]), int(player[1]), int(player[2]), int(player[3]), int(coin[0]), int(coin[1]), int(coin[2]), int(coin[3])) == True:
                score = score + 1000
                coin[0] = 1000
    
        #Enemies -- Starting Door
        for i in range(numEnemies):
            collisionResult = collideRectRectLocation (int(enemies[i][0]),int(enemies[i][1]),int(enemies[i][2]),int(enemies[i][3]),int(startDoor[0]),int(startDoor[1]),int(startDoor[2]),int(startDoor[3]))
            if collisionResult != "none" :
                if collisionResult == "left" :
                    enemies[i][4] = random.randint(-3,3)
                    enemies[i][0] = startDoor[0] + startDoor[2]
                elif collisionResult == "right" :
                    enemies[i][4] = random.randint(-3,3)
                    enemies[i][0] = startDoor[0] - enemies[i][2]
                elif collisionResult == "top" :
                    enemies[i][5] = random.randint(-3,3)
                    enemies[i][1] = startDoor[1] + startDoor[3]
                elif collisionResult == "bottom" :
                    enemies[i][5] = random.randint(-3,3)
                    enemies[i][1] = startDoor[1] - enemies[i][3]

        #Enemies -- Ending Door
        for i in range(numEnemies):
            collisionResult = collideRectRectLocation (int(enemies[i][0]),int(enemies[i][1]),int(enemies[i][2]),int(enemies[i][3]),int(endDoor[0]),int(endDoor[1]),int(endDoor[2]),int(endDoor[3]))
            if collisionResult != "none" :
                if collisionResult == "left" :
                    enemies[i][4] = random.randint(-3,3)
                    enemies[i][0] = endDoor[0] + endDoor[2]
                elif collisionResult == "right" :
                    enemies[i][4] = random.randint(-3,3)
                    enemies[i][0] = endDoor[0] - enemies[i][2]
                elif collisionResult == "top" :
                    enemies[i][5] = random.randint(-3,3)
                    enemies[i][1] = endDoor[1] + endDoor[3]
                elif collisionResult == "bottom" :
                    enemies[i][5] = random.randint(-3,3)
                    enemies[i][1] = endDoor[1] - enemies[i][3]

        #Enemies -- Player
        if invincible == False:
            for i in range(numEnemies):
                if collideRectRect(int(player[0]), int(player[1]), int(player[2]), int(player[3]), int(enemies[i][0]), int(enemies[i][1]), int(enemies[i][2]), int(enemies[i][3])) == True:
                    livesLeft = livesLeft - 1
                    player[0] = 5
                    player[1] = 20
                    if livesLeft <= 0:
                        gamestate = "End Game"
                        pygame.mixer.music.load('Death Sound.ogg')
                        pygame.mixer.music.play(1)

        #Enemies -- Bullet
        for i in range(numEnemies):
            if collideRectRect(int(bullet[0]), int(bullet[1]), int(bullet[2]), int(bullet[3]), int(enemies[i][0]), int(enemies[i][1]), int(enemies[i][2]), int(enemies[i][3])) == True:
                bullet[0] = 10000
                bullet[1] = 10000
                if enemies[i][6] != grey:
                    enemies[i][0] = 1000
                    enemies[i][4] = 0
                    enemies[i][5] = 0
                    score = score + 100
                    killedEnemies = killedEnemies + 1

        #Bullet -- Starting Door
        if collideRectRect(int(bullet[0]), int(bullet[1]), int(bullet[2]), int(bullet[3]), int(startDoor[0]), int(startDoor[1]), int(startDoor[2]), int(startDoor[3])) == True:
            bullet[0] = 10000
            bullet[1] = 10000

        #Bullet -- Wall
        for j in range(len(walls)):
            collisionResult = collideRectRectLocation (int(bullet[0]),int(bullet[1]),int(bullet[2]),int(bullet[3]),int(walls[j][0]),int(walls[j][1]),int(walls[j][2]),int(walls[j][3]))
            if collisionResult != "none" :
                if collisionResult == "left" :
                    bullet[0] = 10000
                    bullet[1] = 10000
                elif collisionResult == "right" :
                    bullet[0] = 10000
                    bullet[1] = 10000
                elif collisionResult == "top" :
                    bullet[0] = 10000
                    bullet[1] = 10000
                elif collisionResult == "bottom" :
                    bullet[0] = 10000
                    bullet[1] = 10000

        #Player -- End of Level
        if player[0] >= screen.get_width():
            if level >= 10:
                gamestate = "End Game"
                pygame.mixer.music.load('sounds/You Win.ogg')
                pygame.mixer.music.play(1)
            else:
                gamestate = "Mid Level"

        #Boss -- Walls
        if level == 7:
            for i in range(len(boss)):
                for j in range(len(walls)):
                    collisionResult = collideRectRectLocation (int(boss[i][0]),int(boss[i][1]),int(boss[i][2]),int(boss[i][3]),int(walls[j][0]),int(walls[j][1]),int(walls[j][2]),int(walls[j][3]))
                    if collisionResult != "none" :
                        if collisionResult == "left" :
                            boss[i][4] = random.randint(3,5)
                            boss[i][0] = walls[j][0] + walls[j][2]
                        elif collisionResult == "right" :
                            boss[i][4] = random.randint(-5,-3)
                            boss[i][0] = walls[j][0] - boss[i][2]
                        elif collisionResult == "top" :
                            boss[i][5] = random.randint(3,5)
                            boss[i][1] = walls[j][1] + walls[j][3]
                        elif collisionResult == "bottom" :
                            boss[i][5] = random.randint(-5,-3)
                            boss[i][1] = walls[j][1] - boss[i][3]
        #Boss -- Player
        if invincible == False:
            if level == 7:
                for i in range(len(boss)):
                    if collideRectRect(int(player[0]), int(player[1]), int(player[2]), int(player[3]), int(boss[i][0]), int(boss[i][1]), int(boss[i][2]), int(boss[i][3])) == True:
                        livesLeft = livesLeft - 1
                        player[0] = 5
                        player[1] = 20
                        if livesLeft <= 0:
                            gamestate = "End Game"
                            pygame.mixer.music.load('sounds/Death Sound.ogg')
                            pygame.mixer.music.play(1)
                            
        #Boss -- Starting Door
        if level == 7:
            for i in range(len(boss)):
                collisionResult = collideRectRectLocation (int(boss[i][0]),int(boss[i][1]),int(boss[i][2]),int(boss[i][3]),int(startDoor[0]),int(startDoor[1]),int(startDoor[2]),int(startDoor[3]))
                if collisionResult != "none" :
                    if collisionResult == "left" :
                        boss[i][4] = random.randint(3,5)
                        boss[i][0] = startDoor[0] + startDoor[2]
                    elif collisionResult == "right" :
                        boss[i][4] = random.randint(-5,-3)
                        boss[i][0] = startDoor[0] - boss[i][2]
                    elif collisionResult == "top" :
                        boss[i][5] = random.randint(3,5)
                        boss[i][1] = startDoor[1] + startDoor[3]
                    elif collisionResult == "bottom" :
                        boss[i][5] = random.randint(-5,-3)
                        boss[i][1] = startDoor[1] - boss[i][3]
        #Boss -- Ending Door
        if level == 7:
            for i in range(len(boss)):
                collisionResult = collideRectRectLocation (int(boss[i][0]),int(boss[i][1]),int(boss[i][2]),int(boss[i][3]),int(endDoor[0]),int(endDoor[1]),int(endDoor[2]),int(endDoor[3]))
                if collisionResult != "none" :
                    if collisionResult == "left" :
                        boss[i][4] = random.randint(3,5)
                        boss[i][0] = endDoor[0] + endDoor[2]
                    elif collisionResult == "right" :
                        boss[i][4] = random.randint(-5,-3)
                        boss[i][0] = endDoor[0] - boss[i][2]
                    elif collisionResult == "top" :
                        boss[i][5] = random.randint(5,5)
                        boss[i][1] = endDoor[1] + endDoor[3]
                    elif collisionResult == "bottom" :
                        boss[i][5] = random.randint(-5,-3)
                        boss[i][1] = endDoor[1] - boss[i][3]
        #Boss -- Bullet
        if level == 7:
            for i in range(len(boss)):
                if collideRectRect(int(bullet[0]), int(bullet[1]), int(bullet[2]), int(bullet[3]), int(boss[i][0]), int(boss[i][1]), int(boss[i][2]), int(boss[i][3])) == True:
                    bullet[0] = 10000
                    bullet[1] = 10000
                    bossHits[i] = bossHits[i] + 1
                    if bossHits[i] == 5:
                        boss[i][0] = 1000
                        boss[i][4] = 0
                        boss[i][5] = 0
                        killedBoss[i] = True
                        score = score + 1000

        #The Eye -- Bullet
        if level == 10 and theEye[4] != grey:
            for i in range(len(boss)):
                if collideRectRect(int(bullet[0]), int(bullet[1]), int(bullet[2]), int(bullet[3]), int(theEye[0]), int(theEye[1]), int(theEye[2]), int(theEye[3])) == True:
                    bullet[0] = 10000
                    bullet[1] = 10000
                    eyeHits = eyeHits + 1
                    if eyeHits == 100:
                        theEye[0] = 1000
                        eyeKilled = True
                        score = score + 5000
                        
        #The Eye -- Player
        if invincible == False:
            if level == 10:
                if collideRectRect(int(player[0]), int(player[1]), int(player[2]), int(player[3]), int(theEye[0]), int(theEye[1]), int(theEye[2]), int(theEye[3])) == True:
                    livesLeft = livesLeft - 1
                    player[0] = 5
                    player[1] = 20
                    if livesLeft <= 0:
                        gamestate = "End Game"
                        pygame.mixer.music.load('Death Sound.ogg')
                        pygame.mixer.music.play(1)


    # ============================== DRAW STUFF ============================ #  
    if gamestate == "Main Menu":
        screen.fill(black)
        score = 0
        textMenuTitle = fontMenuTitle.render('The Eye', True, white)
        screen.blit(textMenuTitle, [275, 100])
        textMenuPressStart = fontMenuPressStart.render('Press "SPACE" to play', True, white)
        screen.blit(textMenuPressStart, [240, 450])
        textMenuPressInstructions = fontMenuPressStart.render('Press "H" to learn how to play', True, white)
        screen.blit(textMenuPressInstructions, [185, 550])

    if gamestate == "How to Play":
        screen.fill(black)
        textInstructions1 = fontEndScore.render('HOW TO PLAY!', True, white)
        screen.blit(textInstructions1, [225, 50])
        textInstructions2 = fontGameTexts.render('Use the arrow keys to move your player', True, white)
        screen.blit(textInstructions2, [75, 150])
        pygame.draw.rect(screen, player[6], [50, (150 + player[3]/2) - 3, player[2], player[3]/2+3])
        pygame.draw.ellipse(screen, skin, [50, 150, player[2], player[3]/2])
        textInstructions3 = fontGameTexts.render('W, A, S, & D will fire UP, LEFT, DOWN, & RIGHT', True, white)
        screen.blit(textInstructions3, [75, 200])
        textInstructions5 = fontGameTexts.render('Kill the enemies to earn points and extra lives', True, white)
        screen.blit(textInstructions5, [75, 250])
        for i in range(1):
            pygame.draw.ellipse(screen, enemies[i][6], [40, 255, enemies[i][2], enemies[i][3]])
            pygame.draw.ellipse(screen, white, [40, 255 + enemies[i][3] / 3, enemies[i][2], enemies[i][3] / 3])
            pygame.draw.ellipse(screen, black, [40 + (enemies[i][2]/2)-5, 255 + (enemies[i][3]/2)-5, enemies[i][2]/3, enemies[i][3]/3])
        textInstructions6 = fontGameTexts.render('Collect powerups to become invincible:', True, white)
        screen.blit(textInstructions6, [75, 300])
        pygame.draw.ellipse(screen, white, [45 - 3,310 - 3,powerupInv[2] + 6,powerupInv[3] + 6])                
        pygame.draw.ellipse(screen, powerupInv[4], [45,310,powerupInv[2],powerupInv[3]])
        pygame.draw.ellipse(screen, white, [45 + 3,310 + 3,powerupInv[2] - 6,powerupInv[3] - 6])
        pygame.draw.rect(screen, white, [680, (300 + player[3]/2) - 3, player[2], player[3]/2+3])
        pygame.draw.ellipse(screen, skin, [680, 300, player[2], player[3]/2])
        textInstructions7 = fontGameTexts.render('Press "P" to pause the game at any time', True, white)
        screen.blit(textInstructions7, [75, 350])
        textInstructions8 = fontGameTexts.render('Press "Space" to return to the main menu', True, white)
        screen.blit(textInstructions8, [75, 500])
        textInstructions9 = fontSmallTexts.render('Press "G" or "B" to change genders when in the main menu', True, white)
        screen.blit(textInstructions9, [75, 550])

    if gamestate == "Pause":
        textPaused = fontEndScore.render('PAUSED', True, black)
        screen.blit(textPaused, [300, 50])
        textPausedPressStart = fontMenuPressStart.render('Press `SPACE` to continue', True, black)
        screen.blit(textPausedPressStart, [200, 450])

    if gamestate == "Play":
        screen.fill (ground)
        pygame.draw.rect(screen, red, [0, 600, screen.get_width(), 50])

        #DRAW COIN
        if level == 2 or level == 5 or level == 8:
            coinFlip = coinFlip + 1
            if coinFlip <= 50:
                pygame.draw.ellipse(screen, coin[4], [coin[0], coin[1], coin[2], coin[3]])
                pygame.draw.rect(screen, gold2, [coin[0] + coin[2] / 5 * 2, coin[1] + coin[3] / 5 * 1.25, coin[2] / 5, coin[3] / 2])
            else:
                pygame.draw.rect(screen, coin[4], [coin[0] + coin[2] / 3, coin[1], coin[2] / 3, coin[3]])
                if coinFlip >= 100:
                    coinFlip = 0
    
        #DRAW INVINCIBILITY POWERUP
        if level == 9:
            invGraphic = invGraphic + 1
            if invGraphic <= 50:
                pygame.draw.ellipse(screen, white, [powerupInv[0] - 2,powerupInv[1] - 2,powerupInv[2] + 4,powerupInv[3] + 4])                
                pygame.draw.ellipse(screen, powerupInv[4], [powerupInv[0],powerupInv[1],powerupInv[2],powerupInv[3]])
                pygame.draw.ellipse(screen, white, [powerupInv[0] + 2,powerupInv[1] + 2,powerupInv[2] - 4,powerupInv[3] - 4])
            else:
                pygame.draw.ellipse(screen, white, [powerupInv[0] - 3,powerupInv[1] - 3,powerupInv[2] + 6,powerupInv[3] + 6])                
                pygame.draw.ellipse(screen, powerupInv[4], [powerupInv[0],powerupInv[1],powerupInv[2],powerupInv[3]])
                pygame.draw.ellipse(screen, white, [powerupInv[0] + 3,powerupInv[1] + 3,powerupInv[2] - 6,powerupInv[3] - 6])
                if invGraphic >= 100:
                    invGraphic = 0

        #DRAW "THE EYE"
        if level == 10:
            if theEye[4] == blue:
                pygame.draw.ellipse(screen, theEye[4], [theEye[0], theEye[1], theEye[2], theEye[3]])
                pygame.draw.ellipse(screen, white, [theEye[0], theEye[1] + theEye[3] / 3, theEye[2], theEye[3] / 3])
                pygame.draw.ellipse(screen, black, [theEye[0] + (theEye[2]/2)-11, theEye[1] + (theEye[3]/2)-12, theEye[2]/3, theEye[3]/3])
            elif  theEye[4] == grey:
                pygame.draw.ellipse(screen, theEye[4], [theEye[0], theEye[1], theEye[2], theEye[3]])
                pygame.draw.ellipse(screen, black, [theEye[0], theEye[1] + theEye[3] / 10 * 5, theEye[2], theEye[3] / 5])
                pygame.draw.ellipse(screen, theEye[4], [theEye[0], theEye[1] + theEye[3] / 10 * 5 - 5, theEye[2], theEye[3] / 5])

        #DRAW KEY
        if level == 4:
            if hasKey == False :
                pygame.draw.ellipse(screen, keyDim[4], [keyDim[0], keyDim[1], keyDim[2], keyDim[3] / 2])
                pygame.draw.rect(screen, keyDim[4], [keyDim[0] + (keyDim[2] / 2.75), keyDim[1] + (keyDim[3] / 8), keyDim[2] / 4, keyDim[3]])
                pygame.draw.rect(screen, keyDim[4], [keyDim[0] + (keyDim[2] / 2.75), keyDim[1] + (keyDim[3] / 1.5), keyDim[2] / 2.75, keyDim[3] / 7])
                pygame.draw.rect(screen, keyDim[4], [keyDim[0] + (keyDim[2] / 2.75), keyDim[1] + (keyDim[3] / 1.1), keyDim[2] / 2, keyDim[3] / 7])        
                pygame.draw.ellipse(screen, ground, [keyDim[0] + (keyDim[2] / 4), keyDim[1] + (keyDim[3] / 6), keyDim[2] / 2, (keyDim[3] / 2) / 2])
            if hasKey == True:
                keyDim[0] = 760
                keyDim[1] = 610
                pygame.draw.ellipse(screen, keyDim[4], [keyDim[0], keyDim[1], keyDim[2], keyDim[3] / 2])
                pygame.draw.rect(screen, keyDim[4], [keyDim[0] + (keyDim[2] / 2.75), keyDim[1] + (keyDim[3] / 8), keyDim[2] / 4, keyDim[3]])
                pygame.draw.rect(screen, keyDim[4], [keyDim[0] + (keyDim[2] / 2.75), keyDim[1] + (keyDim[3] / 1.5), keyDim[2] / 2.75, keyDim[3] / 7])
                pygame.draw.rect(screen, keyDim[4], [keyDim[0] + (keyDim[2] / 2.75), keyDim[1] + (keyDim[3] / 1.1), keyDim[2] / 2, keyDim[3] / 7])        
                pygame.draw.ellipse(screen, red, [keyDim[0] + (keyDim[2] / 4), keyDim[1] + (keyDim[3] / 6), keyDim[2] / 2, (keyDim[3] / 2) / 2])            
        if level == 10:
            if eyeKilled == True:
                if hasKey == False :
                    pygame.draw.ellipse(screen, keyDim[4], [keyDim[0], keyDim[1], keyDim[2], keyDim[3] / 2])
                    pygame.draw.rect(screen, keyDim[4], [keyDim[0] + (keyDim[2] / 2.75), keyDim[1] + (keyDim[3] / 8), keyDim[2] / 4, keyDim[3]])
                    pygame.draw.rect(screen, keyDim[4], [keyDim[0] + (keyDim[2] / 2.75), keyDim[1] + (keyDim[3] / 1.5), keyDim[2] / 2.75, keyDim[3] / 7])
                    pygame.draw.rect(screen, keyDim[4], [keyDim[0] + (keyDim[2] / 2.75), keyDim[1] + (keyDim[3] / 1.1), keyDim[2] / 2, keyDim[3] / 7])        
                    pygame.draw.ellipse(screen, ground, [keyDim[0] + (keyDim[2] / 4), keyDim[1] + (keyDim[3] / 6), keyDim[2] / 2, (keyDim[3] / 2) / 2])
                if hasKey == True:
                    keyDim[0] = 760
                    keyDim[1] = 610
                    pygame.draw.ellipse(screen, keyDim[4], [keyDim[0], keyDim[1], keyDim[2], keyDim[3] / 2])
                    pygame.draw.rect(screen, keyDim[4], [keyDim[0] + (keyDim[2] / 2.75), keyDim[1] + (keyDim[3] / 8), keyDim[2] / 4, keyDim[3]])
                    pygame.draw.rect(screen, keyDim[4], [keyDim[0] + (keyDim[2] / 2.75), keyDim[1] + (keyDim[3] / 1.5), keyDim[2] / 2.75, keyDim[3] / 7])
                    pygame.draw.rect(screen, keyDim[4], [keyDim[0] + (keyDim[2] / 2.75), keyDim[1] + (keyDim[3] / 1.1), keyDim[2] / 2, keyDim[3] / 7])        
                    pygame.draw.ellipse(screen, red, [keyDim[0] + (keyDim[2] / 4), keyDim[1] + (keyDim[3] / 6), keyDim[2] / 2, (keyDim[3] / 2) / 2]) 
        #DRAW BOSS
        for i in range(len(boss)):
            if level == 7 and killedBoss[i] == False:
                pygame.draw.ellipse(screen, boss[i][6], [boss[i][0], boss[i][1], boss[i][2], boss[i][3]])
                pygame.draw.ellipse(screen, white, [boss[i][0], boss[i][1] + boss[i][3] / 3, boss[i][2], boss[i][3] / 3])
                pygame.draw.ellipse(screen, black, [boss[i][0] + (boss[i][2]/2)-7, boss[i][1] + (boss[i][3]/2)-8, boss[i][2]/3, boss[i][3]/3])

        #DRAW BULLET
        pygame.draw.rect(screen, bullet[6], [bullet[0], bullet[1], bullet[2], bullet[3]])

        #DRAW PLAYER
        pygame.draw.rect(screen, player[6], [player[0], (player[1] + player[3]/2) - 3, player[2], player[3]/2+3])
        pygame.draw.ellipse(screen, skin, [player[0], player[1], player[2], player[3]/2])

        #DISPLAY TIMER -- DISPLAY SCORE -- DISPLAY LIVES
        if len(str(timeSeconds)) == 2 and len(str(time)) == 2:
            textGameTimer = fontGameTexts.render(str(timeMinutes) + ":" + str(timeSeconds) + ":" + str(time), True, black)
            screen.blit(textGameTimer, [10, 610])
        elif len(str(timeSeconds)) == 1 and len(str(time)) == 2:
            textGameTimer = fontGameTexts.render(str(timeMinutes) + ":0" + str(timeSeconds) + ":" + str(time), True, black)
            screen.blit(textGameTimer, [10, 610])
        elif len(str(timeSeconds)) == 2 and len(str(time)) == 1:
            textGameTimer = fontGameTexts.render(str(timeMinutes) + ":" + str(timeSeconds) + ":0" + str(time), True, black)
            screen.blit(textGameTimer, [10, 610])
        elif len(str(timeSeconds)) == 1 and len(str(time)) == 1:
            textGameTimer = fontGameTexts.render(str(timeMinutes) + ":0" + str(timeSeconds) + ":0" + str(time), True, black)
            screen.blit(textGameTimer, [10, 610])

        textGameScoreNum = fontGameTexts.render('Score: ' + str(score), True, black)
        screen.blit(textGameScoreNum, [130, 610])
        textLivesLeft = fontGameTexts.render('Lives: ' + str(livesLeft), True, black)
        screen.blit(textLivesLeft, [485, 610])
        textLevel = fontGameTexts.render('Level: ' + str(level), True, black)
        screen.blit(textLevel, [625, 610])
        
        #DRAW ENEMIES
        for i in range(numEnemies):
            pygame.draw.ellipse(screen, enemies[i][6], [enemies[i][0], enemies[i][1], enemies[i][2], enemies[i][3]])
            pygame.draw.ellipse(screen, white, [enemies[i][0], enemies[i][1] + enemies[i][3] / 3, enemies[i][2], enemies[i][3] / 3])
            pygame.draw.ellipse(screen, black, [enemies[i][0] + (enemies[i][2]/2)-5, enemies[i][1] + (enemies[i][3]/2)-5, enemies[i][2]/3, enemies[i][3]/3])

        #DRAW WALLS
        for i in range(len(walls)):
            pygame.draw.rect(screen, walls[i][4], [walls[i][0], walls[i][1], walls[i][2], walls[i][3]])

        #DRAW SAFE ZONE DOORS
        pygame.draw.rect(screen, startDoor[4], [startDoor[0], startDoor[1], startDoor[2], startDoor[3]])
        pygame.draw.rect(screen, endDoor[4], [endDoor[0], endDoor[1], endDoor[2], endDoor[3]])

    if gamestate == "Mid Level":
        screen.fill(black)
        textLevelCut = fontMenuTitle.render('Level ' + str(level + 1), True, white)
        screen.blit(textLevelCut, [275, 100])
        textContinue = fontMenuPressStart.render('Press `SPACE` to continue', True, white)
        screen.blit(textContinue, [200, 450])
        
    if gamestate == "End Game":
        score = score + (timeSeconds * 10 + (timeMinutes * 600))
        score = score + (livesLeft * 500)
        livesLeft = 0
        time = 0
        timeMinutes = 0
        timeSeconds = 0
        screen.fill (black)

        textGameOver = fontMenuTitle.render('GAME OVER', True, white)
        screen.blit(textGameOver, [200, 50])

        textEndReturnMenu = fontEndReturnMenu.render('Press `SPACE` to return to the menu', True, white)
        screen.blit(textEndReturnMenu, [150, 550])

        textEndScore = fontEndScore.render('Score:  ' + str(score), True, white)
        screen.blit(textEndScore, [225, 250])
        textEndHighScore = fontEndScore.render('High Score:  ' + str(highScore), True, white)
        screen.blit(textEndHighScore, [100, 300])

        if score > highScore:
            highScore = score
            textHighScore = fontEndScore.render('NEW HIGH SCORE', True, red)
            screen.blit(textHighScore, [200, 400])
        
    # ===================== PYGAME STUFF (NO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(10)
pygame.quit ()
