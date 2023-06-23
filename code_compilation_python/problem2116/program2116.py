def program2116():
    [n,b] = [int(i) for i in input().split(" ")]
    a = [int(i) for i in input().split(" ")]
    m = int(input())
    a.sort() # small -> big
    
    receivable = reduce(lambda x, y: x + y, a[0:min(n,m)])
    payable = max(m-n, 0) * d
    
    print receivable - payable