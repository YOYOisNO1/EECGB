def program4544():
    for i in range(int(input())):
        n,k=[int(w) for w in input().split()]
        print((n**k)%(10**9+7))