import pygame
import random
import time
pygame.init()
black=(0,0,0)
green=(0,155,0)
red=(255,0,0)
white=(255,255,255)
blue=(0,0,200)
brown=(165,42,42)
pygame.display.set_caption("Snake Game")
width=500
height=500
intro = True
hit=pygame.mixer.Sound("hit.wav")
music=pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((width, height))
c = pygame.time.Clock()
icon=pygame.image.load("snake-icon.png")
pygame.display.set_icon(icon)
class Snake():
    def add(self,color,snakelist):
        for xny in snakelist:
            pygame.draw.rect(screen,color,[xny[0],xny[1],10,10])

class Bomb():
    def add(self,x,y):
        z=x+3
        w=y-4
        self.x=x
        self.y=y
        pygame.draw.rect(screen,black,[x,y,10,10])
        pygame.draw.rect(screen,brown,[z,w,2,4])
        pygame.draw.rect(screen,red,[z,w-4,3,3])
class apple():
    def add(self,x,y):
        z=x+3
        w=y-4
        self.x=x
        self.y=y
        pygame.draw.rect(screen,red,[x,y,10,10])
        pygame.draw.rect(screen,brown,[z,w,2,4])
        pygame.draw.rect(screen,green,[z+3,w-1,3,3])


def message_to_screen(msg,color,size,x,y):
    font=pygame.font.SysFont(None,size)
    screen_text=font.render(msg,True,color)
    screen.blit(screen_text,[x,y])
def pauseGame():
    gameisPaused = True
    while gameisPaused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameisPaused = False
                    
                elif event.key == pygame.K_q:
                    pygame.quit()

        screen.fill(white)
        message_to_screen("Paused",
                          black,20,100,100
                          )
        message_to_screen("Press ESC to continue or Q to quit.",
                          black,20,100,200
                          )
        pygame.display.update()
def gameIntro(intro): 
    while intro: 
        for eachEvent in pygame.event.get():
            if eachEvent.type == pygame.QUIT:
                intro=False
            if eachEvent.type == pygame.KEYDOWN:
                if eachEvent.key == pygame.K_a:
                    mainLevel1()
                if eachEvent.key == pygame.K_b:
                    mainLevel2()
                if eachEvent.key == pygame.K_q:
                    intro=False

       
        screen.fill(white)
        message_to_screen("Welcome to Snack Game",green,30,50,10)
        message_to_screen("The more apples you eat, the longer you are",red,15,50,70)
        message_to_screen("The objective of the game is to eat red apples",red,15,50,100)
        message_to_screen("If you run into yourself, or the edges, you die!",red,15, 50,130)
        message_to_screen("Press a to play level1 ",black,25,50,200)
        message_to_screen("press b to play level2 ",black,25,50,250)
        message_to_screen("press Q to quit.",black,25,50,300)
        message_to_screen("you can press esc to pause game *-*",black,25,50,350)
        message_to_screen("GOOD LUCK *-*",green,15,200,400)
        

        pygame.display.update()
        c.tick(500)

def game1():
    into=True
    z=0
    while into:
        z+=1
        for eachEvent in pygame.event.get():
            if eachEvent.type == pygame.QUIT:
                into=False
        screen.fill(white)
        message_to_screen("press up,down,left or right to move!!!",black,25,50,250)
        pygame.display.update()
        c.tick(500)
        if z==500:
            into=False
def game2():
    into=True
    z=0
    while into:
        z+=1
        for eachEvent in pygame.event.get():
            if eachEvent.type == pygame.QUIT:
                into=False
        screen.fill(white)
        message_to_screen("Player A(green) press up,down,left or right to move!!!",green,25,50,250)
        message_to_screen("Player B(blue) press w,s,a or d to move!!!",blue,25,50,300)
        pygame.display.update()
        c.tick(500)
        if z==500:
            into=False
        
    
def mainLevel1 ():
    game1()
    screen.fill(white)
    running=True
    gameOver=False
    score=0
    while running:
        b=apple()
        z=Bomb()
        snake=Snake()
        w=width-10
        h=height-10
        xa=round(random.randrange(3,w)/10)*10
        ya=round(random.randrange(50,h)/10)*10
        xb=round(random.randrange(3,w)/10)*10
        yb=round(random.randrange(50,h)/10)*10
        xs=round(random.randrange(3,w)/10)*10
        ys=round(random.randrange(40,h)/10)*10
        if xs==xb or xs==xa or xa==xb:
            if ys==ya or ya==yb or yb==ys:
                mainLevel1()
        screen.fill(white)
        snakelist=[]
        snakelength=1
        cb=0
        cv=0 
        snakehead=[]
        snakehead.append(xs)
        snakehead.append(ys)
        snakelist.append(snakehead)
        while not gameOver:
           
            cb+=2
            cv+=1
            pygame.draw.line(screen,black,(0,40),(width,40))
            b.add(xa,ya)
            z.add(xb,yb)
            snake.add(green,snakelist)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameOver=True
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP and ys>=40:
                        ys-=10
                        snakebody=[]
                        snakebody.append(xs)
                        snakebody.append(ys)
                        snakelist.append(snakebody)
                    elif event.key==pygame.K_DOWN and ys<=height-20:
                        ys+=10
                        snakebody=[]
                        snakebody.append(xs)
                        snakebody.append(ys)
                        snakelist.append(snakebody)
                    if event.key==pygame.K_LEFT and xs>=10:
                        xs-=10
                        snakebody=[]
                        snakebody.append(xs)
                        snakebody.append(ys)
                        snakelist.append(snakebody)
                    elif event.key==pygame.K_RIGHT and xs<=width-20:
                        xs+=10
                        snakebody=[]
                        snakebody.append(xs)
                        snakebody.append(ys)
                        snakelist.append(snakebody)
                    elif event.key==pygame.K_ESCAPE:
                        pauseGame()
            if xs==xa and ys==ya:
                hit.play()
                score+=1
                snakelength+=1
                time.sleep(0.1)
                xa=round(random.randrange(3,w)/10)*10
                ya=round(random.randrange(50,h)/10)*10
                
                b.add(xa,ya)
            if xs==xb and ys==yb:
                hit.play()
                score-=1
                snakelength-=1
                time.sleep(0.1)
                xb=round(random.randrange(3,w)/10)*10
                yb=round(random.randrange(50,h)/10)*10
                
                z.add(xb,yb)
            if cb==300:
                xb=round(random.randrange(3,w)/10)*10
                yb=round(random.randrange(50,h)/10)*10
                z.add(xb,yb)
                cb=0
            if cv==200:
                xa=round(random.randrange(3,w)/10)*10
                ya=round(random.randrange(50,h)/10)*10
                b.add(xa,ya)
                cv=0 
            if len(snakelist)>snakelength:
                del snakelist[0]
            p=len(snakelist)-1
            for e in snakelist[:-1]: 
                if e== snakelist[p]:
                    gameOver = True
            if score<0:
                gameOver=True
            if score>3:
                gameOver=True
                running=False
                mainLevel2()
           
            message_to_screen("Score:"+str(score),black,20,10,10)
            c.tick(30)
            pygame.display.update()
            screen.fill(white)

            
        
        if running==True and gameOver==True:
            message_to_screen("Game Over",red,40,150,200)
            message_to_screen("Do you want to play again?",blue,25,150,250)
            message_to_screen("press P to play again or Q to quit",blue,25,150,300)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        running=False
                    if event.key==pygame.K_p:
                        intro=True
                        gameIntro(intro)
            time.sleep(3)
        c.tick(30)
        
def mainLevel2():
    game2()
    running=True
    gameOver=False
    scorea=0
    scoreb=0
    while running:
        b=apple()
        z=Bomb()
        snakea=Snake()
        snakeb=Snake()
        w=width-10
        h=height-10
        xa=round(random.randrange(3,w)/10)*10
        ya=round(random.randrange(50,h)/10)*10
        xb=round(random.randrange(3,w)/10)*10
        yb=round(random.randrange(50,h)/10)*10
        xsa=round(random.randrange(3,w)/10)*10
        ysa=round(random.randrange(40,h)/10)*10
        xsb=round(random.randrange(3,w)/10)*10
        ysb=round(random.randrange(40,h)/10)*10
      
        screen.fill(white)
        snakelista=[]
        snakelistb=[]
        snakelengtha=1
        snakelengthb=1
        cb=0
        cv=0 
        snakeheada=[]
        snakeheada.append(xsa)
        snakeheada.append(ysa)
        snakelista.append(snakeheada)
        snakeheadb=[]
        snakeheadb.append(xsb)
        snakeheadb.append(ysb)
        snakelistb.append(snakeheadb)
    
        while not gameOver:
            cb+=2
            cv+=1
            pygame.draw.line(screen,black,(0,40),(width,40))
            b.add(xa,ya)
            z.add(xb,yb)
            snakea.add(green,snakelista)
            
            snakeb.add(blue,snakelistb)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameOver=True
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP and ysa>=40:
                        ysa-=10
                        snakebodya=[]
                        snakebodya.append(xsa)
                        snakebodya.append(ysa)
                        snakelista.append(snakebodya)
                    elif event.key==pygame.K_DOWN and ysa<=height-20:
                        ysa+=10
                        snakebodya=[]
                        snakebodya.append(xsa)
                        snakebodya.append(ysa)
                        snakelista.append(snakebodya)
                    if event.key==pygame.K_LEFT and xsa>=10:
                        xsa-=10
                        snakebodya=[]
                        snakebodya.append(xsa)
                        snakebodya.append(ysa)
                        snakelista.append(snakebodya)
                    elif event.key==pygame.K_RIGHT and xsa<=width-20:
                        xsa+=10
                        snakebodya=[]
                        snakebodya.append(xsa)
                        snakebodya.append(ysa)
                        snakelista.append(snakebodya)
                    elif event.key==pygame.K_w and ysb>=40:
                        ysb-=10
                        snakebodyb=[]
                        snakebodyb.append(xsb)
                        snakebodyb.append(ysb)
                        snakelistb.append(snakebodyb)
                    elif event.key==pygame.K_s and ysb<=height-20:
                        ysb+=10
                        snakebodyb=[]
                        snakebodyb.append(xsb)
                        snakebodyb.append(ysb)
                        snakelistb.append(snakebodyb)
                    if event.key==pygame.K_a and xsb>=10:
                        xsb-=10
                        snakebodyb=[]
                        snakebodyb.append(xsb)
                        snakebodyb.append(ysb)
                        snakelistb.append(snakebodyb)
                    elif event.key==pygame.K_d and xsb<=width-20:
                        xsb+=10
                        snakebodyb=[]
                        snakebodyb.append(xsb)
                        snakebodyb.append(ysb)
                        snakelistb.append(snakebodyb)
                    elif event.key==pygame.K_ESCAPE:
                        pauseGame()
            if xsa==xa and ysa==ya:
                hit.play()
                scorea+=1
                snakelengtha+=1
                time.sleep(0.1)
                xa=round(random.randrange(3,w)/10)*10
                ya=round(random.randrange(50,h)/10)*10
                
                b.add(xa,ya)
            if xsa==xb and ysa==yb:
                hit.play()
                scorea-=1
                snakelengtha-=1
                time.sleep(0.1)
                xb=round(random.randrange(3,w)/10)*10
                yb=round(random.randrange(50,h)/10)*10
            if xsb==xa and ysb==ya:
                hit.play()
                scoreb+=1
                snakelengthb+=1
                time.sleep(0.1)
                xa=round(random.randrange(3,w)/10)*10
                ya=round(random.randrange(50,h)/10)*10
                
                b.add(xa,ya)
            if xsb==xb and ysb==yb:
                hit.play()
                scoreb-=1
                snakelengthb-=1
                time.sleep(0.1)
                xb=round(random.randrange(3,w)/10)*10
                yb=round(random.randrange(50,h)/10)*10
            
                
                z.add(xb,yb)
            if cb==300:
                xb=round(random.randrange(3,w)/10)*10
                yb=round(random.randrange(50,h)/10)*10
                z.add(xb,yb)
                cb=0
            if cv==200:
                xa=round(random.randrange(3,w)/10)*10
                ya=round(random.randrange(50,h)/10)*10
                b.add(xa,ya)
                cv=0
    
    
            if scorea<0:
                message_to_screen("playerB is WINNER",red,20,200,250)
                s="A"
                s2="B"
                gameOver=True
                time.sleep(1)
            if len(snakelista)>snakelengtha:
                del snakelista[0]
            message_to_screen("Score A: "+str(scorea),black,20,420,10)
            
            if scoreb<0:
                s2="A"
                s="B"
                gameOver=True
                
            if len(snakelistb)>snakelengthb:
                del snakelistb[0]
            pa=len(snakelista)-1
            for ea in snakelista[:-1]: 
                if ea== snakelista[pa]:
                    gameOver = True
                    s2="B"
                    s="A"
            pb=len(snakelistb)-1
            for eb in snakelistb[:-1]: 
                if eb== snakelistb[pb]:
                    gameOver = True
                    s2="A"
                    s="B"
            for a in snakelista[:]:
                for bs in snakelistb[:]:
                    if a==bs:
                        gameOver=True
                        s2="No One"
                        s="A & B"
            message_to_screen("Score B: "+str(scoreb),black,20,10,10)
            c.tick(30)
            pygame.display.update()
            screen.fill(white)

        if running==True and gameOver==True:
            message_to_screen("player "+s2+" is WINNER",red,20,150,150)
            message_to_screen(s+" Game Over",red,30,150,200)
            message_to_screen("Do you want to play again?",blue,25,150,250)
            message_to_screen("press P to play again or Q to quit",blue,25,150,300)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameOver=True
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        running=False
                        intro=False
                    if event.key==pygame.K_p:
                        intro=True
                        gameIntro(intro)
        c.tick(30)
            
        

screen.fill(white)
gameIntro(intro)
screen.fill(white)
time.sleep(1)
message_to_screen("Bye ^_^",red,50,width//2-75,height//2-100)
pygame.display.update()
time.sleep(1)

pygame.quit()
        