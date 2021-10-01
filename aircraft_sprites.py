import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

FRAME_PER_SEC = 60

# timer
CREATE_ENEMY_EVENT = pygame.USEREVENT
# hero firing
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """Aircraft Sprite"""

    def __init__(self,image_name, speed=1):

        #father init
        super().__init__()

        #object property
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # vertical move
        self.rect.y += self.speed

class Background(GameSprite):
    """game background sprite"""
    def __init__(self, is_alt=False):

        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """enemy aircraft"""

    def __init__(self):

        # 1 create emeny sprite, and image
        super().__init__("./images/enemy1.png")
        # 2 speed
        self.speed = random.randint(2,5)
        # 3 rect
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        # 1 vertical flight
        super().update()
        # 2 if out of screen, delete the aircraft
        if self.rect.y >= SCREEN_RECT.height:
            # kill will delete the enemy from the sprites
            self.kill()

class Hero(GameSprite):
    """hero sprite"""

    def __init__(self):

        super().__init__("./images/me1.png",0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 50

        self.bullets = pygame.sprite.Group()


    def update(self):

        # move in x direction
        self.rect.x += self.speed

        # hero not move out of screen
        if self.rect.x <0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right


    def fire(self):
        #print("firing...")

        for i in (0,1,2):

            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            self.bullets.add(bullet)


class Bullet(GameSprite):

    def __init__(self):
        super().__init__("./images/bullet1.png", -3)


    def update(self):
        super().update()
        #print("bullet deleted...")
        if self.rect.bottom < 0:
            self.kill()

    #def __del__(self):
        #print("bullet deleted...")