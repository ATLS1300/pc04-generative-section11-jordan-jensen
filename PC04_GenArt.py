"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: YOUR NAME HERE

********* HEY, READ THIS FIRST **********

When I started coming up with this code I was wat ching That 70s Show. 
I decided to make my art based off of the flower designs they always show.
All of the flowers colors are random.

"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
turtle.Screen().bgcolor("white")
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================

colors = ["darkorchid2", "orange1", "magenta", "springgreen", "lightslateblue"]

unoturtle = turtle.Turtle()
unoturtle.up()
dosturtle = turtle.Turtle()
dosturtle.up()
unoturtle.speed(0)
dosturtle.speed(0)

unoturtle.goto(80,90)
unoturtle.color(random.choice(colors))
unoturtle.down()
unoturtle.width(2)

for i in range (45):
    unoturtle.circle(25)
    unoturtle.forward(3)
    unoturtle.right(8)
    
dosturtle.goto(-100,-100)
dosturtle.color(random.choice(colors))
dosturtle.down()
dosturtle.width(4)

for i in range(18):
    dosturtle.circle(50)
    dosturtle.forward(8)
    dosturtle.right(20)
    
dosturtle.up()
unoturtle.up()

unoturtle.goto(-200,130)
unoturtle.color(random.choice(colors))
unoturtle.down()
unoturtle.width(3)

for i in range (36):
    unoturtle.circle(34)
    unoturtle.forward(5)
    unoturtle.right(10)
    
dosturtle.goto(200,-100)
dosturtle.color(random.choice(colors))
dosturtle.down()
dosturtle.width(1)

for i in range (45):
    dosturtle.circle(40)
    dosturtle.forward(1)
    dosturtle.right(8)
    

    
    unoturtle.up()

unoturtle.goto(-100,300)
unoturtle.color(random.choice(colors))
unoturtle.down()
unoturtle.width(3)

for i in range (18):
    unoturtle.circle(25)
    unoturtle.forward(5)
    unoturtle.right(20)
    
dosturtle.up()
dosturtle.goto(270,-270)
dosturtle.color(random.choice(colors))
dosturtle.down()
dosturtle.width(1)

for i in range (18):
    dosturtle.circle(10)
    dosturtle.forward(1)
    dosturtle.right(20)
    
dosturtle.up()
dosturtle.goto(200,270)
dosturtle.color(random.choice(colors))
dosturtle.down()
dosturtle.width(6)

for i in range(18):
    dosturtle.circle(50)
    dosturtle.forward(8)
    dosturtle.right(20)
    
unoturtle.up()

unoturtle.goto(-300,-250)
unoturtle.color(random.choice(colors))
unoturtle.down()
unoturtle.width(2)

for i in range (45):
    unoturtle.circle(25)
    unoturtle.forward(3)
    unoturtle.right(8)



    

# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
# turtle.done()
