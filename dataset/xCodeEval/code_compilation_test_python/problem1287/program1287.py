def program1287():
    # 1
    n, m = map(int, input().split())
    a = []
    c = 0
    color = 'CMY'
    for i in range(n):
         a.append(list(input().replace(' ', '')))
    for i in range(n):
         for j in range(m):
              if a[i][j] in color:
                   c += 1
         print()
    if c > 0:
         print('#Color')
    else:
         print('#Black&White')
    ~                                