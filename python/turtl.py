import turtle
#turtle.speed(0)
turtle.color("red")
turtle.forward(200)
turtle.color("blue")
turtle.pu()
turtle.goto(20,-5)
turtle.pd()
turtle.forward(200)
turtle.pu()
turtle.goto(0,0)
turtle.pd()
  
def disj():
 turtle.color("black")
 turtle.pu()
 turtle.goto(0,0)
 turtle.pd()
 turtle.right(90)
 turtle.forward(20)
 turtle.right(90)
 turtle.forward(8)
 turtle.left(90)
 turtle.forward(30)
 turtle.left(90)
 turtle.pu()
 turtle.forward(10)
 turtle.write("16")
 turtle.right(180)
 turtle.forward(10)
 turtle.pd()
 turtle.left(90)
 turtle.forward(30)
 turtle.left(90)
 turtle.forward(40)
 turtle.left(90)
 turtle.forward(60)
 turtle.left(90)
 turtle.forward(32)
 turtle.right(180)
 turtle.forward(24)
 turtle.left(90)
 turtle.forward(15)
 turtle.pu()
 turtle.right(90)
 turtle.forward(40)
 turtle.left(90)
 turtle.forward(5)
 turtle.right(90)
 turtle.pd()
global c
global d  
c=60
d=80 
def lam():
  
  
  turtle.pu()
  turtle.goto(0,-80)
  turtle.pd()
  turtle.right(90)
  turtle.forward(20)
  turtle.right(90)
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(c)
  turtle.left(90)
  turtle.forward(20)
  x=turtle.xcor()
  y=turtle.ycor()
  turtle.left(90)
  turtle.pu()
  turtle.forward(5)
  turtle.pd()
  turtle.goto(x+15,y)
  turtle.right(90)
  turtle.forward(10)
  turtle.right(90)
  turtle.pu()
  turtle.forward(10)
  turtle.left(90)
  turtle.forward(10)
  turtle.pd()
  turtle.circle(10, 360)
  turtle.pu()
  turtle.forward(10)
  turtle.left(90)
  turtle.forward(10)
  turtle.right(90)
  turtle.pd()
  turtle.forward(9)
  turtle.left(90)
  turtle.forward(d)
  
def pr():
    x=2

def dis():
 turtle.color("black")
 
 turtle.right(90)
 turtle.forward(20)
 turtle.right(90)
 turtle.forward(8)
 turtle.left(90)
 turtle.forward(30)
 turtle.left(90)
 turtle.pu()
 turtle.forward(10)
 turtle.write("16")
 turtle.right(180)
 turtle.forward(10)
 turtle.pd()
 turtle.left(90)
 turtle.forward(30)
 turtle.left(90)
 turtle.forward(40)
 turtle.left(90)
 turtle.forward(60)
 turtle.left(90)
 turtle.forward(32)
 turtle.right(180)
 turtle.forward(24)
 turtle.left(90)
 turtle.forward(15)
def disp():
 turtle.color("black")
 
 turtle.right(90)
 turtle.forward(20)
 turtle.right(90)
 turtle.forward(8)
 turtle.left(90)
 turtle.forward(30)
 turtle.left(90)
 turtle.pu()
 turtle.forward(10)
 turtle.write("10")
 turtle.right(180)
 turtle.forward(10)
 turtle.pd()
 turtle.left(90)
 turtle.forward(30)
 turtle.left(90)
 turtle.forward(40)
 turtle.left(90)
 turtle.forward(60)
 turtle.left(90)
 turtle.forward(32)
 turtle.right(180)
 turtle.forward(24)
 turtle.left(90)
 turtle.forward(15)

def disth():
 turtle.color("black")
 turtle.right(90)
 turtle.forward(20)
 turtle.right(90)
 turtle.forward(8)
 turtle.left(90)
 turtle.forward(30)
 turtle.left(90)
 turtle.pu()
 turtle.forward(10)
 turtle.write("32")
 turtle.right(180)
 turtle.forward(10)
 turtle.pd()
 turtle.left(90)
 turtle.forward(30)
 turtle.left(90)
 turtle.forward(40)
 turtle.left(90)
 turtle.forward(60)
 turtle.left(90)
 turtle.forward(32)
 turtle.right(180)
 turtle.forward(24)
 turtle.left(90)
 turtle.forward(15)

a=0 

    
   

for i in range(0,0):
  dis()
  turtle.pu()
  a=a+52
  turtle.goto(a,0)
  turtle.right(90)
  turtle.pd()

for i in range(0,2):
  disp()
  turtle.pu()
  a=a+52
  turtle.goto(a,0)
  turtle.right(90)
  turtle.pd()
for i in range(0,0):
  disth()
  turtle.pu()
  a=a+52
  turtle.goto(a,0)
  turtle.right(90)
  turtle.pd() 
for i in range (0,1):
    if (i>=1):
        turtle.right(90)
    lam()
    
    c=c+23
    d=d+23
    
    
turtle.goto(a,0)
