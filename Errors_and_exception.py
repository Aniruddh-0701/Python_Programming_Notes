def a():
    print("In a")
    b()
    print("Back in a")


def b():
    print("In b")
    return 42 / 0


a()
