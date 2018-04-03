import turtle
from tkinter import *

print("                nfc 15 100 builder V1.0\n")
print("répondez à ces questions S'il vous plaît :)\n")
in1=int(input("nombre des lampes dans votre maison : "))
in2=int(input("nombre des prises dans votre maison : "))
fox=int(input("nombre des circuit special : "))
saf=int(input("plaque de cuisson 1 ou 0 : "))
print("le shema d'appareillage et d'instalation est le suivant   ")

#turtle.hideturtle()
turtle.speed(0)
turtle.color("red")
turtle.forward(1000)
turtle.color("blue")
turtle.pu()
turtle.goto(20,-5)
turtle.pd()
turtle.forward(1000)
turtle.pu()
turtle.goto(0,0)
turtle.pd()

def eclairage():
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
def courant():
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
def hcourant():
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
 turtle.write("20")
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
def uhcourant():
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
    
  turtle.goto(y,-80)
  turtle.right(180)
  turtle.forward(pria)
  turtle.left(90)
  turtle.forward(5)
  turtle.dot(5, "black");
  turtle.pu()
  turtle.forward(14)
  turtle.pd()
  turtle.dot(5, "black");
  turtle.forward(5)
  turtle.left(90)
  turtle.forward(prib)  
a=0
e=0
e=e+(in1)//8
if ((in1)%8):
    e=e+1;
if in1<8 :
    e=1
p=0
p=p+(in2)//8
if ((in2)%8):
    p=p+1;
if in1<8 :
    p=1
for i in range(0,e):
  eclairage()
  turtle.pu()
  a=a+80
  turtle.goto(a,0)
  turtle.right(90)
  turtle.pd()
  
for i in range(0,p):
  courant()
  turtle.pu()
  a=a+80
  turtle.goto(a,0)
  turtle.right(90)
  turtle.pd()
  
for i in range(0,fox):
  hcourant()
  turtle.pu()
  a=a+80
  turtle.goto(a,0)
  turtle.right(90)
  turtle.pd()
for i in range(0,saf):
  uhcourant()
  turtle.pu()
  a=a+80
  turtle.goto(a,0)
  turtle.right(90)
  turtle.pd()

#------------lampslopp
for i in range (0,in1):
    if (i>=1):
        turtle.right(90)

    #if (i<=7):
    lam()
    c=c+23
    d=d+23
    x=turtle.xcor()
    if ((i+1==8)or(i+1==16)or(i+1==24)or(i+1==32)):
        k=k+80
        turtle.goto(k,-80)
        c=60
        d=80
    
y=x+56    
#-------------plugsloop        
for i in range (0,in2):
  
      
      
      pria=pria+30
      prib=prib+30
      prise()
      last=turtle.xcor()
      if ((i+1==8)or(i+1==16)or(i+1==24)or(i+1==32)):
       pria=prib=0
       y=y+80
      
    























