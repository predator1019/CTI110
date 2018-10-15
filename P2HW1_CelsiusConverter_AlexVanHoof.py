# Converts temperature to celcius
# 9/5/18
# CTI-110 P2HW1 - Celsius Fahrenheit Converter 
# Alex VanHoof
#

#get the degrees to convert
degrees = float(input('enter the Fahrenheit degrees:'))

#calculate the degrees into celcius
degrees = F=9/5*degrees+32

#display the degrees.
print('the degrees in celcius is ', format(degrees, ',.2f'))
