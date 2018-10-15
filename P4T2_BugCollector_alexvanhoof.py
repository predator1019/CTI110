# the program adds the number of bugs collected over 8 days
# 9/17/18
# CTI-110 P4T2 - Bug Collector
# Alex VanHoof

# initialize the accumulator
total=0

#get the bugs collected for each day
for day in range(1, 8):
    #prompt the user
    print('enter the bugs collected on day', day)
    #input the number of bugs
    bugs = int(input())
    #add bugs to the total
    total+= bugs
#display the total bugs.
print('you collected a total of',total,'bugs.')
