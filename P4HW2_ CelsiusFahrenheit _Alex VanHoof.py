# this program creates a chart of fahrenheit degrees to celcius
# 9/18/18
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Alex VanHoof
#
print( "Celsius Temperature\tFahrenheit Equivalent" )
for currentCelsiusTemperature in range( 21 ):
    fahrenheitTemperatureEquivalent = ( 9/5 ) * currentCelsiusTemperature + 32
    print( currentCelsiusTemperature,"\t\t\t\t", \
           format (fahrenheitTemperatureEquivalent, ".1f" ))
