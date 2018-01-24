# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    output = 0
    while list_of_numbers:
        output = max(output, list_of_numbers.pop())
    return output



print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
