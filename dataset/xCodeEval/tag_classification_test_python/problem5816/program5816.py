def program5816():
    n = int(input())
    pos = 0
    number = 1
    while pos<n: 
        pos = pos + number
        number = number +1
    print(n -(pos- number)-1)