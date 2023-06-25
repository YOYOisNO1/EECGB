def program4912():
    input()
    a=[*map(int,input().split())]
    print(['chest','biceps','back'][max(0,1,2,key=lambda i: sum(a[i::3]))])