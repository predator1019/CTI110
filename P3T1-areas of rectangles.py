#areas of the rectangles
#9/10/18
#Tutorial - P3T1 - Areas of Rectangles
# Alex VanHoof


length1 = float(input('enter the length rectangle1:'))
width1 = float(input('enter the width of rectangle1:'))
length2 = float(input('enter the length of rectangle2:'))
width2 = float(input('enter the width of rectangle2:'))

rectangle1= length1*width1

rectangle2= length2*width2

print('the area of rectangle1 is',format(rectangle1,',.2f'))
print('the area of rectangle2 is',format(rectangle2,',.2f'))

if rectangle1 > rectangle2: print('the area of rectangle1 is greater')
if rectangle2 > rectangle1: print('the area of rectangle2 is greater')

