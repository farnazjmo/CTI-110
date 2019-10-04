# The program will ask for the length and width of two rectangles and tell
# the user which rectangle has greater area, or if two rectangles have equal areas.
# 10/01/19
# CTI-110 P3T1 - Areas of Rectangles
# Farnaz Jeddi Moghaddam

# Get the length and width of the rectangles
l1=float(input('Please enter the length of the first rectangle:' ))
w1=float(input('Please enter the width of the first rectangle:' ))

l2=float(input('Please enter the length of the second rectangle:' ))
w2=float(input('Please enter the width of the second rectangle:' ))

# Calculate the areas of the two rectangles
area1=float(l1 * w1)
area2=float(l2 * w2)

# Compare the areas of the rectangles and show the result
if area1>area2:
    print('The first rectangle has a greater area')
elif area1<area2:
    print('The second rectangle has a greater area')
else:
    print('The rectangles have equal areas')
