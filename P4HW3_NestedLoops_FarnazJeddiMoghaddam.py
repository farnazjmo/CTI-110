# This program displays a stair-step pattern
# 10.17.19
# CTI-110 P4HW3 - Nested Loops
# Farnaz Jeddi Moghaddam


def main():
    num_steps=6                         # Define number of iterations
    for r in range(num_steps):
        print('#',end='',sep='')        # Print the first '#'
        for c in range(r):              # Define loop to print the spaces
           print(' ',end='',sep='')
        print('#')                      # Print the second '#'
main()
        
