from gamelib import *
game = Game(1000,700, "Game")
bk = Image("Bk.jpg",game)
hero = Image("Ship.png",game)
HTP = Image("HTP.png",game)
title = Image("Title.png",game)
play = Image("Play.png",game)
story = Image("Story.png",game)
hero2 = Image("Newship.png",game)
select = Image("Select.png",game)
health = Font("arial" ,red,40, None)
c = Animation("Hero.png",10, game , 502/10, 88)
enemy = Image("Henemy.png",game)
shot = Image("bullet.png",game)
level1 = Image("bk2.jpg",game)
tip = Image("text1.png",game)
begin = Image("begin.png",game)
white = Image("square.jpg",game)
hint = Image("Hint.png",game)
T1 = Image("1.png",game)
T2 = Image("2.png",game)
T3 = Image("3.png",game)
T4 = Image("4.png",game)
T5 = Image("5.png",game)
T6 = Image("6.png",game)
T7 = Image("7.png",game)
T8 = Image("8.png",game)
T9 = Image("9.png",game)
score = Image("numbers.png",game)
S2 = Image("2-2.png",game)
S3 = Image("3-2.png",game)
S4 = Image("4-2.png",game)
CH = Image("CH.png",game)
level2 = Image("level2.gif",game)
boss = Image("boss2.gif",game)



pods = []
for index in range(15):
    pods.append(Image("healthpack.png",game))

for index in range(15):
    x = randint(100,1000)
    y = randint(100,4000)
    pods[index].moveTo(x,-y)
    pods[index].setSpeed(6,180)
    pods[index].resizeBy(-95)

ammo = []
for index in range(15):
    ammo.append(Animation("ammo.png",16,game,512/4,512/4))
for index in range(15):
    x = randint(100,1000)
    y = randint(100,4000)
    ammo[index].moveTo(x,-y)
    ammo[index].setSpeed(6,180)
    ammo[index].resizeBy(-40)

c.stop()



            

game.setBackground(bk)

play.moveTo(300,400)
HTP.moveTo(600,600)
story.moveTo(700,400)
title.moveTo(500,200)

hero.resizeBy(-60)
while not game.over:
    game.processInput()
    bk.draw()
    play.draw()
    HTP.draw()
    story.draw()
    title.draw()
    hero.draw()

    if play.collidedWith(mouse) and mouse.LeftButton:
        hero.y -= 75

    if hero.isOffScreen("top"):
        game.over = True
        


    game.update(30)


game.over = False

   
hero2.resizeBy(-80)
hero2.moveTo(500,550)
ammocount = 0

while not game.over:
    game.processInput()
    bk.draw()

    hero2.draw()
    


    if keys.Pressed[K_d]:
        hero2.x += 10
    if keys.Pressed[K_a]:
        hero2.x -= 10

    for index in range(15):
        pods[index].move()
        if pods[index].collidedWith(hero2):
            pods[index].visible = False
            hero.health += 20
        
    for index in range(15):
        ammo[index].move()
        if ammo[index].collidedWith(hero2):
            ammo[index].visible = False
            ammocount += 10
    




    if hero.health >= 200 or ammocount >= 50:
        game.over = True

    
        
     
    game.update(30)
game.over = False

level1.resizeBy(100)
tip.resizeBy(-65)
begin.resizeBy(-30)
begin.moveTo(400,450)
while not game.over:
    game.processInput()
    level1.draw()
    tip.draw()
    begin.draw()

    if begin.collidedWith(mouse) and mouse.LeftButton:
        game.over = True
        
    game.update(30)
game.over = False


hint.moveTo(500,550)
hint.resizeBy(-60)
T1.moveTo(250,150)
T2.moveTo(500,150)
T3.moveTo(750,150)
T4.moveTo(250,300)
T5.moveTo(500,300)
T6.moveTo(750,300)
T7.moveTo(250,450)
T8.moveTo(500,450)
T9.moveTo(750,450)
score.moveTo(300,25)
score.resizeBy(-60)
while not game.over:
    game.processInput()
    level1.draw()
    white.draw()
    hint.draw()
    score.draw()
    T1.draw()
    T2.draw()
    T3.draw()
    T4.draw()
    T5.draw()
    T6.draw()
    T7.draw()
    T8.draw()
    T9.draw()

    if T3.collidedWith(mouse) and mouse.LeftButton:
        game.over = True

   


    game.update(30)
game.over = False

S3.moveTo(250,25)
while not game.over:
    game.processInput()
    level1.draw()
    white.draw()
    hint.draw()
    T1.draw()
    T2.draw()
    T3.draw()
    T4.draw()
    T5.draw()
    T6.draw()
    T7.draw()
    T8.draw()
    T9.draw()
    score.draw()
    S3.draw()

    if T2.collidedWith(mouse) and mouse.LeftButton:
        game.over = True

    
    game.update(30)
    
game.over = False
S2.draw()
S2.moveTo(550,25)
while not game.over:
    game.processInput()
    level1.draw()
    white.draw()
    hint.draw()
    T1.draw()
    T2.draw()
    T3.draw()
    T4.draw()
    T5.draw()
    T6.draw()
    T7.draw()
    T8.draw()
    T9.draw()
    score.draw()
    S2.draw()
    S3.draw()

    if T4.collidedWith(mouse) and mouse.LeftButton:
        game.over = True

   

    game.update(30)
game.over = False
S4.moveTo(750,25)
CH.moveTo(900,500)
CH.resizeBy(-70)
while not game.over:
    game.processInput()
    level1.draw()
    white.draw()
    hint.draw()
    T1.draw()
    T2.draw()
    T3.draw()
    T4.draw()
    T5.draw()
    T6.draw()
    T7.draw()
    T8.draw()
    T9.draw()
    score.draw()
    S2.draw()
    S3.draw()
    S4.draw()
    CH.draw()

    if CH.collidedWith(mouse) and mouse.LeftButton:
        game.over = True

    game.update(30)
game.over = False
level2.resizeBy(250)
c.resizeBy(60)
boss.moveTo(900,450)
c.moveTo(100,500)
shot.resizeBy(-95)
boss.health = 120
while not game.over:
    game.processInput()
    level2.draw()
    c.move()

    boss.move()

    

    if keys.Pressed[K_UP]:
        c.y -= 8
        
    if keys.Pressed[K_DOWN]:
        c.y += 8
        
    if keys.Pressed[K_RIGHT]:
        c.x += 8
        c.nextFrame()
        
    if keys.Pressed[K_LEFT]:
        c.x -= 8
        c.prevFrame()

    if mouse.LeftButton:
        x = randint(c.x,boss.x)
        y = randint(c.y,500)
        shot.setSpeed(15,20)
        shot.visible = True
        shot.moveTo(x,y)

    if shot.collidedWith(boss):
        boss.health -= 10
        shot.visible = False

    if boss.health <1:
        game.over = True

    

    game.update(30)
game.quit()
    










    
    
