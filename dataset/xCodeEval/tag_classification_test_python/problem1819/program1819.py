def program1819():
    arr=["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    n=int(input())
    r=1
    while(r*5<n):
        n=n-(r*5)
        r=r*2
    print(arr[int((n-1)/r)])