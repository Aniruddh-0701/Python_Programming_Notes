#### Program:
A set of instructions to perform a specific task
#### Programming Language

A language used to write a program

#### Types of Programming language:
1.	Statically typed – Compiler; values defined before execution
2.	Dynamically typed – Interpreter; values defined during execution

#### Requirements for running a code:
1.	Compiler (Fastest)
2.	Interpreter 

### Python:  
- Easy typing  
- Open source  

It is dynamically typed Interpreted language.  

Python versions:  
1.	2.x
2.	3.x  
  
Latest: Python 3.9.1
Preferred 3.8.6

Things needed in a program:
1.	Input (i/p)
2.	Output (o/p)
3.	Values
4.	Operator  

###### Note:
[value] - optional parameter

### Input:
Input from the user is obtained using the input statement  
>Syntax: `input(prompt = "")`


```python
# Example 1
a = input('Enter a number ')

# Example 2
b = input()
```

    Enter a number 10
    

### Output:
The output is displayed to the user using the print statement
> Syntax: `print(values,..., end=”\n”, sep=” ”)`



```python
# Example 
print(a)
print()
print(a,b)
```

    10
    
    10 1
    

### Data in Python

Data: Unorderd collection of information

#### Types:
1. Numeric
2. Character
3. Boolean
4. Null
5. Derived or Complex Data Types

#### 1. Numeric:
Associated with number  
Eg: 10, 2.1, -99.7, 3.1416(pi)

##### Types:
1. Integer (int): 10, 100, 0, -5
2. Floating point numbers or double (float): 22/7, -0.15

#### 2. Character (char):
All characters that are defined by Unicode. Look the below chart for the list of characters allowed under ASCII (American Standard Code for Information Interchange) which are most commonly used.

<img src='ASCII chart.png'>

They are denoted using single quotes ('')

Eg: '1', 'a', '#'

#### 3. Boolean (bool):
Asserts if a condition is True or False
If denotion in Number:  
1. True - number != 0
2. False - number = 0

#### 4. Null or None:
If nothing is present

Above four primitive data types

#### 5. Complex Data Types (Derived):
Combination of above four data types

##### Types:
1. List
2. Tuple
3. Set
4. String
5. Dictionary

###### String:
A collection of characters

Eg: 'Prabhu', '123', "Hi", "Hello Python" 

##### Additional types in integers (Base):
1. Binary (base 2) [0,1]
2. Octal (base 8) [0-7]
3. Decimal (base 10) [0-9] Most Common
4. HexaDecimal (base 16) [0-9, A-F]  
The bases allowed are 2 to 35

### Literals
Literals are data that are used or processed in a program.

#### Types:
1. Constant - Values that do not change during the execution
2. Variable - Values that change

There are certain rules to be followed while naming a variable:  
- Should start only with an alphabet or underscore ('_')
- Can contain characters defined in ASCII except ( &#36;, &, \\, /, etc.)
- It should not be keyword
- No spaces
- Generally, uppercase alphabets are not used in the beginning of a variable name.

##### Naming Conventions:
[Naming Convention - Wikipedia article](https://en.wikipedia.org/wiki/Naming_convention_(programming))  
For  Easy readability 
- Function or use as name
- first letter in lowercase
- name has Multiple words:
    1. use underscore for space
    2. joint writing with words from second in caps
- No Long names

Naming convention for multi word variable names:
1. Camel case (abcAbc)
2. Pascal case (AbcAbc)
3. Screaming case (ABC)
4. Lazy case (abc)
5. Kebab case (ab-ab)
6. Snake case(ab_ab)  

E.g.: age, input_values, firstName, number, prime_num  
Not: user name, number_to_find_prime


```python
userName = input()
user_name = input()
```

    a
    

### Keywords or Identifiers or Reserved words:

Words used for a special purpose in program.

E.g: input, print, int, if, for, try, list, etc.


```python
# Key words
try
for
while
input
print
```

### Comments:

Lines that are not executed. It used only for understanding by the programmers or users

'#' is used to comment lines

### Documentation Strings or Doc strings:

''' ''' , """ """ define documentation strings.

Brief explanation of code.



```python
""" 
This line gives example of docstrings.
This doc strings can extend many lines
"""
print('Hi')
```

    Hi
    

### Type Casting and conversion:

Convert one form of data into another

`type()` function gives the data type of a variable

|Method|Result|Syntax|
|---|---|---|
|int()|Converts Numeric data into integer|int(x [, base=10])|
|float()|Converts Numeric Data into float|float(x)|
|str()|Converts Data into string|str([x])|
|ord()|Generates Unicode code point integer value of a character|ord(x)|
|chr()|Returns the Unicode character of given value|chr(x)|
|oct()|Returns octal value as a string|oct(x)|
|bin()|Returns Binary value as a string|bin(x)|
|hex()|Returns Hexadecimal value as a string|hex(x)|
|list()|Returns the list form of given iterable|list([x])|
|tuple()|Returns the tuple form of given iterable|tuple([x])|
|set()|Returns the set form of given iterable|set([x])|
|dict()|Returns Key-value mapping|dict([x])|



```python
print(type('123.0'))
a = float('123.0')
type(a)
```

    <class 'str'>
    




    float




```python
print(a)
int(a)
```

    123.0
    




    123



### Operators:
Used to perform arithmetic and logical operations
#### Types:
1. Arithmetic
2. Relational
3. Assignment
4. Logical
5. Bitwise
6. Membership
7. Identity

##### 1. Arithmetic:  
Perform arithmetic operations

|**Operator**|**Description**|**Example**|
|---|---|---|
|$+$ |Addition|2 $+$ 3 = 5|
|$-$ |Subtraction|2 $-$ 3 = -1|
|$*$ |Multiplication|2 $*$ 3 = 6|
|$/$ |Division|2 $/$ 3 = 0.66667|
|$//$	|Floor Division (quotient)|2 $//$ 3 = 0|
|%	|Modulo (returns remainder)|2 % 3 = 2|
|$**$	|Exponentiation|2 $**$ 3 = 8|
|$+$	|Unary Plus|$+$ 2|
|$-$	|Unary Minus|$-$3|

##### 2. Relational:
Relations between two variables

|Operator|Description|Example|
|---|---|---|
|$==$|Equal|a $==$ b|
|$!=$ or $<>$|Not Equal|a $!=$ b or a $<>$ b|
|$>$|Greater|a $>$ b|
|$>=$|Greater or Equal|a $>=$ b|
|$<$|Lesser|a $<$ b|
|$<=$|Lesser or Equal|a $<=$ b|

##### 3. Assignment:
Assigns value to a variable

|Operator|Description|Example|
|---|---|---|
|$=$|Assign|c $=$ 30|
|$+=$|Add and assign|a $+=$ b|
|$-=$|Subtract and assign|a $-=$ b|
|$*=$ |Multiply and assign|a $*=$ b|
| $/=$|Divide and assign|a $/=$ b|
|$//=$|Floor division and assign|a $//=$ b|
|%=|Get remainder and assign|a %= b|
|$**=$|Exponentiation and assign|a $**=$ b|
|$:=$|Walrus operator (to define values from a function)|y $:=$ f(x)|

###### Note:
Walrus operator came into python in version 3.8. It will not work in previous versions.

##### 4. Logical:
Perform Logical operations

|Operator|Description|
|---|---|
|and|Logical Operator AND|
|or|Logical Operator OR|
|not|Logical operator NOT|

##### 5. Bitwise:
Perform bitwise operations

|Operator|Description|Syntax|Example|
|---|---|---|---|
|&|Bitwise AND| x & y |101 & 11|
| &#124; |Bitwise OR| x &#124; y|101 &#124; 11|
|~|Bitwise NOT|~x|~1|
|^|Bitwise XOR|x ^ y|1 ^ 1|
|<<|Shifts y bits in x to the left (Left shift operator)| 	x << y|111001 << 2|
|>>|Shifts y bits in x to the right (Right Shift Operator)|	x >> y|111001 >> 2|

##### 6. Membership:   
Check if an iterable object contains the element  

|Operator|Description|Syntax|  
|---|---|---|  
|in|True if element in iterable|x in y|  
|not in| True if element not in iterable|x not in y|

##### 7. Identity operator:
Checks if two operands point to same object  

|Operator|Description|Syntax|  
|---|---|---|  
|is|True if point to same object|a is b|  
|is not| True if they do not point| a is not b|  


#### Expressions:

A statement that gives a finite value.

Types:
1. Infix expressions:  
Example: 12 + 23
2. Prefix expressions:  
Example: + 12 23
3. Postfix expressions:  
Example: 12 23 +

#### Escape Sequence:  
Few special characters defined under ASCII for formatting strings/ output

|Sequence|Explanantion|  
|---|---|
|\\\\|Back slash|
|\\'|Apostrophe or Single quotes|
|\n|new line or line feed|
|\f|form feed|
|\r|carriage return|
|\t|horizontal tab|
|\\"|Double quotes|
|\0|Null character|
|\a|bell|
|\v|vertical tab|
|\u...|unicode character|
|\o...|octal values|
|\x...|hexa decimal values|

### String formatting:
String formatting or output formatting is an important part of a program output.
The display of output in user understandable form is important.

The following are the string formatting methods used (in the order of increasing preference):
1. Simple or no formatting
2. Formatting using format specifiers
3. Formatting using the format() method
4. f-strings

#### 1. Simple formtting
`print('string', variable)`


```python
name = input('Enter your name ')
print('Hello', name,', Welcome')

# Input: Prabhu
```

    Enter your name  Prabhu
    

    Hello Prabhu , Welcome
    

#### 2. Format Specifiers:
% symbol indicate format specifiers.

Types:
1. Integer: %d
2. Float: %f
3. Character: %c
4. String: %s  
`print('string format_specifier'%(order of variables))`


```python
name = input()
# printf("%d", a); in C
print('Hello %s, Welcome'%(name))

# Input: Sooriya
```

     Sooriya
    

    Hello Sooriya, Welcome
    


```python
str1 = 'Python'
ver = 3.8
print('Hello %s, Welcome to %s%.1f'%(name, str1, ver))
print("Welcome to %s%.1f %s"%(str1, ver, name))
```

    Hello Sooriya, Welcome to Python3.8
    Welcome to Python3.8 Sooriya
    

#### 3. Format Method:
Uses `.format()` method  
`print("string {order}".format(variables))`


```python
print("Hello {}, Welcome".format(name))
```

    Hello Midhun, Welcome
    


```python
string1 = 'Python'
print("Hello {0}, Welcome to {1}{2}".format(name, string1, ver))
print("Hello {}, Welcome to {}".format(name, string1))
print("Welcome to {}{} {}".format(str1, ver, name))
```

    Hello Sooriya, Welcome to Python3.8
    Hello Sooriya, Welcome to Python
    Welcome to Python3.8 Sooriya
    

#### 4. F-strings:
F-strings or formatted strings used to format strings using variables  
`f'string {variable}'`  
The f-strings came after Python 3.6


```python
print(f'Hello {name}, Welcome to {string1}')
```

    Hello Sooriya, Welcome to Python
    


```python
print(f'Hello {name} '\
     f'Welocme to {string1}{ver}')
```

    Hello Sooriya Welocme to Python3.8
    

### Float and integer formatting:

The format method is used to format integers and floats as required.

#### Integer Formatting:
Leading zeroes adding to integers
Eg: 01 002
##### 1. Format Specifiers:
`%d` - integer  
`%0nd` - no. of leading zeroes = n - no. of digits in the integer 
##### 2. format method:
`format(int_value, format)`
##### 3. f-strings:
`{int_value:0nd}`
#### Float formatting:
Round off decimal places  
Eg: 10.1234: 10.12
##### 1. Format Specifiers:
`%f` - float  
`%.2f` - 2 decimal places
##### 2. format method:
`format(float_value, format)`
##### 3. f-strings:
`{float_value:.nf}`



```python

```

## Muliple Assignment in one line:
Python allows assignment of different variables in one line.

Syntax: `var1, var2, var3, ... = val1, val2, val3, ...`


```python
a, b, c, d = 10, 20, 30, 40
print(a)
print(b)
print(d)
print(c)
```

    10
    20
    40
    30
    
