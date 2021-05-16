from time import *
from itertools import *
from math import *

def prime_gen(n):
    num = 2
    while num <= n:
        k = 2
        while k * k <= num:
            if num % k == 0:
                break
            k += 1
        else:
            yield num
        num += 1

prime = 2
prime_square = 4
__primeval__ = 3 # private value

if __name__ == '__main__':
    t = time()
    for i in prime_gen(10**2):
        print(i)
    # for i in islice(count(), 1, 10**3+1):
    #     print(i)
    print(time()-t)
