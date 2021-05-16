## Functions in Python:
Function is a set of organized lines of code that performs a specific, well defined task.

It is used reduce the number of lines of code and improve reusability.

Syntax:  
*def* function_name(parameters): => function definition  
&nbsp; &nbsp; &nbsp;Statements  
&nbsp; &nbsp; &nbsp; *return* value(s)

...  
...  
function_name(parameters) => Caller

#### Return statement:(*return*)
Returns back a value as specified. It marks the end of a function


## Fruitful function
A fruitful function is a function that returns a value


```python
# Example 1:
def add(a, b): # Function Definition
    return a+b # returns the sum
x = int(input())
y = int(input())
print(add(x, y)) # Function Calling
# Input:
# 12
# 13
```

     12
     13
    

    25
    

## Lambda function (Inline or Anonymous function):
One liner of a function

Syntax:  
*lambda* parameters: Statement



```python
# Example 1
# def c(x):
#     return x % 2 == 0 #One line function to check if even
a = int(input())
c = lambda x: x % 2 == 0 # Equivalent lambda function
print(c(a))

# Input: 10
```

     10
    

    True
    

## Recursion:
Recursion is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem.

## Recursive function:
A function that performs recursion.

A recursive function calls itself repeatedly by dividing the problem into sub problems until the solution is obtained for the smallest sub-problem.

>*def* function(paramters1):  
&nbsp;&nbsp;&nbsp; function(parameters2) -- Recursive calling


```python
# Example using factorial
def factorial(n):
    if -1<n<=1: return 1 # End of recursion
    else: return n*factorial(n-1) # recursive calling

n = int(input())
print(factorial(n))
# Input: 6
```

     6
    

    720
    

Breaking down of problem:

n = 6  
n <= 1 False  
6 * factorial(5)  

n = 5  
n <= 1 False  
5 * factorial(4)  

n = 4  
n <= 1 False  
4 * factorial(3)  

n = 3  
n <= 1 False  
3 * factorial(2)  

n = 2  
n <= 1 False  
2 * factorial(1)  

n = 1  
n <= 1 (n==1) True  
1

Building up:

1 <br>
2 * 1  
3 * 2 * 1  
4 * 3 * 2 * 1  
5 * 4 * 3 * 2 * 1  
6 * 5 * 4 * 3 * 2 * 1  

720

#### Function Arguments or Parameters: (args or params)
Values passed into a function. They are optional
##### Types:  
1. Required Arguments
2. Keyword Arguements
3. Default Arguments
4. Variable length Arguments


#### 1. Required Arguments:

Positional Arguments.
These are arguments required to execute a function.  
The number of required arguments should be equal to the number of arguments passed.
If not, it will result in error.


```python
# Example 
def add(a, b): # Function Definition - no. of required arguments
    return a+b # returns the sum
x = int(input())
y = int(input())
print(add(x, y)) # Function Calling - no. of args passed

# Input:
# 12
# 23
```

     12
     23
    

    35
    


```python
#Example
# Example 
def add(a, b): # Function Definition - no. of required arguments
    return a+b # returns the sum
x = int(input())
y = int(input())
print(add(x)) # Function Calling - no. of args passed < no. of required args
```

     10
     23
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-30-34688768ab06> in <module>
          5 x = int(input())
          6 y = int(input())
    ----> 7 print(add(x)) # Function Calling - no. of args passed < no. of required args
    

    TypeError: add() missing 1 required positional argument: 'b'


#### 2. Keyword arguments (kwargs):
These arguments are not positional but are required.


```python
# Example 2
def add(a, b): # Function Definition - Parameters
    print(a, b)
    return a+b # returns the sum
x = int(input())
y = int(input())
print(add(b = x, a = y)) # Function Calling - Keywords are names of params used in definition
# Input: 10
# 23
```

     10
     23
    

    23 10
    33
    

#### 3. Default arguments:
Arguments which are optional. They have values by default.


```python
#Example 
def add(a, b = 0): # Function Definition - b is default args
    print(a, b)
    return a+b # returns the sum
x = int(input())
y = int(input())

# b given in function call
print('B given')
print(add(x, y)) # Function Calling

print()

# b not given in function call
print('B not given default = 0')
print(add(x)) # Function Calling

# Input: 12
# 23
```

     12
     23
    

    B given
    12 23
    35
    
    B not given default = 0
    12 0
    12
    

### Defining or indicating the difference in the type of args:
From python 3.8, '/' is used to Separate positional args from non positional.


```python
# Example 
def add(a, /, b=0): # Function Definition
    return a+b # returns the sum
x = int(input())
y = int(input())
print(add(x)) # Function Calling 
# Input: 10
# 23
```

     10
     23
    

    10
    

#### 4. Variable Length Arguments:
Args that are used when the number of arguments is not known.
The arguments passed are stored as a tuple. The arguments that start with ' * ' indicate Variable length arguments and are called **gather**


```python
#Example
# Example 
def add(a, *b): # Function Definition -  * incicates variable length arguments
    print(b)
    return a + sum(b) # returns the sum; sum is a built in function that returns sum of elements in an iterable
x = int(input())
y = int(input())
# 2 arguments
print(add(x, y))
print()
# 3 args
print(add(x, y, 10))
print()
# 4 args
print(add(x, y, 10, 20)) # Function Calling - no. of args passed

# Input: 10
# 23
```

     10
     23
    

    (23,)
    33
    
    (23, 10)
    43
    
    (23, 10, 20)
    63
    

#### Types:
1. *args
2. **kwargs

#### 1. &#42;args:
Variable length arguements that are most commonly used. Stores the values as tuple

#### 2. &#42;&#42;kwargs:
Variable length arguments of the form key = value. Stores the values as key-value mapping or dictionary.

### Scope of variable:
The part of code where a variable can be accessed.
Scopes: 
1. Global Variable
2. Local Variable

### 1. Global Variable:
Variable that can be acessed in any part of the program.

### 2. Local Variable:
Variable that can be accessed only inside a specific block or part of a program.


```python
#Example
def add(a, b): 
    c = a+b
    print(c)
    #return a+b

def printf():
    print(k)

x = int(input('x:'))
y = int(input('y:'))
add(x,y)
print('Hello')
s = 10
z = -100
for i in range(5):
    k = 'Hello'
    print(k)
print(x,y,s,z)
print(c)
printf()
print(k)

# Input:
# 10
# 23
```

    x: 10
    y: 23
    

    33
    Hello
    Hello
    Hello
    Hello
    Hello
    Hello
    10 23 10 -100
    


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-2716aba99fc1> in <module>
         18     print(k)
         19 print(x,y,s,z)
    ---> 20 print(c)
         21 printf()
         22 print(k)
    

    NameError: name 'c' is not defined



```python
def printf(): # Function definition
    global k
    k = 'Hi' #Local Variable Gloablized
    print(k)

for i in range(5):
    k = 'Hello' # Global Variable
    print(k) 

printf()
print(k)
```

    Hello
    Hello
    Hello
    Hello
    Hello
    Hi
    Hi
    

### Docstrings in Function:
Docstrings are most commonly used in a function.
They act as descriptor of function, i.e., they describe the function.

Calling docstings:
*function_name.&#95;&#95;doc&#95;&#95;*


```python
def fn():
    '''This is a docstring'''
print(fn.__doc__) # Calls docstring
```

    This is a docstring
    

## Recursion vs Iteration:

Recursion involves calling function repeatedly to breakdown a problem.  
Iteration is solving the problem by breaking down using loops.

Recursion is a easy way to solve a problem. But it is a bit time consuming.
Iteration is hard coding but is efficient in solving the problems.

This brings in a new programming stream called Dynamic Programming.



### Functions seen so far:
1. print
2. input
3. int
4. float

### 1. print:  
Syntax:
`print(values, [end=”\n”, sep=” ”])`


```python
print(1,2,3, sep = "") # no separation between the values
```

    123
    


```python
print(1,2,3)
```

    1 2 3
    


```python
print(1,2,3, sep = '\t')
```

    1	2	3
    


```python
print(1,2,3)
print(4,5)
```

    1 2 3
    4 5
    


```python
print(1,2,3, end='')# end of print is <none>
print(4,5)
```

    1 2 34 5
    


```python
print(1,2,3, end=' ') # end of print is <space>
print(4,5)
```

    1 2 3 4 5
    

### 2. input:
Syntax: `input(prompt="")`


```python
n = input()

# Input: 20
```

     20
    


```python
a = input(prompt = 'Prompt')

# Input: 10
```

    Prompt 10
    

### 3. int:
Syntax: `int(x, base = 10)`


```python
int('10')
```




    10




```python
b = '110'
int(b, 2)
```




    6




```python
x = '7af'
int(x, 16)
```




    1967




```python
o = '75'
int(o, 8)
```




    61



### 4. float:
Syntax: `float(x = 0)`


```python
float()
```




    0.0




```python
float ('1.2')
```




    1.2




```python
float(1)
```




    1.0




```python
float('12') 
```




    12.0



## Multiple Functions with same name:

Python does not allows multiple functions with different parameters with same name. If so exist, the last function definition replaces the first.


```python
def fn():
    return 'Hi'
def fn(x,y):
    return x+y
print(fn())
print(fn(10, 5))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-25-1b56bd1f0423> in <module>
          3 def fn(x,y):
          4     return x+y
    ----> 5 print(fn())
          6 print(fn(10, 5))
    

    TypeError: fn() missing 2 required positional arguments: 'x' and 'y'


## Gather vs Scatter:
Argument given to var. args are gathered and stored together to form a tuple. This is called gather.

Argument given as a list/tuple is split across required variable. This is called scatter


```python
#Example
def add(a, *b): # Function Definition 
    print(a, b)
    return a + sum(b) # returns the sum; sum is a built in function that returns sum of elements in an iterable
l = list(map(int, input().split()))
print(add(*l)) # Function Calling

# Input: 10
# 23
# 30
# 40
```

     10 23 30 40
    

    10 (23, 30, 40)
    103
    


```python

```
