# Using Turtle, draw first and last name initials
# 10.15.19
# CTI-110 P4T1b - Initial
# Farnaz Jeddi Moghaddam


import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(4)            # increase pensize (takes integer)
t.pencolor("blue")     # set pencolor (takes string)
t.shape("turtle")
 

# draw a 'F' by using Turtle graphics

t.left(90)
t.forward(65)
t.right(90)
t.forward(40)
t.penup()
t.left(180)
t.forward(40)
t.left(90)
t.forward(25)
t.left(90)
t.pendown()
t.forward(25)

# move the pen to draw last initial

t.penup()
t.left(35)
t.forward(40)
t.right(35)
t.pendown()

# draw a 'J' by using Turtle graphics
t.forward(10)
t.right(90)
t.forward(50)
t.right(-180)
t.circle(10,-180)


# end commands
win.mainloop()             # Wait for user to close window
