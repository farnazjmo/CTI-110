# CTI-110 
# P3LAB - Debugging 
# Farnaz Jeddi Moghaddam
# 10.03.19

#Named constants to represent the grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

#Get a test score from the user
score=int(input('Enter your test score: '))

#Determine the grade
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your score is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
          
