def program490():
    n, k = map(int, input().split()) ; s = input()
    a = s.index('G') ; b = s.index('T')
    if a < b : 
       n = s[a:b+1:k]
       if 'G' in n and 'T' in n and '#' not in n: print("YES")
       else: print("NO")
    else:
       n = s[b:a+1:k]
       if 'G' in n and 'T' in n and '#' not in n: print("YES")
       else: print("NO")  