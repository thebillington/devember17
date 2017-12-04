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

#f(n, 0) = 0
#f(n, m) = n + f(n, m - 1) || - (n - f(n, m + 1))
#Create a multiplication function to multiply n and m
def multiply(n, m):

    #If m is 0 then return 0
    if m == 0:
        return 0

    #If m is less than 0 recursively call increasing m
    if m < 0:
        return - (n - multiply(n, m + 1))

    #If m is greater than 0 recursively call reducing m
    if m > 0:
        return n + multiply(n, m - 1)

#f(0) = 0
#f(n) = f(n - 1) + 2n - 1
#Create a function to find the square of a number
def square(n):

    #If n = 0 then return 0
    if n == 0:
        return 0

    #Otherwise return square(n - 1) + 2n - 1
    return square(n - 1) + (2 * n) - 1
    
print("\nSum of 1 to 5 = {}".format(sum(5)))
print("5! = {}".format(factorial(5)))
print("6 x 4 = {}".format(multiply(6, 4)))
print("7^2 = {}".format(square(7)))

