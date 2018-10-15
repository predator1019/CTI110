# this program calculates the tuition for a college that has a 3% increase each year
# 9/19/18
# CTI-110 P4HW3 - Tuition Increase
# Alex VanHoof
#
currentTuition = 8000

print( "year\tTuition\n-----\t--------" )
for currentYear in range( 1,6 ):
    currentTuition += ( 3/100 ) * currentTuition
    print( currentYear, "\t$", format(currentTuition,".2f" ),sep = "")
