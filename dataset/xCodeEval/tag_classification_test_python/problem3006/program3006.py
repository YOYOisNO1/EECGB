def program3006():
    v = list(map(int,input().split()))
    c = list(map(int,input().split()))
    print(sum(c[0:v[0]-v[1]])+v[1]*v[2])