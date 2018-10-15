#alexvanhoof
#9/17/18
#P4t1a-turtle graphics
import turtle

wn = turtle.Screen()        
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()       
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()       
for i in [0,1,2,3]:
    alex.forward(50)
    alex.left(90)
    
tess.forward(80)             
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)               

tess.right(180)              
tess.forward(80)             

wn.mainloop()
