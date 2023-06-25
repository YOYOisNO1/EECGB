def program3():
    k=int(input())
    l=int(input())
    c=0
    while k**c<l:
           c+=1
    if k**c==l:
           print("YES")
           print(c-1)
    else:
           print("NO")