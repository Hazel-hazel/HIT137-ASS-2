import turtle 

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
    sides = int(input("Enter number of sides:"))
    length = int(input("Enter side length (pixels):"))
    depth = int(input("Enter recursion depth:"))

    screen = turtle.Screen()
    t= turtle.Turtle ()
    t.speed(0)

    draw_polygon(t, sides, length, depth)

    screen.mainloop()

if __name__ == "__main__":
    main()