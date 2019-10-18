    # CTI-110
    # P4HW1 - Expenses
    # Farnaz Jeddi Moghaddam
    # 10.17.19

def main():
    # Create a variable to control the loop
    keep_going='y'          # Set while condition
    count=0                 # Set expense counter to 0
    expense=[]              # Define expense as array to store expenses 
    starting_amount=int(input('Please enter starting amount in account: '))
    # Get amount and expenses to calculate account balance
    while keep_going == 'y':
        exp=int(input('Please enter expense : '))
        expense.append(exp)
        count+=1
         # Check if the user wants to do another expense
        keep_going=str(input('Do you want to enter another expense? (y/n)'))
        #Display the amount before and after expenses
    print('Amount in account before expense substraction $', starting_amount)
    print('Number of expenses entered:', count)
    print('Amount in account AFTER expenses subtracted is $',starting_amount-sum(expense))
       

main()
        
