from turtle import Turtle
t = Turtle()
t.width(2)

sides = int (input("Enter the number of sides: "))
length = int (input ("Enter the side length: "))
depth = int (input ("Enter the recursion depth: "))


for i in range (sides):
    t.forward (length)
    t.left (360/sides)

input ("Press any key to exit...")   