# Solution For [Code Practice 2](Practice_code2.md)


```python
# Question1
n = int(input())
print('Even' if n%2 == 0 else 'Odd')

# Input: 15
```

     15
    

    Odd
    


```python
# Question 2
n = int(input())
if n > 0: print('Positive')
elif n == 0: print('Zero')
else: print('Negative')

# Input: -7
```

     -7
    

    Negative
    


```python
# Question 3
mark = int(input())
if 90 < mark <= 100: print('O')
elif 80 < mark <= 90: print('A+')
elif 70 < mark <= 80: print('A')
elif 60 < mark <= 70: print('B+')
elif 50 <= mark <= 60: print('B')
elif 0 <= mark < 50: print('Fail')
else: print('Invalid')
    
# Input: 85
```

     85
    

    A+
    


```python
# Question 4
age = int(input())
if age > 17: print('Eligible')
else: print('Ineligible')
    
# Input: 27
```

     27
    

    Eligible
    


```python
# Question 5
```


```python
# Question 6 - Method 1
ch = input()
vowels=["a","e","i","o","u","A","E","I","O","U"] 
if ch in vowels: 
    print("vowel") 
else: 
    print("consonant")

# Input: f
```

     f
    

    consonant
    


```python
# Question 6 - Method 2
ch = input()
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u': 
    print("vowel")
elif ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print('vowel')
else: 
    print("consonant")

# Input: A
```

     A
    

    vowel
    


```python
# Question 6 - Method 3
ch = input()
vowels = 'aeiouAEIOU' 
if ch in vowels: 
    print("vowel") 
else: 
    print("consonant")

# Input: G
```

     G
    

    consonant
    


```python
# Question 7 - Method 1
n1 = int(input())
n2 = int(input())
if n1 > n2: print(n1)
else: print(n2)
    
# Input: 10
# 15
```

     10
     15
    

    15
    


```python
# Question 7 - Method 2
n1 = int(input())
n2 = int(input())
print(n1 if n1 > n2 else n2)

# Input: 10
# 7
```

     10
     7
    

    10
    


```python
# Question 8 - Method 1
n1 = int(input()) 
n2 = int(input()) 
n3 = int(input())
if n1 > n2 >= n3:
    print(n1) 
elif n2 > n1 >= n3:
    print(n2) 
else:
    print(n3)

# Input: 10
# 5
# -7
```

     10
     5
     -7
    

    10
    


```python
# Question 8 - Method 2
n1 = int(input()) 
n2 = int(input()) 
n3 = int(input())
if n1 > n2 and n1 > n3: 
    print(n1) 
elif n2 > n1 and n2 > n3: 
    print(n2) 
else: 
    print(n3)

# Input: 10
# 5
# -7
```

     10
     5
     -7
    

    10
    


```python
# Question 8 - Method 3
n1 = int(input()) 
n2 = int(input()) 
n3 = int(input())
if n1 > n2: 
    if n1 > n3: 
        print(n1)
    else: 
        print(n3)
else: 
    if n3 > n2:
        print(n3)
    else: 
        print(n2)

# Input: 5
# -7
# 10
```

     5
     -7
     10
    

    10
    


```python
# Question 9
n = int(input())  
root = int(n ** (1/2))
if root * root == n: 
    print("perfect square") 
else: 
    print("not perfect square")

# Input: 16
```

     16
    

    perfect square
    


```python

```
