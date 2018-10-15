# this code converts any distance in kilometers to miles
# 9/24/18
# CTI-110 P5T1_KilometerConverter 
# Alex VanHoof
#
def main():
    #get the distance in kilometers.
    kilometers = float(input('enter a distance in kilometers: '))

    #display the distance converted to miles.
    show_miles(kilometers)
    
def show_miles(km):
    #calculate miles.
    miles = km * 0.6214

    #display the miles.
    print(km, 'kilometers equales', miles, 'miles.')

main()
