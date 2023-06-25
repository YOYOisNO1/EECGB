def find_max(p,t):
        return max(3*p/10,p-p/250*t)
    a,b,c,d = list(map(int,input().split()))
    if find_max(a,c) > find_max(b,d):
        print("Misha")
    elif find_max(a,c) == find_max(b,d):
        print("Tie")
    else:
        print("Vasya")
    