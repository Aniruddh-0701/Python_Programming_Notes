# Data Structures or Derived data Types in Python:

Storing multiple values of same or different types under a single name.
They are collection of data.

1. List
2. Tuple
3. String
4. Dictionary
5. Set  
In this notebook, we'll discuss indepth on Strings

## Strings:
Strings are ordered collection or an array of characters.
Represented by quotes either ' ' or " ".  
They are generally immutable. This means individual elements can't be changed.

`String : 'Hello', "Python"`

order of elements: index of element  
Index - may be positive or negative  

|Order (element) | First | Second | Third |...|Last|  
|---|---|---|---|---|---|  
|Positive Index| 0| 1| 2| ...| n-1|  
|Negative Index| -n| -n+1| -n+2| ...| -1|  

## Defining a String:

1. '' or ""
2. str()

### 1. Quotes:
str = 'String'
### 2. str()
Syntax: `str(value = None)`  


```python
str1 = 'Hello'
type(str1)
```




    str




```python
s = str([10, 20])
print(s)
type(s)
```

    [10, 20]
    




    str



## String Input:
All the values that are taken using `input()` method as strings.


```python
s1 = input()
type(s1)
# Input: String
```

     String
    




    str



## Working with Strings:

1. Concatenation
2. Appending
3. Multiplication

### 1. Concatenation:
Two strings can be concatenated by using '+' operator.


```python
str1 = 'String '
str2 = 'Concatenation'
str1+str2 # Concatenation
```




    'String Concatenation'



### 2. Appending:
A character can be appended to string using '+=' operator or by reassignment.


```python
str3 = 'Let'
ch = 's'
str3 += ch # str3 = str3 + ch
str3
```




    'Lets'



### 3. String Multiplication:
String multiplication results a string with repitition. It can be done using ' * ' operator.


```python
str4 = 'Namaste '
str4*4
```




    'Namaste Namaste Namaste Namaste '



## Built-in String Methods:
There are various methods to work with strings. But Unlike lists, string methods don't change strings as ther are immutable. Hence the returned value should always be reassigned.

Methods:
1. capitalize
2. upper
3. lower
4. Center
5. swapcase
6. find
7. rfind
8. index
9. startswith
10. endswith
11. isalnum
12. isalpha
13. isdigit
14. strip
15. split
16. join
17. replace
18. zfill
19. enumerate
20. len
21. isupper
22. islower
23. lstrip
24. rstrip
25. partition
26. ljust
27. rjust
28. sorted 

### 1. capitalize:
Capitalize the string. More specifically, first letter of the string in upper case and rest in lower case.

Syntax: `str.capitalize()`


```python
s1 = 'hello'
s1 = s1.capitalize()
s1
```




    'Hello'



### 2. upper:
Converts the string to upper case

Syntax: `str.upper()`


```python
s1 = 'hello'
s1 = s1.upper()
s1
```




    'HELLO'



### 3. lower:
Converts the string to lowercase

Syntax: `str.lower()`


```python
s1 = 'HI'
s1.lower()
```




    'hi'



### 4. center:
Returns original string to center of given width. The empty places are filled using fillchar

Syntax: `str.center(width, fillchar)`


```python
s1 = 'hii'
s1 = s1.center(5, '*')
s1
```




    '*hii*'




```python
s2 = 'Well'
s2 = s2.center(10, '-')
s2
```




    '---Well---'



### 5. swapcase:
Swaps the case of string to lower if in uppercase, to upper in lowercase

Syntax: `str.swapcase()`


```python
s1 = 'PyThon'
s1.swapcase()
```




    'pYtHON'



### 6. find:
Returns the index of start of substring if present in string else -1.

Syntax: `str.find(substring, start = 0, end = length)`


```python
s1 = 'Python'
s1.find('Py')
```




    0



### 7. rfind:
Returns index of start of last occurence substring if present in string else -1

Syntax: `str.rfind(substring, start = 0, end = length)`


```python
s1 = 'Hello Welcome'
s1.rfind('el')
```




    7



### 8. index:
Returns the index of substring given. Same as find but raises error if absent.

Syntax: `str.index(substring, start = 0, end = length)`


```python
s1 = 'Python'
s1.index('Py')
```




    0



### 9. startswith:
Checks if the given string starts with given Prefix.

Syntax: `str.startswith(prefix, start = 0, end = length)`


```python
str1 = 'preprocessing'
str1.startswith('pre')
```




    True



### 10. endswith:
Checks if the given string ends with the given suffix.

Syntax: `str.endswith(suffix, start = 0, end = length)`


```python
str1 = 'preprocessor'
str1.endswith('or')
```




    True



### 11. isalnum:
Checks if the given string is alpha-numeric, i.e., contains only alphabets or numbers.

Syntax: `str.isalnum()`


```python
s2 = '$hello_'
s2.isalnum()
```




    False




```python
s3 = 'dev23'
s3.isalnum()
```




    True



### 12. isalpha:
Checks if the given string is alphabetic, i.e., contains only alphabets.

Syntax: `str.isalpha()`


```python
s3 = 'dev23'
s3.isalpha()
```




    False




```python
s4 = 'python'
s4.isalpha()
```




    True



### 13. isdigit:
Checks if the given string is numeric, i.e., contains only numbers.

Syntax: `str.isdigit()`


```python
s3 = 'dev23'
s3.isdigit()
```




    False




```python
s5 = '123'
s5.isdigit()
```




    True



### 14. strip:
Removes the leading and trailing whitespaces by default, if any. If *chars* is given (string only), it removes only the characters in it.

Syntax: `str.strip(chars = None)`


```python
str1 = ' Hello '
str1.strip()
```




    'Hello'




```python
str2 = 'HhelloH '
str2.strip('H ')
```




    'hello'



### 15. split:
Return a list of the words in the string, using *sep* as the delimiter. *maxsplit* gives the Maximum no. of splits to be done. The remaining string returned as last element. By default whitespaces, line feed and carriage returns are taken as delimiters.

Syntax: `str.split(/, sep = None, maxsplit = -1)`


```python
str1 = 'Hello\n World\r'
str1.split()
```




    ['Hello', 'World']




```python
str2 = 'Hello-World '
str2.split('-')
```




    ['Hello', 'World ']




```python
str1 = 'Hello\n World\r'
str1.split(maxsplit = 1) # Limiting no. of split
```




    ['Hello', 'World\r']



### 16. join:
Returns a concatenated string of iterable (containing only strings) with *char* (string) as delimiter.

Syntax: `char.join(iterable)`


```python
list1 = ['Hello', 'World']
"".join(list1)
```




    'HelloWorld'




```python
list1 = ['Hello', 'World']
" ".join(list1)
```




    'Hello World'




```python
list1 = ['Hello', 'World']
"-".join(list1)
```




    'Hello-World'



### 17. replace:
Returns a copy of a string with given substring replaced by old substring. *count* is the max no. of occurences to be replaced, all be default.

Syntax: `str.replace(old_string, new_string, count = -1)`


```python
str1 = 'Hello World'
str1.replace('l','L')
```




    'HeLLo WorLd'



### 18. zfill:
Pads zeroes (0) to the start of the numeric string to fill the given width if width > length of string.

Syntax: `str.zfill(width)`


```python
num = '123'
num.zfill(2)
```




    '123'




```python
num = '123'
num.zfill(5)
```




    '00123'



### 19. enumerate:
Returns the enumeration object of given string.

Syntax: `enumerate(str)`


```python
str1 = 'Hello'
print('(Index, Value)')
print(*enumerate(str1), sep='\n') # enumeration object
```

    (Index, Value)
    (0, 'H')
    (1, 'e')
    (2, 'l')
    (3, 'l')
    (4, 'o')
    

### 20. len:
Returns the length o given string

Syntax: `len(str)`


```python
str1 = 'Prabhu'
len(str1)
```




    6



### 21. isupper:
Checks if the given string is in uppercase.

Syntax: `str.isupper()`


```python
str1 = 'HYMN'
str1.isupper()
```




    True



### 22. islower:
Checks if the given string is in lowercase.

Syntax: `str.islower()`


```python
str2 = 'welcome'
str2.islower()
```




    True



### 23. lstrip:
Removes the leading whitespaces by default, if any. If *chars* is given (string only), it removes only the characters in it.

Syntax: `str.lstrip(chars = None)`


```python
str1 = ' Hello '
str1.lstrip()
```




    'Hello '



### 24. rstrip:
Removes the trailing whitespaces by default, if any. If *chars* is given (string only), it removes only the characters in it.

Syntax: `str.rstrip(chars = None)`


```python
str1 = ' Hello '
str1.rstrip()
```




    ' Hello'



### 25. partition:
Partition the string into three parts using the given separator. 

If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string and two empty strings.

Syntax: `str.partition(sep)`


```python
str2 = 'Hello-World'
str2.partition('-')
```




    ('Hello', '-', 'World')




```python
str2 = 'Hello-World'
str2.partition('a')
```




    ('Hello-World', '', '')



### 26. ljust:
Pads given char (default - space) to the end of the string to fill the given width if width > length of string. Left justified string.

Syntax: `str.ljust(width, fillchar = ' ')`


```python
s1 = 'hii'
s1.ljust(5, '*')
```




    'hii**'



### 27. rjust:
Pads given char (default - space) to the start of the string to fill the given width if width > length of string. Right justified string.

Syntax: `str.rjust(width, fillchar = ' ')`


```python
s1 = 'hii'
s1.rjust(5)
```




    '  hii'



### 28. sorted:
Returns sorted string as a list based on given key.

Syntax: `sorted(iterable, key = None, reverse = False)`


```python
s1 = 'hii'
sorted(s1)
```




    ['h', 'i', 'i']



## Accessing Elements in a string:

Elements of a string can be accessed using index.

*Example:*  
Consider a string, `s = 'Hello'`. Length = 5

| Element | 'H' | 'e' | 'l' | 'l' | 'o' |  
|---|---|---|---|---|---|  
|Position| 1| 2| 3| 4| 5|  
|Positive Index| 0 | 1 | 2 | 3 | 4 |  
|Negative Index| -5 | -4 | -3 | -2 | -1|  

Calling $i^{th}$ element:   
positive index: s [i-1]  
negative index: s [i - 1 - length]


```python
s1 = 'Hello'
print(s1[0])
print(s1[-2])
```

    H
    l
    

## Slicing operator:
Used to get a substring of a string. Denoted by '[ ]'

Syntax: `string_name[start = 0 : stop = length : stride = 1]`


```python
s1 = 'Python is Easy to Learn'
s1[5:-3]
```




    'n is Easy to Le'



## Printing the elements in a string:
1. Using loops
2. Using * 

### 1. Looping:
Use for or while loop to access element or string.

### 2. Using * :
Using * will convert the characters in the string into arguements of print method


```python
s2 = 'Welcome'
for i in s2:
    print(i, end='')
```

    Welcome


```python
s3 = 'Python Programming'
for i in range(len(s3)):
    print(s3[i], end='')
```

    Python Programming


```python
s2 = 'Book'
print(*s2)
```

    B o o k
    

## Working with ASCII values:
Two built in methods, *ord* and *chr* can be used to work with ASCII values.

### 1. ord:
Returns the decimal ASCII (ordinal) value or Unicode point of given one-character string.

Syntax: `ord(c)`

### 2. chr:
Returns the one character Unicode or ASCII string of given ordinal.

Syntax: `chr(i)`


```python
s = 'a'
ord(s)
```




    97




```python
o = 97
chr(o)
```




    'a'



## String Comparison:
Python allows usage of relational operators on strings.

Python compares two strings using Lexicographical order (dictionary arrangement), i.e. using ASCII values of these characters.  
This means that 'B'(ASCII value = 66) is smaller than 'b' (ASCII value = 98)


```python
sample1 = 'Python'
sample2 = 'midhun'
sample1 > sample2
```




    False




```python
sample1 = 'PYTHON'
sample2 = 'pYTHON'
sample1 < sample2
```




    True




```python
sample1 = 'Hi'
sample2 = 'Hello'
sample1 > sample2
```




    True



## Some other methods in Python Strings:
1. max
2. min
3. reversed
4. splitlines
5. format

### 1. max:
Returns the maximum value in the given string. Returns the character with maximum ASCII value in the String by default.

Syntax: `max(String, key = None)`


```python
s = 'hello'
max(s)
```




    'o'




```python
s = 'hello'
max(s, key = lambda x: s.count(x))
```




    'l'



### 2. min:
Returns minimum value in the string. Returns the character with minimum ASCII value in the String by default.

Syntax: `min(iterable, key = None)`


```python
s = 'hello'
min(s)
```




    'e'



### 3. reversed:
Returns iterator object of reversed string.

Syntax: `revrsed(sequence)`


```python
s = 'hello'
for i in reversed(s):
    print(i, end='')
```

    olleh

### 4. splitlines:
Returns a list of strings split with carriage return and line feed (CRLF) as separator.

Syntax: `str.splitlines(keepends = False)`


```python
s1 = 'Hello\n\rPython'
s1.splitlines()
```




    ['Hello', '', 'Python']




```python
s1 = 'Hello\n\rPython'
s1.splitlines(keepends = True)
```




    ['Hello\n', '\r', 'Python']



### 5. format:
Returns formatted string as required.

Syntax: `str.format(*args, **kwargs)`

It was already discussed at String formatting in [Introduction to Python Programming](Introduction_to_Python_Programming.ipynb)

## String Formatting:
Refer discussion in [Introduction to Python Programming](Introduction_to_Python_Programming.ipynb)
