# Data Structures or Derived data Types in Python:

Storing multiple values of same or different types under a single name.
They are collection of data.

1. List
2. Tuple
3. String
4. Dictionary
5. Set  
In this notebook, we'll discuss indepth on Dictionaries

## Dictionary:
Dictionaries are unordered collection of data.
They are key-value mapping.  
Represented by Curly braces '{ }'  
`dictionary : {1:10, 2:20, 3:30, 4:'Hello', 5:-2.0}`

Defined by - key : value.  
Each key-value map is separated by comma (,)

|Keys| 1| 2| 3| 4| 5|  
|---|---|---|---|---|---|  
|Values| 10| 20| 30| 40| 50|  

## Defining a dictionary:

1. '{ }'
2. dict()

### 1. '{}'
dict1 = {1:10, 2:20, 3:30}
### 2. dict()
Syntax: `dict(iterable = None)`  
iterable: any data structures listed above given that elements are present as key value mapping. 


```python
d1 = {}
type(d1)
```




    dict




```python
l = [(1, 10), (2, 20), (3, 35)]
d2 = dict(l)
print(d2)
type(d2)
```

    {1: 10, 2: 20, 3: 35}
    




    dict



## Methods or Functions in dictionaries:  
There are various methods or functions that are used to work with dictionaries.  
1. len  
2. str   
3. clear  
4. copy  
5. fromkeys  
6. get  
8. items  
9. keys  
10. values   
11. update  
12. pop
13. popitem
10. setdefault 

### 1. len:
Returns the length of the given iterable.

Syntax: `len(iterable)`


```python
d1 = {1: 12, 2: 23, 3: 34}
len(d1)
```




    3



### 2. str:
Returns the string format of the given dictionary.

Syntax: `str(dict)`


```python
d1 = {1: 12, 2: 23, 3: 34}
str(d1)
```




    '{1: 12, 2: 23, 3: 34}'



### 3. clear:
Deletes the items in the dictionary.

Syntax: `dict.clear()`


```python
d1 = {1: 12, 2: 23, 3: 34}
d1.clear()
d1
```




    {}



### 4. copy:
Returns the shallow copy of the given dictionary.

Syntax: `dict.copy()`


```python
d1 = {1: 12, 2: 23, 3: 34}
d2 = d1.copy()
d2
```




    {1: 12, 2: 23, 3: 34}



### 5. fromkeys:
Returns  a new dictionary form the given list of keys. By default the values are set to None.

Syntax: `dict.fromkeys(sep, val = None)`


```python
key = ['key1', 'key2', 'key3']
d2 = dict.fromkeys(key)
d2
```




    {'key1': None, 'key2': None, 'key3': None}




```python
key = ['key1', 'key2', 'key3']
d2 = dict.fromkeys(key, 0)
d2
```




    {'key1': 0, 'key2': 0, 'key3': 0}



### 6. get:
Returns the value of the given key if present else returns the default value given (None by Default).

Syntax: `dict.get(key, default = None)`


```python
d1 = {1: 12, 2: 23, 3: 34}
d1.get(1)
```




    12




```python
d1 = {1: 12, 2: 23, 3: 34}
print(d1.get(4))
```

    None
    


```python
d1 = {1: 12, 2: 23, 3: 34}
d1.get(4, 0)
```




    0



### 7. items:
Returns the list of key-value pairs in the dictionary.

Syntax: `dict.items()`


```python
d1 = {1: 12, 2: 23, 3: 34}
d1.items()
```




    dict_items([(1, 12), (2, 23), (3, 34)])



### 8. keys:
Returns the list of keys present in the dictionary.

Syntax: `dict.keys()`


```python
d1 = {1: 12, 2: 23, 3: 34}
d1.keys()
```




    dict_keys([1, 2, 3])



### 9. values:
Returns the list of values present on the dictionary.

Syntax: `dict.values()`


```python
d1 = {1: 12, 2: 23, 3: 34}
d1.values()
```




    dict_values([12, 23, 34])



### 10. update:
Adds the key-value pairs in second dictionary to the first.

Syntax: `dict.update(dict)`


```python
d1 = {1: 12, 2: 23, 3: 34}
d2 = {4: 45, 5: 56}
d1.update(d2)
d1
```




    {1: 12, 2: 23, 3: 34, 4: 45, 5: 56}



### 11. pop:
Removes and returns the value of given key. If the key is absent, Error is raised if default is not given.

Syntax: `dict.pop(key, [default])`


```python
d1 = {1: 12, 2: 23, 3: 34}
print(d1.pop(2))
d1
```

    23
    




    {1: 12, 3: 34}




```python
d1 = {1: 12, 2: 23, 3: 34}
print(d1.pop(4))
d1
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-31-59e0c7377e6c> in <module>
          1 d1 = {1: 12, 2: 23, 3: 34}
    ----> 2 print(d1.pop(4))
          3 d1
    

    KeyError: 4



```python
d1 = {1: 12, 2: 23, 3: 34}
print(d1.pop(4, 30))
d1
```

    30
    




    {1: 12, 2: 23, 3: 34}



### 12. popitem:
Removes and returns the last key-value pair of the dictionary.

Syntax: `dict.popitem()`


```python
d1 = {1: 12, 2: 23, 3: 34}
print(d1.popitem())
d1
```

    (3, 34)
    




    {1: 12, 2: 23}



### 13. setdefault:
Sets the default value to key if the key is absent.

Syntax: `dict.setdefault(key, value)`


```python
d1 = {1: 12, 2: 23, 3: 34}
d1.setdefault(4, 45)
d1
```




    {1: 12, 2: 23, 3: 34, 4: 45}



## Accessing elements:
The values in the dictionary are accessed by key.

Syntax: `dictionary[key]`


```python
d1 = {1: 12, 2: 23, 3: 34}
d1[2]
```




    23




```python
d1 = {1: 12, 22: 23, 3: 34}
d1[22]
```




    23




```python
d1 = {1: 12, 2: 23, 3: 34}
d1[4]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-36-d109a962441b> in <module>
          1 d1 = {1: 12, 2: 23, 3: 34}
    ----> 2 d1[4]
    

    KeyError: 4


## Adding or Modifying items:
Items can be added or modified by using keys.

Syntax: `dictaionary[key] = value` 


```python
d1 = {1: 12, 2: 23, 3: 34}
d1[2] = 24 # modify
d1[4] = 45 # add
d1
```




    {1: 12, 2: 24, 3: 34, 4: 45}



## Delete Elements:
Elements can be deleted by using the *del* keyword.

Syntax: `del dict[key]`


```python
d1 = {1: 12, 2: 23, 3: 34}
del d1[2], d1[3]
d1
```




    {1: 12}



## Printing Items:
Use for loop to iterate through the dictionary.


```python
d1 = {1: 12, 2: 23, 3: 34}
for key, val in d1.items():
    print(key, val)
```

    1 12
    2 23
    3 34
    

## Sorting a dictionary:
Dictionaries are sorted only by keys.


```python
d1 = {1: 12, 2: 23, 3: 34}
for i in sorted(d1.keys()):
    print(i, d1[i])
print()
for i in sorted(d1):
    print(i, d1[i])
```

    1 12
    2 23
    3 34
    
    1 12
    2 23
    3 34
    

## Nested Dictionaries:
Dictionaries inside a dictionary is nested dictionary.


```python
d1 = {1: 12, 2: 23, 'd': {1: 12, 2: 23, 3: 34}}
for i,j in d1.items():
    print(i,j)
```

    1 12
    2 23
    d {1: 12, 2: 23, 3: 34}
    

## Dictionaries and list Comprehension:
Dictionaries can be defined by comprehensions.

Syntax: `dict = {key: value (loops)}`


```python
d2 = {x: x**2 for x in range(10)}
d2
```




    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}



## Dictionaries for switch case:
Dictionaries can be used as switch cases.


```python
switch = {1: 'One',
          2: 'Two', 
          3: 'Three'}
switch[1]
```




    'One'


