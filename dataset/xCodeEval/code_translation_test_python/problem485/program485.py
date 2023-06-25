def program485():
    n,m=[int(num) for num in input().split(" ")]
    if m-1==0:
        print(m*(n-1))
    else:
        print((n*(m-1)))