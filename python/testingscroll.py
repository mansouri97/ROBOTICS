import turtle
from tkinter import *

print("             nfc 15 100 builder V1.0\n")
print("répondez à ces questions S'il vous plaît :)\n")
while True: 
 try:
    in1= int(input("nombre des lampes dans votre maison : "))
    
 except ValueError:
    print("donner un entier!")
    #continue
 else:
     break
while True:
 try:
    in2=int(input("nombre des prises dans votre maison : "))
    
 except ValueError:
    print("donner un entier!")
    #continue
 else:
     break
while True:
 try:
    fox=int(input("nombre des circuit special ex :\n(-lave linge\n -lave vaisselle\n -sèche linge\n -four indépendant\n -chaudière\n -volets roulants électriques\n -climatisation): "))
    
 except ValueError:
    print("donner un entier!")
    #continue
 else:
     break  

while True:
 try:
    saf=int(input("plaque de cuisson 1 ou 0 : "))
    
 except ValueError:
    print("donner un entier!")
    #continue
 else:
     break

print("le shema d'appareillage et d'instalation est le suivant   ")

root=Tk()
wid= root.winfo_screenwidth()
hei= root.winfo_screenheight()


root.geometry('800x800-5+40') #added by me

cv = turtle.ScrolledCanvas(root,width=wid,height=hei)
cv.pack()

screen = turtle.TurtleScreen(cv)
screen.screensize(4500,1500) #added by me


t = turtle.RawTurtle(screen)



t.speed(0)
t.color("red")
t.forward(700)
t.color("blue")
t.pu()
t.goto(20,-5)
t.pd()
t.forward(700)
t.pu()
t.goto(0,0)
t.pd()



def eclairage():
 t.color("black")
 
 t.right(90)
 t.forward(20)
 t.right(90)
 t.forward(8)
 t.left(90)
 t.forward(30)
 t.left(90)
 t.pu()
 t.forward(10)
 t.write("16A")
 t.right(180)
 t.forward(10)
 t.pd()
 t.left(90)
 t.forward(30)
 t.left(90)
 t.forward(40)
 t.left(90)
 t.forward(60)
 t.left(90)
 t.forward(32)
 t.right(180)
 t.forward(24)
 t.left(90)
 t.forward(15)

def courant():
 t.color("black")
 
 t.right(90)
 t.forward(20)
 t.right(90)
 t.forward(8)
 t.left(90)
 t.forward(30)
 t.left(90)
 t.pu()
 t.forward(10)
 t.write("20A")
 t.right(180)
 t.forward(10)
 t.pd()
 t.left(90)
 t.forward(30)
 t.left(90)
 t.forward(40)
 t.left(90)
 t.forward(60)
 t.left(90)
 t.forward(32)
 t.right(180)
 t.forward(24)
 t.left(90)
 t.forward(15)








def uhcourant():
 t.color("black")
 
 t.right(90)
 t.forward(20)
 t.right(90)
 t.forward(8)
 t.left(90)
 t.forward(30)
 t.left(90)
 t.pu()
 t.forward(10)
 t.write("32A")
 t.right(180)
 t.forward(10)
 t.pd()
 t.left(90)
 t.forward(30)
 t.left(90)
 t.forward(40)
 t.left(90)
 t.forward(60)
 t.left(90)
 t.forward(32)
 t.right(180)
 t.forward(24)
 t.left(90)
 t.forward(15)


global c
global d
global k
global f
f=0
k=0
c=60
d=80 



def lam():
  
  t.pu()
  t.goto(f,-80)
  t.pd()
  t.right(90)
  t.forward(20)
  t.right(90)
  t.forward(50)
  t.left(90)
  t.forward(c)
  t.left(90)
  t.forward(20)
  x=t.xcor()
  y=t.ycor()
  t.left(90)
  t.pu()
  t.forward(5)
  t.pd()
  t.goto(x+15,y)
  t.right(90)
  t.forward(10)
  t.right(90)
  t.pu()
  t.forward(10)
  t.left(90)
  t.forward(10)
  t.pd()
  t.circle(10, 360)
  t.pu()
  t.forward(10)
  t.left(90)
  t.forward(10)
  t.right(90)
  t.pd()
  t.forward(9)
  t.left(90)
  t.forward(d)



global pria
global prib
global y
pria=prib=0
y=0


def prise():
  t.pu()  
  t.goto(f,-80)
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
e=0
e=(in1)//8
if ((in1)%8):
    e=e+1;
if in1<8 :
    e=1
if in1==0:
    e=0
p=0
p=(in2)//8
if ((in2)%8):
    p=p+1;
if in2<8 :
    p=1
if in2==0:
    p=0


for i in range(0,e):
  eclairage()
  t.pu()
  a=a+80
  t.goto(a,0)
  t.right(90)
  t.pd()

for i in range(0,p):
  courant()
  t.pu()
  a=a+80
  t.goto(a,0)
  t.right(90)
  t.pd()

for i in range(0,fox):
  courant()
  t.pu()
  a=a+80
  t.goto(a,0)
  t.right(90)
  t.pd()

for i in range(0,saf):
  uhcourant()
  t.pu()
  a=a+80
  t.goto(a,0)
  t.right(90)
  t.pd()


for i in range (0,in1):
    if (i>=1):
        t.right(90)

    #if (i<=7):
    lam()
    c=c+23
    d=d+23
    
    if ((i==7)or(i+1==16)or(i+1==24)or(i+1==32)):
        f=t.xcor()
        f=f+56
        t.pu()
        t.goto(f,-80)
        t.pd()
        c=60
        d=80
    if i==in1-1:
        f=t.xcor()

if (in1==0):
        t.left(90)
if(in1!=0):
    f=f+56
if (in1==8):
    f=f-56
for i in range (0,in2):
      pria=pria+30
      prib=prib+30
      prise()
      
      if ((i+1==8)or(i+1==16)or(i+1==24)or(i+1==32)):
       f=t.xcor()
       pria=prib=0
       f=f+56
      if i==in2-1:
        f=t.xcor()
pria=prib=0
if(in2!=0):
    f=f+56
for i in range (0,fox):
    pria=pria+30
    prib=prib+30
    prise()
    f=t.xcor()
    f=f+56

    pria=prib=0



for i in range (0,saf):
    pria=pria+30
    prib=prib+30
    prise()
    f=t.xcor()
    f=f+56
    pria=prib=0
t.pu()
t.goto(0,110)
t.pd()
t.write( "                       NFC BUILDER V1.0[connaître votre appareillage]\n-votre installation électrique a besoin au moins de :\n - "+str(e)+" disjoncteurs16A (eclairage),section des fil est de 1.5mm²\n - "+str(p+fox)+" disjoncteurs20A (prise et circuit speciales),section des fil est de 2.5mm²\n - "+str(saf)+" disjoncteurs32A (p de cuisson),section des fil est de 6mm²\n- ce n'est pas montré dans le schéma mais un disjoncteur principal et 2 disjoncteurs différentiels sont nécessaire pour assurer une bonne selectivite et pour votre protection\n\n\n le schéma :", font=("Arial", 15, "normal"))
#NFC BUILDER V1.0\n-cette une schema de votre appareillage necessaire pour l'instalation tel que:\n *le nombre et calibre des disjoncteurs\n *les interupteurs \n *les prises de courant \n-NB q'il faut des ddf pour assurer votre protection contre les choc electrique qui ne sont pas afficher\n il faut un minimum 2 ddf pour assurer une bonne selectivite et aussi il faut ajouter un raccordement a la terre  
root.mainloop()

