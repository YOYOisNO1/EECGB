def f(n,a,b):
        losses = []
        # minimum wins
        for i in range(3):
            l = max([a[i-1] - (n-b[i]),0])
            losses.append(l)
        losses = sum(losses)
        #maximum wins
        wins = []
        for i in range(3):
            w = min([a[i-1],b[i]])
            wins.append(w)
        wins = sum(wins)
        return [losses,wins]
    
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    results = f(n,a,b)
    for i in results:
        print(i,end=' ')