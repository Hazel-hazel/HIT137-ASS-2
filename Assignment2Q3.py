'''
Hit137: Team Dan_Ext40

Assignment 2: Question 3

Program: Ass2_Q1.py

Authors: Maharun Momo Islam, Moneya Islam, Andrew Morris, Kudzaishe Mutyasira

Last date modified: 05/09/25

    Explanation 
The purpose of this program is to utilise Python's turtle graphics to generate a 
geometric pattern through a recursive function. The pattern begins with a regular 
polygon and recursively modifies each edge according to the given parameters to form 
an intricate design.

The program will ask for the following characteristics to be specified:
    - The number of sides: which determines the initial polygon.
    - The side length: the length of each edge of the initial polygon (in pixels). 
    - Recursion depth: this is how many times the pattern rules will be applied. 
    - The pen colour and tip width.
    
Of the specified shape, each edge will be divided into three equal sections, of which 
the middle will be replaced. In its place will be two sides of an equilateral triangle, 
pointed inwards, creating an 'indentation'. This transforms one straight edge into four 
smaller edges, which are all 1/3 of the initial edge length. This process will be repeated 
for as many times as specified by the recursion depth. 

'''


import turtle # Imports turtle graphics library 
import math  # Needed to centre polygon

def main():
    sides = int(input("Enter number of sides: "))
    length = int(input("Enter side length (pixels): "))
    depth = int(input("Enter recursion depth: "))
    colour = (input("Enter a colour: "))
    width = int(input("Enter a pen tip width: "))
    
    R = length / (2* math.sin(math.pi / sides))  # Calculate radius of polygon

    screen = turtle.Screen() # Creates a drawing window 
    t= turtle.Turtle () #Creates a turtle pen
    t.speed(0) # Defines drawing speed (fastest used) 

    t.up ()  # Pen up, so it doesn't draw while turtle is moved to start position
    t.left (90+ (360 / (2 * sides))) # Set polygon vertex intercept angle
    t.forward(R) # Send turtle one polygon radius to start position 
    t.setheading(0) # Face turtle East
    t.down () # Pen down, so it can draw
    t.pensize(width)  # Set width of pen tip
    t.pencolor(colour)  # Set colour of pen 

    draw_polygon(t, sides, length, depth)

    screen.mainloop() # Window remains open until manually closed 

# Recursive function to draw a single fractal edge 
def draw_edge(t, length, depth):
    if depth == 0: # If theres no recursions, just draw a straight line 
        t.forward(length)  # Move turtle forwards by 'length'
        return 

    segment = length / 3.0     # Divides edge into 3 equal segments 
    draw_edge(t, segment, depth - 1) # Draws the first third 
    t.right(60) # Turns line 60 degrees to the right for 'spike' 
    draw_edge(t, segment, depth - 1) # Draws next segment, part of 'spike' 
    t.left(120) # Turns line 120 degrees to the left, to make other side of 'spike' 
    draw_edge(t, segment, depth - 1) # Draws next segment 
    t.right(60) # Turns line back to its initial placement 
    draw_edge(t, segment, depth - 1) # Draws final segment 

# Recursive function to draw a full polygon 
def draw_polygon(t, sides, length, depth):
    exterior_turn = 360.0 / sides # Exterior angle needed to complete the polygon 
    for _ in range(sides): # Repeats for each side of the polygon 
        draw_edge(t, length, depth) # Draws one fractal side 
        t.right(exterior_turn) # Turns turtle to begin next side 

# Run program 
if __name__ == "__main__":
    main()











