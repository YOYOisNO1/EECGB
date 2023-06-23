def program517():
    a=list(map(int, input().strip().split(' ')))
    c=0
    for i in a:
        c+=i
    
    if(c%5==0 && c!=0):
        print(int(c/5))
    else:
        print("-1")