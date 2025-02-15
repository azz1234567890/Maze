from pygame import *

class GameSprite(sprite.Sprite):
 def __init__(self, player_image, player_x, player_y, size_x, size_y):
     sprite.Sprite.__init__(self)
     self.image = transform.scale(image.load(player_image), (size_x, size_y))

     self.rect = self.image.get_rect()
     self.rect.x = player_x
     self.rect.y = player_y
 def reset(self):
     window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
 def __init__(self, player_image, player_x, player_y, size_x, size_y,x_speed,y_speed):
     GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)
     self.x_speed = x_speed
     self.y_speed = y_speed

 def update_pos(self):
    if 0 <= self.rect.x + self.x_speed <= 800:
            self.rect.x += self.x_speed
            
    platforms_touched = sprite.spritecollide(self, grup_tembok, False)
    if self.x_speed > 0:
            for platform in platforms_touched:
                self.rect.right = min(self.rect.right, platform.rect.left)
    elif self.x_speed < 0:
            for platform in platforms_touched:
                self.rect.left = max(self.rect.left, platform.rect.right)

    if 0 <= self.rect.y + self.y_speed <= 596:
        self.rect.y += self.y_speed

    platforms_touched = sprite.spritecollide(self, grup_tembok, False)
    if self.y_speed > 0:
            for platform in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, platform.rect.top)
    elif self.y_speed < 0:
            for platform in platforms_touched:
                self.rect.top = max(self.rect.top, platform.rect.bottom)
 
 def fire(self):
        bullet = Bullet('panah.png', self.rect.right, self.rect.centery, 50,50, 15)
        grup_bullet.add(bullet)
 
class Musuh(GameSprite):
    def __init__(self,player_image, player_x, player_y,size_x, size_y,x_awal,y_awal,x_akhir,y_akhir,speed,arah):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)
        self.x_awal = x_awal
        self.x_akhir = x_akhir
        self.y_awal = y_awal
        self.y_akhir = y_akhir
        self.speed = speed
        self.arah = arah
    def update_pos(self):
        if self.arah == 'h':
            self.rect.x += self.speed
            if self.rect.x < self.x_awal and self.speed < 0:
                self.speed  *= -1
            if self.rect.x > self.x_akhir and self.speed > 0 :
                self.speed = self.speed *-1
        if self.arah == 'v':
            self.rect.y += self.speed
            if self.rect.y < self.y_awal and self.speed < 0:
                self.speed  *= -1
            if self.rect.y > self.y_akhir and self.speed > 0 :
                self.speed = self.speed *-1

class Bullet(GameSprite):
    def __init__(self,player_image, player_x, player_y,size_x, size_y,speed):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 700 :
            self.kill()


display.set_caption("Game Labirin")
window = display.set_mode((900, 700))
back = (78, 156, 80)
font.init()
bg = image.load('view.jpeg')
font = font.SysFont('Calibri', 70)
tambah = font.render('+ 1 koin', True, (255,255,255))
koin = False


w1 = GameSprite('tembok4.jpg', 500, 0, 100, 350)
w2 = GameSprite('platform3.png', -10, 110, 400, 85)
w3 = GameSprite('platform3.png', 598, 300, 200, 85)
w4 = GameSprite('platform3.png', 150, 300, 350, 85)
w5 = GameSprite('tembok4.jpg', 160, 380, 100, 170)
w6 = GameSprite('platform3.png', 550, 500, 350, 85)
w7 = GameSprite('platform3.png', 260, 500, 150, 85)

packman = Player('archer.png', 0,0, 100, 100, 0, 0)

musuh = Musuh('hero.png', 200, 600,50,50, 200, 600, 470, 600, 3, 'h')
musuh2 = Musuh('musuh2.png', 800, 230,50,50, 800,230, 800,400, 4, 'v' )
musuh3 = Musuh('musuh2.png', 600, 600,50,50, 600,600, 700,630, 5, 'v' )

koin1 = GameSprite('koins.png', 600,460,40,40)
koin2 = GameSprite('koins.png', 250, 250,40,40)
koin3 = GameSprite('koins.png', 300,78,40,40)
koin4 = GameSprite('koins.png', 800,600,40,40)
koin5 = GameSprite('koins.png', 300,460,40,40)

winner = GameSprite('harta.png', 620,235,120,100)

grup_tembok = sprite.Group()
grup_tembok.add(w1)
grup_tembok.add(w2)
grup_tembok.add(w3)
grup_tembok.add(w4)
grup_tembok.add(w5)
grup_tembok.add(w6)
grup_tembok.add(w7)

grup_bullet = sprite.Group()

grup_koin = sprite.Group()
grup_koin.add(koin1)
grup_koin.add(koin2)
grup_koin.add(koin3)
grup_koin.add(koin4)
grup_koin.add(koin5)



grup_musuh = sprite.Group()
grup_musuh.add(musuh)
grup_musuh.add(musuh2)
grup_musuh.add(musuh3)


finish = False
run = True
while run == True:
 time.delay(40)
 for e in event.get():
      if e.type == QUIT:
          run = False
      elif e.type == KEYDOWN:
          if e.key == K_LEFT:
              packman.x_speed = -5
          elif e.key == K_RIGHT:
              packman.x_speed = 5
          elif e.key == K_UP:
              packman.y_speed = -5
          elif e.key == K_DOWN:
              packman.y_speed = 5
      elif e.type == KEYUP:
          if e.key == K_LEFT:
              packman.x_speed = 0
          elif e.key == K_RIGHT:
              packman.x_speed = 0
          elif e.key == K_UP:
              packman.y_speed = 0
          elif e.key == K_DOWN:
              packman.y_speed = 0
          elif e.key == K_SPACE:
              packman.fire()

 if finish != True:
    window.fill(back)
    window.blit(transform.scale(bg, (900,700)), (0, 0))
    packman.reset()
    packman.update_pos()
    musuh.update_pos()
    musuh2.update_pos()
    musuh3.update_pos()
    w1.reset()
    w2.reset()
    w3.reset()
    w4.reset()
    w5.reset()
    w6.reset()
    w7.reset()
    grup_tembok.draw(window)
    grup_bullet.draw(window)
    grup_musuh.draw(window)
    sprite.groupcollide(grup_bullet, grup_tembok, True, False)
    sprite.groupcollide(grup_bullet, grup_musuh, True, True)
    
    
    winner.reset()
    
    if sprite.collide_rect(packman, winner):
        finish = True
        img1 = image.load('menang.png')
        window.blit(transform.scale(img1, (600,600)), (150,80))
    for musuhh in grup_musuh:
        musuhh.reset()
        if sprite.collide_rect(packman, musuhh):
            finish = True
            img2 = image.load('kalahh.png')
            window.blit(transform.scale(img2, (700,700)),(104,-10))
            print('Kamu Kalah !')
            
    for kooin in grup_koin:
        kooin.reset()
        if sprite.collide_rect(packman, kooin):
            print('Koin Terkumpul!')
            koin = True
            grup_koin.remove(kooin)
            window.blit(tambah, (300,300))

 display.update()
