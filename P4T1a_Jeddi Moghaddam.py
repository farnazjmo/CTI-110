# Using loops to draw repeating squares shown as Figure 13 of Page 180
# 10.15.19
# CTI-110 P4T1a - Repeating Squares
# Farnaz Jeddi Moghaddam

import turtle as t

# Named constants
num_squares = 100                  # Number of squares to draw
side = square_side = 10          # Starting side for the first square

# Draw 100 nested squares, with turtle
# by increasing sides after each square is drawn

for sq in range(1, num_squares + 1):
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    side = square_side + 3 * sq  # Increase the size of the side

    t.goto(0,0)                  # Return to base

t.done()
