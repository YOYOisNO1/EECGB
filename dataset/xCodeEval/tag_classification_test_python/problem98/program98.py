def program98():
    # import sys
    # sys.stdin = open('/media/stuxnet/OS/Users/Rohan/OneDrive/Atom/RoundCodeforces/codeforces/input.txt', 'r')
    
    x,y,z=map(int,input().split())
    a,b,c=map(int,input().split())
    m=min(x,a)
    x-=m
    a-=m
    m=min(y,a+b)
    y-=m
    b=a+b-m
    z-=min(z,b+c)
    # print(a,b,c)
    if x==0 and y==0 and z==0:
        print("YES")
    else:
        print("NO")