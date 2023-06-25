def program4143():
    x=int(input)
    a=input().split()
    s=[int(num)for num in a]
    q=0
    for i in s:
        q+=i
    if q%2==0:
        print('Bob')
    else:
        print('Alice')