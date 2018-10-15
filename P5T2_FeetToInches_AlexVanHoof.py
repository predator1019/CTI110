# this code coverts any number of feet to inches
# 9/24/18
# CTI-110 P5T2_FeetToInches 
# Alex VanHoof
#

# constant for the number of inches per foot.
INCHES_PER_FOOT = 12

# main function
def main():
    #get a number of feet from the user.
    feet = int(input('enter a number of feet: '))

    # convert that to inches.
    print(feet, 'equals', feet_to_inches(feet),'inches.')

# the feet_to_inches function coverts feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

#call the main function.
main()
