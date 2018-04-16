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
level1 = Image("mars.png" , game)
enemy = Image("Henemy.png",game)
shot = Image("bullet.png",game)
boss = Image("boss.png", game)




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
hero.moveTo(300,300)
hero2.moveTo(700,300)
select.moveTo(400,600)
while not game.over:
    game.processInput()
    bk.draw()
    hero2.draw()
    hero.draw()
    select.draw()

    if hero2.collidedWith(mouse) and mouse.LeftButton or hero.collidedWith(mouse) and mouse.LeftButton:
        game.over = True

    game.update(30)



podspassed = 0
ammocount = 0
hero2.resizeBy(-50)
game.over = False
hero2.moveTo(500,550)

while not game.over:
    game.processInput()
    bk.draw()


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
    


    hero2.draw()

    if hero.health >= 200 or ammocount >= 50:
        game.over = True

    
        
     
    game.update(30)
game.over = False
c.resizeBy(100)
c.moveTo(200,400)
enemy.resizeBy(-40)
shot.resizeBy(-90)
shot.setSpeed(40,50)
enemy.health = 100
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    level1.draw()

    enemy.draw()
    enemy.moveTo(800,200)

    c.move()

    if keys.Pressed[K_SPACE]:
        shot.visible = True 
        shot.draw()
        shot.moveTo(enemy.x,enemy.y)

    if shot.collidedWith(enemy) == True:
        shot.visible = False
        enemy.health -= 10

    if enemy.health == 0:
        game.over = True

    


    game.update(30)


game.over = False

while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    level1.draw()

    boss.draw()

    c.move()

    game.update(30)
    


    
    
