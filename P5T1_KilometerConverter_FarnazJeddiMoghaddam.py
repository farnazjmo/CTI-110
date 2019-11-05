# This program converts kilometers to miles
# 10.29.19
# CTI-110 P5T1_KilometerConverter 
# Farnaz Jeddi Moghaddam


conversion_factor=0.6214

#The main function gets the distance in kilometers and
#calls sho_miles function to convert it
def main():
    #Get the distance in kilometers
    kilometers=float(input('Enter a distance in kilometers: '))

    #Display the distance converted to miles
    show_miles(kilometers)

#The show_miles function the parameter km from kilometers to miles
# and displays the result
def show_miles(km):
    #Calculate miles.
    miles=km*conversion_factor

    #Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

#Call the main function
main()
