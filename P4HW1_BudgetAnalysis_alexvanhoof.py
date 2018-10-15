# program that calculates the users budget expenses and if they went over it or not
# 9/18/18
# CTI-110 P4HW1 - Budget Analysis
# Alex VanHoof
#

userBudget = float(input("please enter how much you have budgeted "+ \
                         "for the month:"))
moreExpenses = 'y'
usertotalExpenses = 0
while moreExpenses == 'y':
    userExpense = float(input('enter an expense:'))
    usertotalExpenses += userExpense
    moreExpenses = input('do you have more expenses?: Type y '+ \
                         'for yes, any key for no:')

if usertotalExpenses > userBudget:
    print('you were over your budget of',userBudget,'by',usertotalExpenses - \
          userBudget)
elif userBudget > usertotalExpenses:
    print('you were under your budget of',userBudget,'by',userBudget - \
          usertotalExpenses)
else:
    print('you used exactly your buget of',userBudget,'.')
