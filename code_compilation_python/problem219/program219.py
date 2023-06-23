def program219():
    x = int(input())
    b = []
    for j in range(1,x+1):
        b.append(pow(j,j-1))
    print(sum(b)%(x+1))