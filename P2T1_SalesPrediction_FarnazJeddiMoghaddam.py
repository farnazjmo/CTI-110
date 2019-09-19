# The program will calculate the profit as 23 percent of entered Total Sales amount
# 9/18/19
# CTI-110 P2T1 - Sales Prediction
# Farnaz Jeddi Moghaddam

#Input the total sales
Total_Sales=float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of total sales
Profit=(Total_Sales) * 0.23

#Display the profit
print('The profit is $',format(Profit,',.2f') )
