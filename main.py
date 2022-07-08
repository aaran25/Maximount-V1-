import pygame
Infinite = ("Infinite")
pygame.init()
jumped = False
acceleration = 6
negative_gravity = 3
Screen_Dimensions = pygame.display.set_mode((1920,1080))
skye = pygame.image.load("sky.webp")
tileset = pygame.image.load("tileset.png")
surface_image2 = tileset.get_rect()
surface_image = skye.get_rect()
DEFAULT_IMAGE_SIZE = (552, 222)
Scaled_Tileset = pygame.transform.scale(tileset, DEFAULT_IMAGE_SIZE)
spritesprite = pygame.image.load("sprite.png")
sprite = spritesprite.get_rect()
print (sprite)
Scaled_Sprite = pygame.transform.scale(spritesprite, (150, 150))

# TileX, TileY, cropX, cropY, cropWidth, cropHeight
Cropped_griddle = [1000, 541, 30, 0, 50, 45]
sum = 1000
Cropped_Dirtle = [200, 582, 20, 150, 100, 349]
def moving(x, y):
    global acceleration, jumped, Scaled_Sprite
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        x -= 56
        return x, y
    if key[pygame.K_w]:
        #y -= 70

        if jumped == False:
            jumped = True
        if jumped == True:
            if y < 470 :
                y = y - acceleration * 6
                acceleration -= 1
                print(y)
                return x, y
            else:
                return x, y



    if key[pygame.K_s]:
        Scaled_Sprite = pygame.transform.scale(spritesprite, (150, 80))
        if y > 420:
            return x, y
        else:
            return x, y+70




    if key[pygame.K_d]:
        x += 59
        return x, y
    else:
        return x, y
x = 850
y = 420
while True:
    sum1 = 0
    sum2 = 0
    Screen_Dimensions.blit(skye, surface_image)
    for i in range(80):
        Screen_Dimensions.blit(Scaled_Tileset, (sum1, Cropped_griddle[1]),
            (Cropped_griddle[2], Cropped_griddle[3], Cropped_griddle[4], Cropped_griddle[5]))
        Screen_Dimensions.blit(Scaled_Tileset, (sum2, Cropped_Dirtle[1]),
            (Cropped_Dirtle[2], Cropped_Dirtle[3], Cropped_Dirtle[4], Cropped_Dirtle[5]))
        sum1 += 50
        sum2 += 72
        Screen_Dimensions.blit(tileset, (0, 0))
    x, y = moving(x, y)
    Screen_Dimensions.blit(Scaled_Sprite, (x, y))


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()





