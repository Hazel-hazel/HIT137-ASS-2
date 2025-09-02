import turtle 
import math

def draw_edge(t, length, depth):

    if depth == 0:
        t.forward(length)
        return 
    
    segment = length / 3.0
    draw_edge(t, segment, depth - 1)
    t.right(60)
    draw_edge(t, segment, depth - 1)
    t.left(120)
    draw_edge(t, segment, depth - 1)
    t.right(60)
    draw_edge(t, segment, depth - 1)

def draw_polygon(t, sides, length, depth):
    exterior_turn = 360.0 / sides 
    for _ in range(sides):
        draw_edge(t, length, depth)
        t.right(exterior_turn)

def main():
    sides = int(input("Enter number of sides: "))
    length = int(input("Enter side length (pixels): "))
    depth = int(input("Enter recursion depth: "))
    colour = (input("Enter a colour: "))
    width = int(input("Enter a pen tip width: "))
    
    R = length / (2* math.sin(math.pi / sides))  # Calculate radius of polygon

    screen = turtle.Screen()
    t= turtle.Turtle ()
    t.speed(0)

    #t.pensize(2)  # Set width of pen tip
    t.up ()  # Pen up, so it doesn't draw while turtle is moved to start position
    t.left (90+ (360 / (2 * sides))) # Set polygon vertex intercept angle
    t.forward(R) # Send turtle one polygon radius to start position 
    t.setheading(0) # Face turtle East
    t.down () # Pen down, so it can draw
    t.pensize(width)  # Set width of pen tip
    t.pencolor(colour)  # Set colour of pen 

    draw_polygon(t, sides, length, depth)

    screen.mainloop()

if __name__ == "__main__":

    main()


