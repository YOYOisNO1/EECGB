def program2496():
    a=input()
    b=input()
    n=len(a)
    r=''
    for i in range(n):
     if a[i]==b[i]: r+='0'
     else: r+='1'
    print(r)