# this program can tell if the users number is prime or not
# 9/24/18
# CTI-110 P5HW1 - Prime Numbers
# Alex VanHoof
#

def is_prime( number ):
    evenDivisions = 0
    if number <= 1:
        return False
    for currentnumber in range( 1, number + 1 ):
        if number % currentnumber == 0:
           evenDivisions = evenDivisions + 1
           if evenDivisions > 2:
               return False
    return True

def main():
    number = int(input('please enter a number: '))
    print()
    if is_prime( number ):
        print(number,'is a prime number!' )
    else:
        print(number,'is NOT a prime number!' )

main()
