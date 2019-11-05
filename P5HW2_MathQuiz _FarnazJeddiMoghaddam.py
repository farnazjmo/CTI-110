# The program give the user two random numbers to add
# and tell the user if the answer was correct or not
# 11.04.19
# CTI-110 P5HW2 - Math Quiz
# Farnaz Jeddi Moghaddam

import random
print('Welcome to Math Quiz!')

# random_number function generates the random numbers
def random_number():
    return random.randint(1,100)
    return random.randint(1,100)
     

# Perform the math quiz
def math_quiz():
    # Keep the random numbers in variables a and b
    a=random_number()
    b=random_number()
    # Keep the correct answer for comparison
    c=a+b
    while True:
        try:
            print(' ',a,'\n+',b)
            # Get the answer from the student
            ans=int(input('Enter the answer: '))
            if ans==c:
                print('Congratulations! You are right.')
                # Ask the user if he/she wants to continue
                return math_quiz() if input('Take the quiz again?(y/any key to exit)').lower()=='y' else 0
            else:
                print('That is incorrect.\n The correct answer is ',c)
        except ValueError:
            print('Input must be an integer value!')

# The main function
def main():
    # Call the math_quiz function
    math_quiz()
# Call the main function
main()

