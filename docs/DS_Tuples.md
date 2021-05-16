# Data Structures or Derived data Types in Python:

Storing multiple values of same or different types under a single name.
They are collection of data.

1. List
2. Tuple
3. String
4. Dictionary
5. Set  
In this notebook, we'll discuss indepth on Tuples

## Tuple:
Tuples are ordered collection of data. Unlike Lists they are immutable.
Represented by parenthesis '( )'  
`tuple : (10, 20, 30, 'Hello', -2.0)`

Each value in the tuple is called a element  
order of elements: index of element  
Index - may be positive or negative  

|Order (element) | First | Second | Third |...|Last|  
|---|---|---|---|---|---|  
|Positive Index| 0| 1| 2| ...| n-1|  
|Negative Index| -n| -n+1| -n+2| ...| -1|  

## Defining a tuple:

1. '( )'
2. tuple()

### 1. '( )'
l = (10, 20, 30)  
add a comma ',' if tuple is singleton
### 2. tuple()
Syntax: `tuple(iterable = None)`  
iterable: any data structures listed above  


```python
t = (10, 30)
print(t)
type(t)
```

    (10, 30)
    




    tuple




```python
t1 = (10,)
print(t1)
type(t1)
```

    (10,)
    




    tuple




```python
t2 = tuple()
print(t2)
type(t2)
```

    ()
    




    tuple



## Working with tuples:

1. Concatenation
2. Appending
3. Multiplication

### 1. Concatenation:
Two tuples can be concatenated by using '+' operator.


```python
t1 = (10, 20)
t2 = (30,)
t1+t2
```




    (10, 20, 30)



### 2. Appending:
A tuples can be appended to string using '+=' operator or by reassignment.


```python
t1 = (10, 20)
t2 = (30,)
t1 += t2
t1
```




    (10, 20, 30)



### 3. Tuple Multiplication:
Tuple multiplication results a new tuple with repitition. It can be done using ' * ' operator.


```python
t1 = (10, 20)
t1*5
```




    (10, 20, 10, 20, 10, 20, 10, 20, 10, 20)



## Methods or Functions in tuple:
There are various methods or functions that are used to work on tuples.  

1. map
5. filter
7. sorted
9. index
11. reduce
12. reversed
13. len
14. count
15. sum
16. max
17. min
18. enumerate
20. zip

### 1. map:
Applies the given function to every element in a iterable.

Syntax: `map(function, iterable)`


```python
def sample_fn(x):
    return x+2
t = [1, 2, 3, 4]
t = tuple(map(sample_fn, t))
t
```




    (3, 4, 5, 6)



### 2. filter:
Filters out the elements that match the given condition

Syntax: `filter(condition, iterable)`

The condition should be given as a function definition which can be mapped to each variable. 


```python
t = (1, -1, 0, 3, -10, 100)
t2 = tuple(filter(lambda x: x>0, t)) # A Lambda function used for condition
print(t2)
```

    (1, 3, 100)
    

### 3. sorted:
Sorts the given tuple and returns a copy

Syntax: `sorted(iterable, key = None, reverse = False)`


```python
l2 = (10, 20, 50, 0, -10, -1, 100)
l2 = tuple(sorted(l2))
l2
```




    (-10, -1, 0, 10, 20, 50, 100)



### 4. index:
Returns the index of the element in the tuple. If multiple elements exist, it gives the index of first occurrence. If the element is not in the tuple, it raises an error

Syntax: `tuple.index(element)`


```python
l = (10, 20, 30, 40, 10)
l.index(10)
```




    0



### 5. reduce:
Sequentially applies the elements in the tuple to a function to give the final value. To use this we need to call *functools* module. In depth study of modules will be dealt later

Syntax: `reduce(function, tuple)`


```python
from functools import reduce

def add(x, y):
    return x+y

l = (10, 20, 30, 40)
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

End is reached. so the result 100 is returned

### 6. reversed:
Returns iterator object of reversed tuple.

Syntax: `revrsed(sequence)`


```python
s = (10, 20, 30)
for i in reversed(s):
    print(i, end=' ')
```

    30 20 10 

### 7. len:
Returns the length of the given iterable

Syntax: `len(iterable)`


```python
list2 = (10, 20, 30, -1, 123, 10.0)
len(list2)
```




    6



### 8. count:
Returns the count of the element specified

Syntax: `tuple.count(element)`


```python
l = (10, 20, 30, 10, 20, 25, 20, 50)
print(l.count(20))
l.count(10)
```

    3
    




    2



### 9. sum:
Returns the sum elements in the tuple.

Syntax: `sum(tuple, start = 0)`


```python
l = (10, -10, 20, -30, 40)
sum(l)
```




    30



### 10. max:
Returns the maximum value in the tuple.

Syntax: `max(tuple, key = None)`


```python
l = (10, 15, 50, 21, -7)
max(l)
```




    50




```python
l = (10, 15, 50, 21, -7, 7)
max(l, key = lambda x: x % 5) # Maximum reminder when divided by 5
```




    -7



### 11. min:
Returns minimum value in the iterable

Syntax: `min(iterable, key = None)`


```python
l = (10, 15, 50, 21, -7)
min(l)
```




    -7




```python
l = (10, 15, 50, 21, -7, 10.0)
min(l)
```




    -7



### 12. enumerate:
Returns the enumerate object for given tuple. An enumerate object is an iterable which contains ordered pair of the form `(index, value)`  

Syntax: `enumerate(iterable, start = 0)`


```python
l = (10, 20, 'Hello', 'a', -1)
tuple(enumerate(l))
```




    ((0, 10), (1, 20), (2, 'Hello'), (3, 'a'), (4, -1))



### 13. zip:
Returns zipped object containing order pairs of elements from given iterables.

Syntax: `zip(iterables)`


```python
l = (10, 15, 50, 21, -7, 8)
t = ['Ten', 'Fifteen', 'Fifty', 'Twenty One', 'Negative Seven']
print(*zip(l,t))
```

    (10, 'Ten') (15, 'Fifteen') (50, 'Fifty') (21, 'Twenty One') (-7, 'Negative Seven')
    

## Accessing Elements in a tuple:

Elements of a tuple can be accessed using index.

*Example:*  
Consider a tuple, `t = (10, 20, 30, 40, 50)`. Length = 5

| Element | 10 | 20 | 30 | 40 | 50 |  
|---|---|---|---|---|---|  
|Position| 1| 2| 3| 4| 5|  
|Positive Index| 0 | 1 | 2 | 3 | 4 |  
|Negative Index| -5 | -4 | -3 | -2 | -1|  

Calling $i^{th}$ element:   
positive index: t [i-1]  
negative index: t [i - 1 - length]

## Slicing operator:
Used to get / set a sub-tuple of a tuple. Denoted by '[ ]'

Syntax: `tuple_name[start = 0 : stop = length : step = 1]`


```python
t = (10, 20, 30, 40)
t[:3]
```




    (10, 20, 30)



## Printing the elements in a tuples:
1. Using loops
2. Using  * 

### 1. Looping:
Use for or while loop to access elements.

### 2. Using * :
Using * will convert the tuple elements into individual arguments of print method


```python
# for loop to get index
l = (10, 20, 30, 40, 50)
for i in range(len(l)):
    print(l[i], end= ' ')
```

    10 20 30 40 50 


```python
# Using *
l = (10, 20, 30, 40, 50)
print(*l)
```

    10 20 30 40 50
    

## List Comprehension in tuples: 
It follows the form of the mathematical set-builder notation unlike the use of map and filter functions. It is used to create tuples from either an existing one or a completely new tuple.
 
Set bulider form:
{$x: x ~\rm{\epsilon~ iterable}$}  
Example: `l = tuple(expression (loops))`


```python
# comprehension
l = [10, 20, 30, 40, 50]
s = tuple(i**2 for i in l) # squares of elements in list l using comprehension
sq = list(map(lambda x: x**2, l)) # Using map
print(*s)
print(*sq)
```

    100 400 900 1600 2500
    100 400 900 1600 2500
    

## Multi-dimensional tuples or matrices:
Like Lists, tuples / lists in a tuple is called a multidimensional tuple or nested tuple. They are generally used to store matrices.

Example: `list = ((10, 20, 30), (40, 50, 60))` - Two dimensional 

### Accessing elements using index:
Syntax: `tuple_name[outermost tuple index][inner]...`

## Matrix:
A rectangular array of elements. Two dimensional lists or tuples are used to work with matrices.

Each row of matrix is stored as a list / tuple

Example: `matrix = ([10, 20, 30], (40, 50, 60))`

### Matrix input:
Matrix can be taken as input using loops or list comprehension.

### Output:
Output is printed using for loop

## Variable length argument Tuples:
The input given to variable length arguements are gathered together to form a tuple

## Tuple Comparison:
Python allows usage of relational operators on Tuples.

Python compares two tuples using the elements present in them. Whenever a greater element is encounter thr boolean value is returned.
