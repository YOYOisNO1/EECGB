def program276():
    n = int(input())
    a = [int(x) for x in input().split()]
    mx = a.index(max(a))
    mi = a.index(min(a))
    l = len(a)-1
    print(max(mx-mi,l-mx,l-mi,mx,mi))