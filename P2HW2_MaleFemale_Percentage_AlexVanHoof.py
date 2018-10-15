# A brief description of the project
# 9/5/18
# CTI-110 P2HW2 - Male Female Percentage
# Alex VanHoof
#

#the total amount of people in class

girls = float(input('enter the number of girls in the room:'))

boys = float(input('enter the number of boys in the room:'))

#calculate the percent of boys and girls
people= boys+girls

percent1 = boys/people

percent2 = girls/people

#display the percent of girls and boys
print(' percent of boys is', format(percent1,',.2f'))

print(' percent of girls is', format(percent2,',.2f'))
