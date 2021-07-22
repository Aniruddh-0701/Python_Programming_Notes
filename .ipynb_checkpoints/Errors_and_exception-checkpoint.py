def a():
    print("In a")
    b()
    print("Back in a")

def b():
    val = 52
    print("In b")
    val
    return val

a()