# Generators in Python:

Syntax similar to function but are used to generate values.

New instances are not created everytime the function is called.

### Types:
1. Function type generators
2. Inline generators

### 1. Function type:
Definition as a function. Difference is that it uses yield instead of return.


```python
def my_first_generator(): # Defining a generator
    i = 1
    while i<=100:
        yield i
        i += 1
for j in my_first_generator(): # Calling a generator
    print(j, end=' ')
```

    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 

### 2. Inline generators:
List comprehension inside paranthesis give inline generators.  
Syntax: `generator_name = (...List Comprehension...)`


```python
gen = ( 2*i for i in range(10) ) # Definition of a generator
for i in gen:
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
    

## next method:
Returns the next element of the generator.

Syntax: `generator.__next__()`


```python
def my_first_generator(): # Defining a generator
    i = 1
    while i<=100:
        yield i
        i += 1
gen = my_first_generator()
for j in range(50): # Calling a generator
    print(gen.__next__())
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
    


```python
gen = ( 2*i for i in range(10) ) # Definition of a generator
for i in range(5):
    print(gen.__next__())
```

    0
    2
    4
    6
    8
    
