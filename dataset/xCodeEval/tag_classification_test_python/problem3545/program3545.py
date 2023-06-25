def program3545():
    n, k = list(map(int, input().split()))
    g = list(input())
    for x in range(0,k):
        i = 0
        while i < n-1:
                if g[i] == "B" and g[i+1] == "G":
                    g[i] = "G"
                    g[i+1] = "B"
                    i+=2
                else:
                    i+=1
    z = ''
    for x in g:
        z+=x
    print(z)