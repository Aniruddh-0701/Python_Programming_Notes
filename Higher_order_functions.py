def deco(k): # Higher order function / decorator
    def multiple(n):
        return n*k
    return multiple

second_multiple = deco(2)
n = int(input("Enter a num\n"))
print(second_multiple(n))