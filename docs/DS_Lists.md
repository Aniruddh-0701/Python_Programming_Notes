# Data Structures or Derived data Types in Python:

Storing multiple values of same or different types under a single name.
They are collection of data.

1. List
2. Tuple
3. String
4. Dictionary
5. Set  
In this notebook, we'll discuss indepth on Lists

## Lists:
Lists are ordered collection of data.
Represented by square brackets '[ ]'  
`list : [10, 20, 30, 'Hello', -2.0]`

Each value in the list is called a element  
order of elements: index of element  
Index - may be positive or negative  

|Order (element) | First | Second | Third |...|Last|  
|---|---|---|---|---|---|  
|Positive Index| 0| 1| 2| ...| n-1|  
|Negative Index| -n| -n+1| -n+2| ...| -1|  

## Defining a list:

1. '[ ]'
2. list()

### 1. '[ ]'
l = [10, 20, 30]
### 2. list()
Syntax: `list(iterable = None)`  
iterable: any data structures listed above  


```python
l = [10, 'Hello', -3.9]
type(l)
```




    list




```python
list1 = list()
list1
```




    []




```python
list2 = list(1)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-3-2f4d7a16774a> in <module>
    ----> 1 list2 = list(1)
    

    TypeError: 'int' object is not iterable


### Getting list as input:
list1 = list(input())  
list1 = list(input().split())


```python
list1 = list(input())
list1

# Input: Hello
```

     Hello
    




    ['H', 'e', 'l', 'l', 'o']




```python
list2 = list(input().split())
list2
# Input: 10 20 30 40.0
```

     10 20 30 40.0
    




    ['10', '20', '30', '40.0']




```python
list3 = list(input().split())
list3
# Input: Hello Python
```

     Hello Python
    




    ['Hello', 'Python']



## Methods or Functions in list:
There are various methods or functions that are used to work on lists.  
1. append  
2. insert  
3. pop  
4. map  
5. filter  
6. sort  
7. sorted  
8. extend  
9. index  
10. remove  
11. reduce  
12. reverse  
13. len  
14. count  
15. sum  
16. max  
17. min  
18. enumerate

### 1. append:
Adds the given element to the end of the list.  
Syntax: `list.append(element)`


```python
# Example
l = []
n = 1
l.append(10)
l.append(15)
l.append('Hello')
l.append(n)
print(l)
```

    [10, 15, 'Hello', 1]
    

### 2. insert:
Inserts the element at the index specified  
Syntax: `list.insert(index, element)`


```python
# Example
list1 = [10, 15, 25, 30]
n = 35
list1.insert(2, 20)
list1.insert(-1, n)
list1
```




    [10, 15, 20, 25, 35, 30]



### 3. pop:
Removes and returns the element from the index specified. Default is last element

Syntax: `list.pop(index = -1)`


```python
list2 = [10, 100, 1000, 'Hi']
print(list2.pop())
print(list2)
print(list2.pop(1))
list2
```

    Hi
    [10, 100, 1000]
    100
    




    [10, 1000]



### 4. map:
Applies the given function to every element in a list or iterable.

Syntax: `map(function, iterable)`


```python
def sample_fn(x):
    return x+2
l = [1, 2, 3, 4]
l = list(map(sample_fn, l))
l
```




    [3, 4, 5, 6]



### Getting a list of integers or float as input:
Use map function to map int function to each value


```python
list1 = list(map(int, input().split()))
print(type(list1[0]))
list1

# Input: 10 20 30 40
```

     10 20 30 40
    

    <class 'int'>
    




    [10, 20, 30, 40]



### 5. filter:
Filters out the elements that match the given condition

Syntax: `filter(condition, iterable)`

The condition should be given as a function definition which can be mapped to each variable. 


```python
l = [1, -1, 0, 3, -10, 100]
list2 = list(filter(lambda x: x>0, l)) # A Lambda function used for condition
print(list2)
```

    [1, 3, 100]
    

### 6. sort:
Sorts the list as per the given condition

Syntax: `list.sort(key = None, reverse = False)`


```python
l = [10, 60, 0, 40, -100]
l.sort() # Ascending order
print(l)
l.sort(reverse = True) # Descending Order
print(l)
```

    [-100, 0, 10, 40, 60]
    [60, 40, 10, 0, -100]
    


```python
l1 = ['Hi', 'Python', 'how', 'String', 'Data', 'Sorting Strings']
l1.sort()
print(l1)
l1.sort(key = len, reverse = True)
print(l1)
```

    ['Data', 'Hi', 'Python', 'Sorting Strings', 'String', 'how']
    ['Sorting Strings', 'Python', 'String', 'Data', 'how', 'Hi']
    

### 7. sorted:
It is also function used to sort. Difference is that the sorted list should be reassigned to a variable.

Syntax: `sorted(iterable, key = None, reverse = False)`


```python
l2 = [10, 20, 50, 0, -10, -1, 100]
l2 = sorted(l2)
l2
```




    [-10, -1, 0, 10, 20, 50, 100]



### 8. extend:
Extends the given list using the elements of iterable, i.e. appends the elements of iterable to the given list  

Syntax: `list.extend(iterable)`


```python
l = [10, 20, 30, 40]
l.extend([50, 60, 70])
l
```




    [10, 20, 30, 40, 50, 60, 70]




```python
l1 = ['H','e', 'l', 'l', 'o']
l1.extend('Welcome')
l1
```




    ['H', 'e', 'l', 'l', 'o', 'W', 'e', 'l', 'c', 'o', 'm', 'e']



### 9. index:
Returns the index of the element in the list. If multiple elements exist, it gives the index of first occurrence. If the element is not in the list, it raises an error

Syntax: `list.index(element)`


```python
l = [10, 20, 30, 40, 10]
l.index(10)
```




    0



### 10. remove:
Removes the first occurence of the element if present. Raises error when element not present

Syntax: `list.remove(value)`


```python
l = [10, 20, 30, 40]
l.remove(20)
l
```




    [10, 30, 40]




```python
l.remove(20) # Removing element that is not present
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-7-39403d13bd0b> in <module>
    ----> 1 l.remove(20)
    

    ValueError: list.remove(x): x not in list


### 11. reduce:
Sequentially applies the elements in the list to a function to give the final value. To use this we need to call *functools* module. In depth study of modules will be dealt later

Syntax: `reduce(function, list)`


```python
from functools import reduce

def add(x, y):
    return x+y

l = [10, 20, 30, 40]
c = reduce(add, l)
c
```




    100



#### Explanation:
*Step 1:*
applies 10 and 20 to the function. result = 30

*Step 2:*
applies the result and next element (30). result = 60

*Step 3:*
applies the result and next element (40). result = 100

List end is reached. so the result 100 is returned

### 12. reverse:
Used to reverse the list.

Syntax: `list.reverse()`


```python
list1 = [10, 20, 30, 50, 60]
list1.reverse()
list1
```




    [60, 50, 30, 20, 10]



### 13. len:
Returns the length of the given iterable

Syntax: `len(iterable)`


```python
list2 = [10, 20, 30, -1, 123]
len(list2)
```




    5



### 14. count:
Returns the count of the element specified

Syntax: `list.count(element)`


```python
l = [10, 20, 30, 10, 20, 25, 20, 50]
print(l.count(20))
l.count(10)
```

    3
    




    2



### 15. sum:
returns the sum elements in the list or tuple.

Syntax: `sum(list, start = 0)`


```python
l = [10, -10, 20, -30, 40]
sum(l)
```




    30




```python
l = ['Hello', 'World'] # Non Numeric data raise error.
sum(l)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-2-4f5edc0ac672> in <module>
          1 l = ['Hello', 'World']
    ----> 2 sum(l)
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'


### 16. max:
Returns the maximum value in the list.

Syntax: `max(list, key = None)`


```python
l = [10, 15, 50, 21, -7]
max(l)
```




    50




```python
l = [10, 15, 50, 21, -7, 7]
max(l, key = lambda x: x % 5) # Maximum reminder when divided by 5
```




    -7



### 17. min:
Returns minimum value in the iterable

Syntax: `min(iterable, key = None)`


```python
l = [10, 15, 50, 21, -7]
min(l)
```




    -7



### 18. enumerate:
Returns the enumerate object for given list. An enumerate object is an iterable which contains ordered pair of the form `(index, value)`  

Syntax: `enumerate(iterable, start = 0)`


```python
l = [10, 20, 'Hello', 'a', -1]
list(enumerate(l))
```




    [(0, 10), (1, 20), (2, 'Hello'), (3, 'a'), (4, -1)]



## Accessing Elements in a list:

Elements of a list can be accessed using index.

*Example:*  
Consider a list, `l = [10, 20, 30, 40, 50]`. Length = 5

| Element | 10 | 20 | 30 | 40 | 50 |  
|---|---|---|---|---|---|  
|Position| 1| 2| 3| 4| 5|  
|Positive Index| 0 | 1 | 2 | 3 | 4 |  
|Negative Index| -5 | -4 | -3 | -2 | -1|  

Calling $i^{th}$ element:   
positive index: l [i-1]  
negative index: l [i - 1 - length]


```python
l = [10, 50, 20, 30, -2]
n = len(l) # length
print(n-1, l[n-1]) # Last Element Positive index
print(l[-1]) # Last Element negative index
print(l[2]) # third element
```

    4 -2
    -2
    20
    


```python
l = [10, 50, 20, 30, -2]
for index, element in enumerate(l):
    print(index, element)
```

    0 10
    1 50
    2 20
    3 30
    4 -2
    

## Slicing operator:
Used to get / set a sublist of a list. Denoted by '[ ]'

Syntax: `list_name[start = 0 : stop = length : step = 1]`


```python
# Getting sublist in forward direction
l = [10, 50, 20, 30, -2]
print(l[1:-1])
print(l[1::2])
print(l[::2])
```

    [50, 20, 30]
    [50, 30]
    [10, 20, -2]
    


```python
# Getting Sublist in reverse:
l = [10, 50, 20, 30, -2]
print(l[4:0:-1])
print(l[::-1]) # reverse of the list
print(l[::-2]) # reverse list every alternate term
```

    [-2, 30, 20, 50]
    [-2, 30, 20, 50, 10]
    [-2, 20, 10]
    

## Printing the elements in a list:
1. Using loops
2. Using Variable length argument ( * )

### 1. Looping:
Use for or while loop to access element or list.

### 2. Using * :
Using * will convert the elements of the list into arguements of print method


```python
# for loop to get index
l = [10, 20, 30, 40, 50]
for i in range(len(l)):
    print(l[i], end= ' ')
```

    10 20 30 40 50 


```python
# for loop to get elements
l = [10, 20, 30, 40, 50]
for i in l:
    print(i, end = ' ')
```

    10 20 30 40 50 


```python
# while loop to get index
l = [10, 20, 30, 40, 50]
i = 0
while i<len(l):
    print(l[i], end= ' ')
    i += 1
```

    10 20 30 40 50 


```python
# Using *
l = [10, 20, 30, 40, 50]
print(*l)
```

    10 20 30 40 50
    

## List Comprehension: 
It follows the form of the mathematical set-builder notation unlike the use of map and filter functions. It is used to create lists from either an existing like or a completely new list.
 
Set bulider form:
{$x: x ~\rm{\epsilon~ list}$}  
Example: `list1 = [expression (loops)]`


```python
# map vs comprehension
l = [10, 20, 30, 40, 50]
s = [i**2 for i in l] # squares of elements in list l using comprehension
sq = list(map(lambda x: x**2, l)) # Using map
print(*s)
print(*sq)
```

    100 400 900 1600 2500
    100 400 900 1600 2500
    


```python
# Equivalent of above comprehension
l = [10, 20, 30, 40, 50]
s = list()
for i in l:
    s.append(i ** 2)
print(*s)
```

    100 400 900 1600 2500
    


```python
# filter vs comprehension
l = [10, 20, 30, 40, 50]
mul_t = [i for i in l if i % 20 == 0] # Multiples o twenty in l Using Comprehension
mul_tc = list(filter(lambda x: x % 20 == 0, l )) #Using filter
print(*mul_t)
print(*mul_tc)
```

    20 40
    20 40
    


```python
# Equivalent of above comprehension
l = [10, 20, 30, 40, 50]
mul = list()
for i in l:
    if i % 20 == 0: mul.append(i)
print(*mul)
```

    20 40
    

## List Aliasing:
Aliasing a list variable with another name. Referring a single list by multiple names.  
Syntax: `new_name = old_name`


```python
a = [10, 20, 0]
b = a # aliasing list a
b
```




    [10, 20, 0]



## List Copying or Cloning:
Create a new instance of list with same value. It is used to copy a list to a new variable by new memory allocation.

### Types:
1. Shallow Copy
2. Deep copy

### Methods:
1. copy method
2. slicing operator
3. list method
4. copy module

### 1. Copy method:
Creates a shallow copy of variable  

Syntax: `new_list = list.copy(list_name)`


```python
l = [10, 20, 30, 40]
list1 = l.copy()
list1
```




    [10, 20, 30, 40]



### 2. slicing operator:
Another method for shallow copy

Syntax: `new_list = old_list[:]`


```python
l = [10, 20, 30]
list2 = l[:]
list2
```




    [10, 20, 30]



### 3. list function:
Create a new instance using list function. It also results in shallow copy

Syntax: `list_new = list(old_list)`


```python
l = [10, 20, 30]
m = list(l)
m
```




    [10, 20, 30]



### 4. Copy module:
Copy module can be used to copy list to new variable

Functions:
1. copy
2. deepcopy

#### 1. copy:
creates shallow copy

Syntax: `new_list = copy(list_name)`

#### 2. deepcopy:
Creates a deep copy

Syntax: `new_list = deepcopy(list_name)`


```python
import copy

l = [10, 20, 30]
m = copy.copy(l)
s = copy.deepcopy(l)
print(m)
s
```

    [10, 20, 30]
    




    [10, 20, 30]



## Multi-dimensional lists or matrices:
Lists in a list is called a multidimensional list or nested lists. They are generally used to work with matrices.

Example: `list = [[10, 20, 30], [40, 50, 60]]` - Two dimensional list

### Accessing elements using index:
Syntax: `list_name[outermost list index][inner list index]...`


```python
m = [[10, 20, 30], [40, 50, 60]] # two dimensional
print(m[0]) # first element in outermost list
print(m[0][0]) # first element in first inner list
```

    [10, 20, 30]
    10
    


```python
l = [ [[10, 20], [30]], 
     [[40, 50,], [60]] ] # three dimensional
print(l[0]) # first element in outermost list
print(l[0][0]) # first element in first inner list
print(l[0][0][0]) # first element in first innermost list in first inner list
```

    [[10, 20], [30]]
    [10, 20]
    10
    

## Matrix:
A rectangular array of elements. Two dimensional lists or tuples are used to work with matrices.

Each row of matrix is stored as a list

Example: `matrix = [[10, 20, 30], [40, 50, 60]]`

### Matrix input:
Matrix can be taken as input using loops or list comprehension.


```python
# Using loops and append function:
matrix1 = list()
n = int(input()) # no. of rows
for i in range(n):
    matrix1.append(list(map(int, input().split()))) # a row of integer input
matrix1
# Input: 3
# 10 2 -3
# -2 1 0
# 3 9 11
```

     3
     10 2 -3
     -2 1 0
     3 9 11
    




    [[10, 2, -3], [-2, 1, 0], [3, 9, 11]]




```python
# Using list comprehension:
m = int(input()) # no. of rows
matrix2 = [ list(map(int, input().split())) for i in range(m)] # a matrix input
matrix2
# Input: 3
# 10 2 -3
# -2 1 0
# 3 9 11
```

     3
     10 2 -3
     -2 1 0
     3 9 11
    




    [[10, 2, -3], [-2, 1, 0], [3, 9, 11]]



### Output:
Output is printed using for loop


```python
# Using iterable:
matrix3 = [[1, 2],[4, 3]] # A 2x2 matrix 
for i in matrix3:
    print(*i)
```

    1 2
    4 3
    


```python
# Using range:
matrix3 = [[1, 2],[4, 3]] # A 2x2 matrix 
for i in range(len(matrix3)):
    print(*matrix3[i])
```

    1 2
    4 3
    


```python
# Using nested loop:
matrix3 = [[1, 2],[4, 3]] # A 2x2 matrix 
for i in range(len(matrix3)):
    for j in range(len(matrix3[0])):
        print(matrix3[i][j], end=' ')
    print()
```

    1 2 
    4 3 
    

## Stack:
A data type where elements are arranged such that the elements can only be added to and removed from the last.  
It follows the principle *FILO* - First In Last Out

**Methods used:** append() and pop()

## Queue
A data type where elements are arranged such that the elements can only be added to the last and removed from the first.  
It follows the principle *FIFO* - First In First Out

**Methods Used:** append() and pop(0)

## Mutability:
It is the ability to change the value of an element in a Data structure during execution.

### 1. Mutables:
1. List
2. Dictionary
4. Sets

### 2. Immutable:
1. Tuple
2. String

## Working with lists:

1. Concatenation
2. Appending
3. Multiplication

### 1. Concatenation:
Two lists can be concatenated by using '+' operator.


```python
l1 = ['list']
l2 = ['Concatenation']
l1 + l2 # Concatenation
```




    ['list', 'Concatenation']



### 2. Appending:
A list can be appended to string using '+=' operator or by reassignment.


```python
l3 = ['Let']
ch = ['s']
l3 += ch # str3 = str3 + ch
l3
```




    ['Let', 's']



### 3. List Multiplication:
List multiplication results a list with repitition. It can be done using ' * ' operator.


```python
l4 = ['Namaste ', 'Hello']
l4*5
```




    ['Namaste ',
     'Hello',
     'Namaste ',
     'Hello',
     'Namaste ',
     'Hello',
     'Namaste ',
     'Hello',
     'Namaste ',
     'Hello']



## List Comparison:
Python allows usage of relational operators on List.

Python compares two lists using the elements present in them. Whenever a greater element is encounter thr boolean value is returned.
