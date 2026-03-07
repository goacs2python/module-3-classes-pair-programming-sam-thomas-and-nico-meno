from email.mime import text
import random
import pgzrun
import time
import math

mouseX = 0
mouseY = 0
bulletX = mouseX
bulletY = mouseY
firing = False
yVel = 5
WIDTH = 1000
HEIGHT = 800
bullets = []
targets = []
timer = 600
def update():
    for bullet in bullets:
        global bulletX, bulletY, firing, yVel

    if firing == False:

        bulletX = mouseX + 10

        bulletY = mouseY - 10

    else:

        bulletX += 10

        bulletY -= yVel

        yVel -= .2

        

    if bulletX >= 1020 or bulletY >= 820:

        firing = False

        bulletX = mouseX + 10

        bulletY = mouseY - 10

        yVel = 5

class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.yVel = 5
        self.firing = False

 
def draw():
    screen.clear()
    for bullet in bullets:
        screen.draw.filled_circle((bulletX, bulletY), 10, "white")
    screen.draw.filled_circle((mouseX,mouseY),20,"green")
    screen.draw.text(str(timer), (10, 10), color="white", fontsize=30)
    for target in targets:
        screen.draw.filled_circle((target.x, target.y), 20, "red")
    if math.sqrt((bulletX - mouseX) ** 2 + (bulletY - mouseY) ** 2) < 30:
        targets.remove(target)
        bullets.remove(bullet)
def bullet_radius():
    return 10
def target_radius():
    return 20
def countdown():
    global timer
    if timer > 0:
        timer -= 1
    elif timer <= 0:
        print("Game Over")
        exit()

def spawn_target():
    x = random.randint(100, 900)
    y = random.randint(100, 700)
    target = Target(x, y)
    targets.append(target)

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
if distance < target_radius + bullet_radius:
   
        
def on_mouse_down(button):
       global firing, bulletX, bulletY, yVel, xVel
       if button == mouse.LEFT:
        firing = True 
        bulletX = mouseX + 10
        bulletY = mouseY - 10
        xVel = 10
        yVel = 5
        bullets.append(Bullet(bulletX, bulletY))

        
def on_mouse_move(pos):
  global mouseX, mouseY
  mouseX, mouseY = pos

spawn_target()
pgzrun.go()