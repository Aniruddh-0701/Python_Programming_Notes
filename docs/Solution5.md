# Solution for [Code Practice 5](Practice_code5.md)


```python
# Question 1:
n = int(input())
list1 = list()
for i in range(n):
    list1.append(int(input()))
print(list1)

# Input: 3
# 5
# 2
# -20
```

     3
     5
     2
     -20
    

    [5, 2, -20]
    


```python
# Question 19
r = int(input())
c = int(input())

matrix1 = [list(map(int,input().split())) for i in range(r)]
matrix2 = [list(map(int,input().split())) for i in range(r)]

for i in range(r): 
    for j in range(c): 
        print(matrix1[i][j] + matrix2[i][j], end=" ")  
    print()
```

     4
     4
     9 13 5 2
     1 11 7 6
     3 7 4 1
     6 0 7 10 
     -2 4 7 31
     6 9 12 6
     12 11 0 1
     9 10 2 3
    

    7 17 12 33 
    7 20 19 12 
    15 18 4 2 
    15 10 9 13 
    


```python
# Question 20
r = int(input())
c = int(input())

matrix1 = [list(map(int,input().split())) for i in range(r)] 
matrix2 = [list(map(int,input().split())) for i in range(r)]  
matrix3 = [list(map(int,input().split())) for i in range(r)]

for i in range(r): 
    for j in range(c): 
        print(matrix1[i][j] + matrix2[i][j] + matrix3[i][j], end=" ")  
    print()
```

     4
     4
     9 13 5 2
     1 11 7 6
     3 7 4 1
     6 0 7 10
     -2 4 7 31
     6 9 12 6
     12 11 0 1
     9 10 2 3
     0 2 8 6
     3 7 1 0
     0 0 1 2
     10 1 0 11
    

    7 19 20 39 
    10 27 20 12 
    15 18 5 4 
    25 11 9 24 
    
