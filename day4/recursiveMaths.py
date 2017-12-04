# Come very simple maths algorithms built recursively (I'm on the recursion hype)
# Sorry for the simplicity, there are only so many hours in a day
# Time started: 10:45pm
# Time finished: 

#f(0) = 0
#f(n) = n + f(n - 1)
#Create a recursive function to sum the numbers 0 to n
def sum(n):

    #If n is greater than 0 return this number plus sum(n-1)
    if n > 0:
        return n + sum(n - 1)

    #Otherwise return 0
    return 0

#f(1) = 1
#f(n) = n * f(n - 1)
#Create a function to calculate the factorial of a number
def factorial(n):

    #If n is greater than 0 return this number multiplied by factorial(n-1)
    if n > 1:
        return n * factorial(n - 1)

    #Otherwise return 0
    return 1
    
print("\nSum of 1 to 5 = {}".format(sum(5)))
print("5! = {}".format(factorial(5)))
