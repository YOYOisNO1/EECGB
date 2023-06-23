def program1067():
    line = input()
    data = [int(i) for i in line.split()]
    n,m,k = data
    
    limit = n - (n/k)
    if m <= limit :   print m % 1000000009 
    else:
        score = 0
        totry = m - limit
        for i in range(totry):
            score += k
            score *= 2
            m -=k
        score += m
        print score % 1000000009 