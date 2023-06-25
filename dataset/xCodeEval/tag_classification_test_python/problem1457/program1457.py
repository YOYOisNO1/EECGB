def program1457():
    x,y,z=map(int,input().split())
    a,b,c=[int(x) for x in input().split()]
    print("YES" if a==x or y==b or z==c else "NO")