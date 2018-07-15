from decimal import Decimal
# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, list_mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.
"""
Exercises
"""

def list_mean(list_numbers):
    """The mean of a set of numbers is the sum of the numbers divided by the
    number of numbers. Write a procedure, list_mean, which takes a list of numbers
    as its input and return the mean of the numbers in the list."""
    if not list_numbers:
        return "not a valid list"
    sum_numbers = 0
    for l_number in list_numbers:
        sum_numbers = sum_numbers + l_number
    return sum_numbers/float(len(list_numbers))

print(list_mean([1, 2, 3, 4]))
#>>> 2.5
print(list_mean([1, 3, 4, 5, 2]))
#>>> 3.0
print(list_mean([]))
#>>> ??? You decide. If you decide it should give an error, comment
# out the print line above to prevent your code from being graded as
# incorrect.
print(list_mean([2]))
#>>> 2.0
print(list_mean([7.7000000000000002, 1.2, 3.2000000000000002, 8.1999999999999993,3.3999999999999999]))
#>>> 4.74
print(list_mean([2, 4, 5, 6, 7, 1, 1, 1]))
#>>> 3.375
