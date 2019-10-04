# CTI-110
# P3HW1 - Month number
# Farnaz Jeddi Moghaddam
# 10/03/19

#Get the month number input from the user
def main():
    month=int(input("Please enter the month's numbr (1 through 12): "))

#Create dictionary for month numbers and names
    monthdict={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

#Compare the input number to display the result to the user
    if month in monthdict:
        month = monthdict[int(month)]
        print(month)
    else:
        print("The entered number is not in the range of 1 to 12!")
    
main()
