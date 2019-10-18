# CTI-110
# P4HW2 - MealTipTax
# Farnaz Jeddi Moghaddam
# 10.17.19

def main():
    
    total_charge=float(input('Please enter the total charge for food: '))           # Get the total amount of meal charge
    accepted_percentage=[0.16,0.18,0.20,16, 18,20]                                  # Set the accepted amounts for tip percentages
#Get the tip percentage for server (16% or 18% or 20%)
    correct=False               # Set the label to go back to at the end of loop
    while not correct:
        a=float(input('Please enter the tip percentage (16% or 18% or 20%): '))
        if not(a in accepted_percentage):
            print("The value is outside the acceptable percentages. Please enter the percentage in following formats: 0.18 or 18%)")
        elif a>=1:
            tip_percent=a/100
        else:
            tip_percent=float(a)
    
#Calculate tip and tax amount

        tip=total_charge * tip_percent
        tax=total_charge * 0.06
        total_meal=float(total_charge + tip + tax)

#Display original food charge, calculated tip, and total cost of meal

        print('The amount of original food charge is: $',total_charge)
        print('The amount of tip for server is: $',tip)
        print('The amount of tax is: $',format(tax,',.2'))
        print('The total amount of the meal is: $',total_meal)
        keep_going=str(input('Do you want to enter another tip percentage? (y/n)'))     # Ask user if they'd like to run the program again
        if keep_going is 'y':           # Continue to run the program again if user says 'y'
            correct=False
        else:
            correct=True
main()

