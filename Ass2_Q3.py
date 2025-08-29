"""
Hit137: Team Dan_Ext40
Assessment 2: Question 3

Program: Ass2_Q3.py
Authors: Maharun Momo Islam, Moneya Islam, Andrew Morris, Kudzaishe Mutyasira
Last date modified: 30/08/25

The purpose of this program is to...

"""

from turtle import Turtle

t = Turtle() # so we don't have to keep typing Turtle() 

t.width(2) # pen width
t.up () # pen up, so it doesn't draw while turtle is moved to start position
t.goto (-460, 460) # send turtle to start position coordinates
t.down () # pen down so it will draw 

sides = int(input("Enter the number of sides: "))
length = int(input ("Enter the side length: "))
depth = int(input ("Enter the recursion depth: ")) # only changes the size of the lines at this point

x = length/3 ** depth

if depth == 0:
    for i in range (sides):
        t.forward (length)
        t.left(360/sides)
else:        
    """ Defines a function to makes the line the pointy shape"""

def thirds():
    t.forward (x)
    t.right (60)
    t.forward(x)
    t.left (120)
    t.forward (x)
    t.right (60)
    t.forward(x)

""" Draws the polygon"""
for i in range (sides):
   
   """Example of depth one recursion, have to work out how to do it properly"""

   thirds()
   t.right (60)

   thirds()
   t.left (120)

   thirds()
   t.right (60)

   thirds()
   t.right (360/sides)

input ("Press any key to exit...") # Stops turtle window disappearing
