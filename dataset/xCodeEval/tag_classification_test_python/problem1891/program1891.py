def program1891():
    n=int(input())
    s=input()
    a,b=0,0
    for i in s:
        if i=='L':
            a+=1
        else:
            b+=1
    print(a+b+1)    