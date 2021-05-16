# Some Indepth concepts on I/O:
I/O - Input/Output.
Input and Output are integral part of a program. This makes the program interactive (dynamic) and user friendly.

Input conditions and values may vary depending on situation / constraints. So handling Inputs is important.


## Variations:
1. One line Input of multiple values

### 1. One line input:
Multiple values can be given in one line as input which needs to be processed differently. This brings in the need for a method to work with them.

1. fixed type input
2. variable length input

Generally one line input uses multiple assignment by splitting the values down (or scattering) to the required variables.  
*map* functions are used to assign a function or change the data type of the variables.

#### 1. Fixed type:
In this type, the number of inputs in the line is fixed and known. A simple input statements has the required no. of variables in the LHS and input command with string splitting on the RHS.

#### 2. Variable length type
In this type, the number of inputs in the line is variable and only minimum count is known. A simple input statements has the required no. of variables with last variable working as gather variable (with * before its name) in the LHS and input command with string splitting on the RHS.


```python
# Example for two inputs
a, b = input().split()
print(a)
print(b)
# input: Hi Hello
```

     Hi Hello
    

    Hi
    Hello
    


```python
# Change type for input
c, d = map(int, input().split())
print(c, type(c), sep = '\n')
print(d, type(d), sep = '\n')
# Input: 10 20
```

     10 20
    

    10
    <class 'int'>
    20
    <class 'int'>
    


```python
# Var length input
a, b, *c = map(int, input().split())
print(a, type(a))
print(b, type(b))
print(c, type(c))
```

     10 20 30 40 50
    

    10 <class 'int'>
    20 <class 'int'>
    [30, 40, 50] <class 'list'>
    


```python
# one line input
x, y, z = map(int, input().split())
print(x, type(x))
print(y, type(y))
print(z, type(z))
```

     10 20 30
    

    10 <class 'int'>
    20 <class 'int'>
    30 <class 'int'>
    
