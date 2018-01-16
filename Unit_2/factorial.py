# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    out = 1
    while n>=2:
        out = out*n
	n = n-1
    return out




print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720


