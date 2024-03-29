import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex

# Draw a square
for i in range(4):
    alex.forward(50)
    alex.left(90)

# Draw a triangle    
for i in range(3):
    alex.forward(80)            
    alex.left(120)

wn.mainloop()             # End commands. Wait for user to close window
