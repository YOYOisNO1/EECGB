def program18():
    a,b,c = map(int,input().split())
    count = 0
    count += 2*c
    if a==0 and b == 0:
        count += 0
    elif a != 0 and b ==0:
        count += 1
    elif a == 0 and b!=0:
        count += 1
    elif a==b:
        count += 2*a
    else:
        count += 2*min(a,b) + 1
    print(count)