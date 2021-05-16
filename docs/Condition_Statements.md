### Condition Statements
Condition statements or Control flow statements or Desicion Control Statements are statements that are used to control the flow or execution of a program.
The flow is controlled the values of few variables that decide the proceedings of a program.

The conditions statements have same basic structure in all programming languages.
The list of Control statements are:
1. *if* statement
2. *if - else* statements
3. *if - elif - else* statements
4. Nested *if - else* statements
5. Inline *if - else* statements

The condition given in the if statements need to result in allowed boolean values.  
1. For integral type: value!=0 is True and value=0 is False  
2. For list and tuple: length(value)>0 is True and length=0 is False  
(boolean as applicable)

#### 1. if statement:
Executes the statements inside the block only if the condition is satisfied.

Syntax: 
>*if* condition:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Statements

#### Note: Indentation in python indicates blocks.


```python
# Example
x = 14
y = 18
if y>x:
    print(y)
```

    18
    


```python
# Example2
x = int(input())
if x:
    print('not zero')

# Input: -1
```

     -1
    

    not zero
    

#### 2. *if - else* statements:
Executes *else* when *if* condition fails  
Syntax:  
>if condition1:  
&nbsp;&nbsp;&nbsp;&nbsp;Statements  
else:  
&nbsp;&nbsp;&nbsp;&nbsp;Statements

#### 3. *if - elif - else* statements:
Checks for truth of *elif* statement when *if* statement fails. Chain of *if-else*  
Syntax:  
>if condition1:  
&nbsp;&nbsp;&nbsp;&nbsp;Statements
elif condition2:  
&nbsp;&nbsp;&nbsp;&nbsp;Statements
else:  
&nbsp;&nbsp;&nbsp;&nbsp;Statements

#### 4. Nested *if - else* statements:
*if else* within another *if else* statement

Syntax:
>if condition1:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if condition2:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Statements  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Statements  
else:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if condition3:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Statements  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Statements  

#### 5. Inline *if - else* statements:
One liner of *if else* statements

Syntax:
> Statement1 if condition else Statement2
