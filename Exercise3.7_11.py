
import math


def sum_of_given_numbers(n):
    total = 0
    for number in range(1,n+1,1):
        total = total + number
    print (total)
    return total

a = int(input("how many first natural numbers to sum? "))
    
sum_of_given_numbers(a)

