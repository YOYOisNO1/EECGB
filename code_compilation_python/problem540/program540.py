def program540():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    k,l,m,n=sorted([k,l,m,n])
    num = 0
    if k!= 1 and l!=1 and m!=1 and n!=1:
    for i in range(1,(d+1)):
    if i % k == 0 or i % l == 0 or i%m == 0 or i%n == 0:
    num += 1
    else:
    num = d
    print(num)