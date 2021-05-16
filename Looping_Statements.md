### Looping Statements:
Execute a group of lines repeatedly.

Finite looping is the best practice in programming but infinite looping are done because they are easy at times.

1. For loop
2. While loop

Looping variables are generally named i, j, and k, while other names can be used.

#### 1. For loop:
General and most common finite looping.

For loop is used to iterate through a sequence or iterator.
Lists, tuple, dictionary and string.
Syntax:
>*for* value *in* iterable:  
&nbsp;&nbsp;&nbsp; Statements


```python
# Example 1
l = [1, 2, 3, 4, 5]
for i in l:
    print(i)
```

    1
    2
    3
    4
    5
    


```python
# Example 2
s = 'Hello'
for char in s:
    print(char)
```

    H
    e
    l
    l
    o
    


```python
# Error for int
num = 10
for i in num:
    print(num)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-3-e4b54106f29e> in <module>
          1 num = 10
    ----> 2 for i in num:
          3     print(num)
    

    TypeError: 'int' object is not iterable


#### Range function:
Used to create an sequence/object from *start* to *stop* in *steps*

Syntax: *range*(stop)  
*range*(start, stop, [step=1])


```python
# Output of range
print(*range(1, 10))
print(*range(10))
```

    1 2 3 4 5 6 7 8 9
    0 1 2 3 4 5 6 7 8 9
    


```python
#Example 1
for i in range(10):
    print(i)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    


```python
#Example 2
for i in range(0, 20, 2):
    print(i)
```

    0
    2
    4
    6
    8
    10
    12
    14
    16
    18
    


```python
#Example 3
for i in range(0, 10, 1):
    print(i)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    

#### 2. While loops:
Most common for infinite looping.
Used to work on numbers or variable length iterables.
Preferred for variable conditions

Syntax: 
>*while* condition:  
&nbsp;&nbsp;&nbsp;Statements


```python
# Example 1:
i = 1
while i<=10:
    print(i)
    i+=1
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    


```python
# Example 2 using infinite looping
i = 1
while True:
    print(i)
    if i==100:
        break
    i+=1
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    50
    51
    52
    53
    54
    55
    56
    57
    58
    59
    60
    61
    62
    63
    64
    65
    66
    67
    68
    69
    70
    71
    72
    73
    74
    75
    76
    77
    78
    79
    80
    81
    82
    83
    84
    85
    86
    87
    88
    89
    90
    91
    92
    93
    94
    95
    96
    97
    98
    99
    100
    

#### Loop Control statements:

Control the execution of the loop

1. Break
2. Continue
3. Pass

#### 1. break

This statement ends the loop when encountered.

#### 2. continue

Skips the loop execution when encountered.

#### 3. pass
No change to loop
Used when there no statements currently present


```python
i = 1
while i<5:
    j=0
    while True:
        print(i)
        j+=1 # j = j+1
        if j==4:
            break
    i+=1
```

    1
    1
    1
    1
    2
    2
    2
    2
    3
    3
    3
    3
    4
    4
    4
    4
    


```python
#Example
i = 0
while i<11:
    i+=1
    if i==5: continue
    print(i)
```

    1
    2
    3
    4
    6
    7
    8
    9
    10
    11
    


```python
#Example 1
for i in range(10):
    if i%2 == 0:
        pass
    else: print(i)
```

    1
    3
    5
    7
    9
    


```python
#Example 2
for i in range (10):
    if i%2==0: pass
    else: print('Odd')
    print(i)
```

    0
    Odd
    1
    2
    Odd
    3
    4
    Odd
    5
    6
    Odd
    7
    8
    Odd
    9
    


```python

```
