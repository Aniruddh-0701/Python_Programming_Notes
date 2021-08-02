# Example using factorial (n! = 1 * 2 * 3 ... n) n! = n * (n-1)!
def factorial(n, indent=''):
    print(indent, n)
    if -1 < n <= 1: 
        print(indent, 1)
        return 1 # End of recursion
    else: 
        fac = n * factorial(n-1, indent+' ') # recursive calling
        print(indent, fac)
        return fac

n = int(input())
print(factorial(n))
# Input: 6