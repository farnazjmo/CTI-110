# CTI-110 
# P3HW2 - MealTipTax 
# Farnaz Jeddi Moghaddam
# 10/03/19

#Get the total charge for food
def main():
    total_charge=float(input('Please enter the total charge for food: '))

#Get the tip percentage for server (16% or 18% or 20%)

    a=float(input('Please enter the tip percentage (16% or 18% or 20%): '))
    accepted_percentage=[16,18,20]
    if not(a in accepted_percentage):
        print("The value is outside the acceptable percentages.")
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
main()
