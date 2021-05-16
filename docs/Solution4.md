# Solution for [Code Practice 4](Practice_code4.md)


```python
# Question 1
def multiply(x, y):
    return x*y
m = int(input())
n = int(input())
print(multiply(m, n))

# Input: 
# 10
# 20
```

     10
     20
    

    200
    


```python
# Question 2
def perimeter_area(l, b):
    p = 2 * (l+b)
    a = l * b
    return p,a
l = int(input())
b = int(input())
perimeter, area = perimeter_area(l, b)
print(perimeter)
print(area)
# Input:
# 15
# 18
```

     15
     18
    

    66
    270
    


```python
# Question 3:
def print_times(n, v):
    for i in range(n):
        print(v)
    return

n = int(input())
s = input()
print_times(n, s)
```

     10
     Hello
    

    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    


```python

```
