"""
Created on Tue Sep 15 11:39:56 2020
PC04 multiturtle example
@author: YOURNAME HERE

This code draws two wiggling turtles that mirror each other's movements
There's a random value added to the vertical position, which makes the waves wiggly.
I chose a monochrome palette becuase it's cool!

**** BORROWING THIS CODE? READ FIRST ****
*                                       *
*   You MUST modify this code if you    *
*   borrow it!. That means you'll       *
*   change the pattern (wave freq,      *
*   position, color, thickness).        *
*   You must cite this example code!    *
*                                       *
*****************************************


"""

import turtle, math
import random

turtle.colormode(255)
turtle.tracer(0) # this turns off animation. You must update the panel manually when this function is called.

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# ============= YOUR CODE BELOW! =======================

# Make my palette list of hex strings (from coolors.co)
# Yes, turtle takes hex colors too!! :D
MONO = ["#0D5C63", "#247B7B", "#44A1A0", "#78CDD7", "#FFFFFA"] # dark to light
startX = -350 # where I want my turtles to start.

# Set panel background color
panel.bgcolor(MONO[0]) # I can use dot notation to access the bgcolor function for my variable panel

# Make first turtle and adjust settings
wiggleWave = turtle.Turtle()
wiggleWave.width(4) # use dot notation to access all your favorite functions to control a specific turtle
wiggleWave.up()
wiggleWave.color(MONO[-2])

# Make second turtle and adjust settings
mirrorTurt = turtle.Turtle() # this turtle mirrors my first turtle
mirrorTurt.width(4) # notice how I use the same format, but a different variable name!
mirrorTurt.up()
mirrorTurt.color(MONO[-3]) 

# Send them to opposite sides of the screen and face inward
wiggleWave.goto(startX, 0) # already facing to the right
mirrorTurt.goto(-startX, 0)
mirrorTurt.setheading(-90) # face to the left

# Now let's use PARAMETRIC FUNCTIONS to draw a wave. X will increase constantly, but Y will get wavy
# I'll define my variables here, to make it easy to copy. In practice, you should define these variables up by line 45
scale = 100 # how big I want my waves
wSize = 25 # how big I want my wiggles
numWaves = 2

for angle in range(360*numWaves):
    # for loop cycles through all the degrees in a circle to make a complete wave.
    
    X = angle # set x to angle BEFORE converting radians
    angle = math.radians(angle)
    Y = scale * math.sin(angle*2)  
    
    # RANDOM ELEMENT
    wiggle = wSize * (random.random() + -0.5) # random.random gives me a value between 0 and 1. I subtract 0.5 to get some negatives too.
    # I'll multiply it by my wSize to get the effect I want
    
    wiggleWave.goto(startX+X, Y+wiggle)
    mirrorTurt.goto(-startX-X, Y+wiggle) # mirror goes the OPPOSITE x direction
    
    wiggleWave.down()
    mirrorTurt.down()

panel.update() # becuase the animation is turned off (line 27), I'll update the panel after the for loop. The entire image will appear at once
    
#CLEAN UP
turtle.done() # I'm finished executing my code, so I'll tell Python not to expect any more commands
# this means I can't edit my work using the command line!
