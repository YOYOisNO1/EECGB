def program3393():
    for z in range(int(input())):
        n,k,d= map(int, input().split())
        a = input().split()
        r= n
        for i in range(n-(d-1)):
            if len(set(a[i:i+d])) < r:
                r= len(set(a[i:i+d]))
        print(r)