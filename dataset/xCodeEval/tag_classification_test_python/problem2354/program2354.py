def program2354():
    n=int(input())
    i=2
    while i*i<n and n%i:i+=1
    if i*i>n:i=n
    print(1+(n-i)//2)