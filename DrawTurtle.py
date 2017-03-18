import turtle #makes objects move
def draw_shapes(): #defining a function to draw shapes

    window = turtle.Screen()
    window.bgcolor("red")
    
    brad=turtle.Turtle() 
    brad.shape("circle")
    brad.color("green")
    brad.speed(0)
    square=0
    while square <= 3: #loop to draw square
        brad.forward(100)
        brad.right(90)
        square = square + 1

    seth=turtle.Turtle() #draw the circle
    seth.shape("arrow")
    seth.color("blue")
    seth.circle(100)
    
    tracy=turtle.Turtle()
    tracy.color("purple")
    tracy.right(90)
    tracy.forward(100)
    tracy.left(90)
    tracy.forward(100)
    tracy.left(135)
    tracy.forward(150)
        
    
    window.exitonclick()
        
draw_shapes()
