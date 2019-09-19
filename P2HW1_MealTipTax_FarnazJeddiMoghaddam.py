# This project will calculate the tip, tax, and total meal amount based on entered total food charge and percentages of tip and tax
# 9/19/19
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Farnaz Jeddi Moghaddam

#Get the total charge for food

total_charge=float(input('Please enter the total charge for food: '))

#Get the tip for server as percentage in decimal format

a=float(input('Please enter the tip percentage for server: '))
if a>=1:
    tip_percent=a/100
else:
    tip_percent=float(a)
    
#Get the tax percentage in decimal format

b=float(input('Please enter the tax percentage: '))
if b>1:
    tax_percent=float(b/100)
else:
    tax_percent=float(b)
    
#Calculate tip and tax amount

tip=total_charge * tip_percent
tax=total_charge * tax_percent
total_meal=float(total_charge + tip + tax)

#Display calculated tip, calculated tax, and total cost of meal

print('The amount of tip for server is: $',tip)
print('The amount of tax is: $',format(tax,',.2'))
print('The total amount of the meal is: $',total_meal)
