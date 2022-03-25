def main():
    import turtle
    import time
    import random
    
    hiz = 0.001

    pencere = turtle.Screen()
    pencere.title("kaçış Oyunu")
    pencere.bgcolor("black")
    pencere.setup(width=600, height=600)
    pencere.tracer(0)
    
    zaman1=time.time()
    puan=1
    yaz = turtle.Turtle()
    yaz.speed(0)
    yaz.shape("square")
    yaz.color("white")
    yaz.penup()
    yaz.hideturtle()
    yaz.goto(0, 260)
    yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "italic"))

    levelUpYazı = turtle.Turtle()
    levelUpYazı.speed(0)
    levelUpYazı.shape("square")
    levelUpYazı.color("green")
    levelUpYazı.penup()
    levelUpYazı.hideturtle()
    levelUpYazı.goto(0,220)
    

    kare = turtle.Turtle()
    kare.speed(0)
    kare.shape("square")
    kare.color("white")
    kare.penup()
    kare.goto(0, -100)
    kare.direction = "enine"
    p=0
    tuzak= []
    while p <14:
    
        tuzak.append(turtle.Turtle())
        tuzak[p].speed(1)
        tuzak[p].shape("circle")
        tuzak[p].color("red")
        tuzak[p].penup()
        x = random.randint(-300, 300)
        y = random.randint(50, 250)
        tuzak[p].goto(x,y)
        tuzak[p].shapesize(0.80, 0.80)
        tuzak[p].direction = "down"
        p=p+1
    hareketHızı = 1.2
    tuzakHızı = 1.5

    def move():

        if kare.direction == "right":
            x = kare.xcor()
            kare.setx(x + hareketHızı)
        if kare.direction == "left":
            x = kare.xcor()
            kare.setx(x - hareketHızı)

        for f in tuzak:
            if f.direction == "down":
                y= f.ycor()
                f.sety(y-tuzakHızı)


    def goRight():
        if kare.direction != "right":
            kare.direction = "right"

    def goLeft():
        if kare.direction != "left":
            kare.direction = "left"

    pencere.listen()
    pencere.onkey(goRight, "Right")
    pencere.onkey(goLeft, "Left")

    while True:
        pencere.update()
        zaman2=time.time()
        puan= zaman2-zaman1
        puan= int(puan)
        yaz.clear()
        yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "italic"))
        
        if(puan%15==0) and (puan>1):                  
            tuzakHızı= tuzakHızı+0.1
            hareketHızı = hareketHızı + 0.1
            print("tuzak hızı arttırıldı, yeni hız:" + str(tuzakHızı))
            print("hareket hızı arttırıldı, yeni hız:" + str(hareketHızı))
            levelUpYazı.write("LEVEL ARTTIRIYORUM", align="center", font=("Courier", 24, "italic"))
            time.sleep(1)
            levelUpYazı.clear()


        for p in tuzak:
            if kare.xcor() > 300:
                kare.goto(300, -100)
                kare.direction = "enine"
            if kare.xcor() < -300:
                kare.goto(-300,-100)
                kare.direction ="enine"

            if kare.distance(p) < 20:
                time.sleep(3)
                kare.goto(0, -100)
                kare.direction = "enine"
                zaman2= time.time()
                zaman1 = zaman2 
                tuzakHızı = 1.5
                
                
                for l in tuzak:
                    l.goto(0,150)
                    l.direction = "down"
                print("What a LOOSER!")
                
                
            if p.ycor() <-250:
                x = random.randint(-300, 300)
                y = random.randint(-0, 250)
                p.goto(x, y)
        
        """print(time.process_time) """      
        move()
        time.sleep(hiz)
main()    