import pygame
Infinite = "Infinite"
pygame.init()
jumped = False
acceleration = 6
altitude = 240
negative_gravity = 3
Screen_Dimensions = pygame.display.set_mode((1920 , 1080))
skye = pygame.image.load("sky.webp")
tileset = pygame.image.load("tileset.png")
tree = pygame.image.load("Tree.png")
mars = pygame.image.load("mars.png")
spritesheet = pygame.image.load("spritesheet.png")
Scaled_SpriteSheet = pygame.transform.scale(spritesheet, (900,900))
Current_Frame = 0

surface_image2 = tileset.get_rect()
surface_image = skye.get_rect()
DEFAULT_IMAGE_SIZE = (552, 222)
Scaled_Tileset = pygame.transform.scale(tileset, DEFAULT_IMAGE_SIZE)
#spritesprite = pygame.image.load("sprite.png")
#sprite = spritesprite.get_rect()
#print (sprite)
#Normal_Sprite = pygame.transform.scale(spritesprite, (150, altitude))
Scaled_Tree = pygame.transform.scale (tree, (200, 250))


# TileX, TileY, cropX, cropY, cropWidth, cropHeight
Cropped_griddle = [1000, 541, 30, 0, 50, 45]
sum = 1000
Cropped_Dirtle = [200, 582, 20, 150, 100, 349]

Run_Sprite = [200, 100, 36, 510, 100, 75]

Crouch_Frame = [220, 585, 57, 75]




Frames = []
a = 36
b = 100
for i in range(7):
    Run_Frames = [a, 510, 57, 75]
    a += 60
    #b += 85
    Frames.append(Run_Frames)






#57 is the gap between each sprite frame




def moving(x, y):
    global acceleration, jumped, Scaled_Sprite, Normal_Sprite, altitude
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        x -= 56
        Screen_Dimensions.blit(Scaled_SpriteSheet, (x, y),
        (Frames[Current_Frame][0], Frames[Current_Frame][1], Frames[Current_Frame][2],Frames[Current_Frame][3]))
        return x, y
    if key[pygame.K_d]:
        x += 59
        Screen_Dimensions.blit(Scaled_SpriteSheet, (x, y),
        (Frames[Current_Frame][0], Frames[Current_Frame][1], Frames[Current_Frame][2],Frames[Current_Frame][3]))
        return x, y
        # Jump
    if key[pygame.K_w]:

        if jumped == False:
            jumped = True
        if jumped == True:
            # Finished w jump
            if y == 420 and acceleration < 0:
                jumped = False
                acceleration = 6
                return x, y

            elif y < 421:
                y = y - acceleration * 6
                acceleration -= 1
                print(y)
                print(jumped)
                return x, y
            else:
                return x, y


    # Crouch
    if key[pygame.K_s]:
        if altitude == 240:
            altitude = altitude - 70
            #Normal_Sprite = pygame.transform.scale(spritesprite, (150, altitude))
        if y > 510:
            return x, y
        else:
            return x, y+70
    #Standing still
    else:
        if jumped == True:
            # Finished w jump
            if y == 510 and acceleration < 0:
                jumped = False
                acceleration = 6
                return x, y

            elif y < 511:
                y = y - acceleration * 5
                acceleration -= 1
                print(y)
                print(jumped)
                return x, y
        if altitude == 170:
            altitude = altitude + 70
            #Normal_Sprite = pygame.transform.scale(spritesprite, (150, altitude))
            return x, y-70
        else:
            Screen_Dimensions.blit(Scaled_SpriteSheet, (x, y),
                (Crouch_Frame[0], Crouch_Frame[1], Crouch_Frame[2], Crouch_Frame[3]))
            return x, y
x = 850
y = 510
angle = 0
while True:

    sum1 = 0
    sum2 = 0
    rotating_mars = pygame.transform.rotate(mars, angle)
    angle += 0.05
    coordinate = (400,100)

    #mars.get_rect(topleft=coordinate).center)
    #new_rect = rotating_mars.get_rect.center


    #Screen_Dimensions.blit(rotated_image, new_rect)new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    #Screen_Dimensions.blit(rotating_mars, new_rect)
    if angle == 360:
        angle = 0

    print(angle)


    Screen_Dimensions.blit(skye, surface_image)

    Screen_Dimensions.blit(rotating_mars, (400, 100))
    Screen_Dimensions.blit(Scaled_SpriteSheet, (400, 200))

    if Current_Frame != 6:
        Current_Frame += 1
    else:
        Current_Frame = 0

    for i in range(80):
        Screen_Dimensions.blit(Scaled_Tileset, (sum1, Cropped_griddle[1]),
            (Cropped_griddle[2], Cropped_griddle[3], Cropped_griddle[4], Cropped_griddle[5]))
        Screen_Dimensions.blit(Scaled_Tileset, (sum2, Cropped_Dirtle[1]),
            (Cropped_Dirtle[2], Cropped_Dirtle[3], Cropped_Dirtle[4], Cropped_Dirtle[5]))
        sum1 += 50
        sum2 += 72
        Screen_Dimensions.blit(tileset, (0, 0))
    Screen_Dimensions.blit(Scaled_Tree, (400, 336))
    x, y = moving(x, y)
    Screen_Dimensions.blit(Scaled_SpriteSheet, (x, y),
    (Crouch_Frame[0], Crouch_Frame[1], Crouch_Frame[2],Crouch_Frame[3]))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
