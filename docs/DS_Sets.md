# Data Structures or Derived data Types in Python:

Storing multiple values of same or different types under a single name.
They are collection of data.

1. List
2. Tuple
3. String
4. Dictionary
5. Set  
In this notebook, we'll discuss indepth on Sets

## Sets:
Sets are unordered collection of unique data.
Enclosed by Curly braces '{ }'  
`set: {10, 20.2, 30.0}`

Each value in the set is called a element  
Since set is unordered collection, it cannot be indexed. The elements are randomly stored.

## Defining a set:

### set() method

Syntax: `set(iterable = None)`  
iterable: any data structures listed above  

By default the { } map to a dictionary. So empty curly braces cannot be used.


```python
l = [10, 20, 30]
s = set(l)
s
```




    {10, 20, 30}




```python
s = {10, 20, 30, 10, 30}
s
```




    {10, 20, 30}



### Getting set as input:
s1 = set(input())  
s2 = set(input().split())

## Methods or Functions in sets:
There are various methods or functions that are used to work on sets.  
1. add  
2. update   
3. discard  
4. pop  
5. clear  
6. len  
7. issubset  
8. issuperset  
9. union  
10. intersection  
11. intersection_update  
12. difference  
13. symmetric_difference  
14. copy  
15. isdisjoint  
16. max  
17. min  
18. enumerate
19. sum
20. sorted

## 1. add:
Adds an element to the end of the set.

Syntax: `set.add(element)`


```python
set1 = {10, 20, 30}
set1.add(40)
set1
```




    {10, 20, 30, 40}



## 2. update:
Adds elements in another set to given set

Syntax: `set.update(set)`


```python
set1 = {10, 20, 30}
set2 = {10, 25, 40}
set1.update(set2)
set1
```




    {10, 20, 25, 30, 40}



### 3. discard:
Discards the given element in the set.

Syntax: `set.discard(element)`


```python
set1 = {10, 20, 30}
set1.discard(20)
set1
```




    {10, 30}



## 4. pop:
Removes and returns a random element from set.

Syntax: `set.pop()`


```python
set1 = {10, 20, 30}
set1.pop()
```




    10



## 5. clear:
Empties the set.

Syntax: `set.clear()`


```python
set1 = {10, 20, 30}
set1.clear()
set1
```




    set()



## 6. len
Returns the length of the set

Syntax: `len(set)`

## 7. issubset:
Checks if a set subset of another.

Syntax: `set.issubset(set)`  
Or set1 <= set2


```python
set1 = {10, 20, 30}
set2 = {10, 20}
set2.issubset(set1)
```




    True



## 8. issuperset:
Checks if the set superset of another.

Syntax: `set.issuperset(set)`  
Or set1 >= set2


```python
set1 = {10, 20, 30}
set2 = {10, 20, 30, 35}
set2.issuperset(set1) # set1.issubset(set2)
```




    True



## 9. union:
Returns the union of 2 sets

Syntax: `set.union(set)`  
Or set1|set2


```python
set1 = {10, 20, 30}
set2 = {12, 22, 30}
set1.union(set2)
```




    {10, 12, 20, 22, 30}




```python
set1 = {10, 20, 30}
set2 = {12, 22, 30}
set1|set2
```




    {10, 12, 20, 22, 30}



## 10. intersection:
Returns the intersection of 2 sets

Syntax: `set.intersection(set2)`  
Or set1 & set2


```python
set1 = {10, 20, 30}
set2 = {12, 22, 30}
set1.intersection(set2)
```




    {30}




```python
set1 = {10, 20, 30}
set2 = {12, 22, 30}
set1 & set2
```




    {30}



## 11. intersection_update:
Updates the set with intersection of given set.

Syntax: `set.intersection_update(set)`  
Or set1 &= set2


```python
set1 = {10, 20, 30}
set2 = {12, 22, 30}
set1.intersection_update(set2)
set1
```




    {30}




```python
set1 = {10, 20, 30}
set2 = {12, 22, 30}
set1 &= set2
set1
```




    {30}



## 12. difference:
Returns the set difference of given set

Syntax: `set1-set2`  
Or set1 - set2


```python
set1 = {10, 20, 30}
set2 = {12, 22, 30}
set1.difference(set2)
```




    {10, 20}



## 13. Symmetric Difference:
Returns the symmetric difference of two sets.

Syntax: `set.symmetric_difference(set)`
Or set1 ^ set2


```python
set1 = {10, 20, 30}
set2 = {12, 22, 30}
set1.symmetric_difference(set2)
```




    {10, 12, 20, 22}



## 14. copy:
Copies a set

Syntax: `set.copy()`


```python
set1 = {10, 20, 30}
set2 = set1.copy()
set2
```




    {10, 20, 30}



## 15. isdisjoint:
Checks if the given sets are mutually exclusive.

Syntax: `set.isdisjoint(set)`


```python
set1 = {10, 20, 30}
set2 = {1, 22, -37}
set1.isdisjoint(set2)
```




    True




```python
l = [10, -10, 20, -30, 40]
sum(l)
```




    30



### 16. max:
Returns the maximum value in the set.

Syntax: `max(set, key = None)`


```python
l = {10, 15, 50, 21, -7}
max(l)
```




    50




```python
l = {10, 15, 50, 21, -7, 7}
max(l, key = lambda x: x % 5) # Maximum reminder when divided by 5
```




    -7



### 17. min:
Returns minimum value in the iterable

Syntax: `min(iterable, key = None)`


```python
l = {10, 15, 50, 21, -7}
min(l)
```




    -7



### 18. enumerate:
Returns the enumerate object for given set. An enumerate object is an iterable which contains ordered pair of the form `(index, value)`  

Syntax: `enumerate(iterable, start = 0)`


```python
l = {10, 20, 'Hello', 'a', -1}
list(enumerate(l))
```




    [(0, 10), (1, 'Hello'), (2, 20), (3, 'a'), (4, -1)]



### 19. sum:
returns the sum elements in the set.

Syntax: `sum(set, start = 0)`

### 20. sorted:
It is a function used to sort.

Syntax: `sorted(iterable, key = None, reverse = False)`

## Printing the elements in a set:
1. Using loops
2. Using Variable length argument ( * )

### 1. Looping:
Use for loop to access element.

### 2. Using * :
Using * will convert the elements of into arguements of print method


```python
set1 = {10, 20, 30}
for i in set1:
    print(i)
```

    10
    20
    30
    


```python
set1 = {10, 20, 30}
print(*set1)
```

    10 20 30
    

## Comprehensions:


```python
set1 = set(i+1 for i in range(0, 10))
set1
```




    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}



## all and any:
*any* checks if any of the element in an iterable is true.

*all* checks if all the element on an iterable is True


```python
l = [10, 20, 30, 0]
print(any(l))
print(all(l))
```

    True
    False
    


```python
set1 = {10, 20, 30, -1}
print(any(set1))
print(all(set1))
```

    True
    True
    
