# OOPS:

Object Oriented Programming or OOP is working with classes and objects. It involves interaction between objects having various attributes.

Python is a object oriented programming language. This meand that all the types are representation or instance of a type class.

## Components:
1. Class
2. Object


## Class:

It is a structure or a building block (a code block) representing or defining the attributes (features and behaviour) of similar parameters.

### Definition:
Using `class` keyword.
Name of a class should start with an uppercase letter.

Syntax: `class Class_name`


```python
class Student:
    roll_no = int()
    name = str()
```

## Object:

It is an instance of a class.

Syntax: `obj_name = Class_name()`


```python
student1 = Student() # creating a new object

student1.roll_no = 1
student1.name = 'Prabhu'
```


```python
print(student1.name)
print(student1.roll_no)
```

    Prabhu
    1
    

## *self* Keyword:

Calls the attributes for current instance or object.

Syntax: `self.attribute_name`

## Defining attributes in a class:

Attributes or Properties are  defined using a constructor.

### Constructor:
Executes a set of code whenever a new object/instance is created.

Defined by \_\_init\_\_ method.


```python
class Student:
    def __init__(self): # default constructor
        self.roll_no = 0
        self.name = 'Name'
#         print('__init__ file')
    
    def study():
        print('Studying....')
```


```python
st1 = Student()
st1.roll_no = 1
st1.name = 'Ravi'
print(f'Roll No: {st1.roll_no}, Name: {st1.name}')
```

    __init__ file
    Roll No: 1, Name: Ravi
    


```python
class Student:
    def __init__(self, rn = 0, st_name = 'Name'): # Parametric Constructor
        self.roll_no = rn
        self.name = st_name
#         print('__init__ file')
    
    def study():
        print('Studying....')
```


```python
st2 = Student(2, 'Rahul')
print(f'Roll No: {st2.roll_no}, Name: {st2.name}')
```

    Roll No: 2, Name: Rahul
    

## destructor:
Delete the current instance of class or object.

Use \_\_del\_\_ method

## Some other methods:

1. \_\_repr\_\_ - String representation
2. \_\_cmp\_\_ - Compare two objects
3. \_\_len\_\_ - length of object
4. \_\_lt\_\_ - less than
7. \_\_le\_\_ - less than or equal
8. \_\_gt\_\_ - greater than
9. \_\_ge\_\_ - greater than or equal
10. \_\_ne\_\_ - not equal
0. \_\_eq\_\_ - equal
5. \_\_getitem\_\_ - get a key from a iterable
6. \_\_setitem\_\_ - set a value to the given key of iterable

## Private variables and methods:

Start with \_\_

E.g.: \_\_var, \_\_method

It is advised for best programming practice to avoid calling private attributes outside the class.  
But if needed, use the following syntax:

`obj._classname__attribute`

## Calling a method in another method inside the class:

Use self keyword to call the function.

## Definining run time class attributes:

## Methods of attributes:


```python

```
