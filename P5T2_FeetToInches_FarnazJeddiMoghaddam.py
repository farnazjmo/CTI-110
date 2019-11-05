# This program converts feet to inches
# 10.29.19
# CTI-110 P5T2_FeetToInches 
# Farnaz Jeddi Moghaddam

# Constant for the number of inches per foot
inches_per_foot = 12

# Main function
def main():
    # Get a number of feet from the user
    feet = float(input('Enter a number of feet: '))

    # Convert feet to inches
    print(feet, 'feet equals', feet_to_inches(feet), 'inches.')
    
# The feet_to_inches function converts feet to inches
def feet_to_inches(feet):
    return feet*inches_per_foot

# Call the main function
main()
