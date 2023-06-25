def program737():
    n = int(input())
    k = 10**6 + 1
    for i in range(2,min(n,k)):
        while not n%i**2:
            n //= i
    print(n)