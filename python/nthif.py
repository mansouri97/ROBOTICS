import turtle

turtle.speed(0)
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

global c
global d
global k
k=0
c=60
d=80 

def lam():
  
  
  turtle.pu()
  turtle.goto(k,-80)
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
global pria
global prib
global y
pria=prib=0
y=0

def prise():
  t.pu()  
  t.goto(k,-80)
  t.pd()
  t.right(180)
  t.forward(pria)
  t.left(90)
  t.forward(5)
  t.dot(5, "black");
  t.pu()
  t.forward(14)
  t.pd()
  t.dot(5, "black");
  t.forward(5)
  t.left(90)
  t.forward(prib) 

a=0

for i in range(0,2):
  dis()
  turtle.pu()
  a=a+80
  turtle.goto(a,0)
  turtle.right(90)
  turtle.pd()
  


for i in range (0,9):
        
    if (i>=1):
        turtle.right(90)
    lam()
    c=c+23
    d=d+23 
    if ((i==7)or(i+1==16)or(i+1==24)or(i+1==32)):

        k=k+80
        print(k)
        turtle.goto(k,-80)
        c=60
        d=80



for i in range (0,3):
      pria=pria+30
      prib=prib+30
      prise()
      
      if ((i+1==8)or(i+1==16)or(i+1==24)or(i+1==32)):
       f=turtle.xcor()
       pria=prib=0
       f=f+56
          
   


turtle.goto(x+56,-80)
     
