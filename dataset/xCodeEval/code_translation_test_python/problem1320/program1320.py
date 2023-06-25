def program1320():
    input=__import__('sys').stdin.readline
    for _ in range(int(input())):
        n=int(input())
        i=2
        while i*i<=n and n%i!=0:
            i+=1
        if i*i>n:
            print(1,n-1)
        else:
            print(n//i,n//i*(i-1))