def program4485():
    import math
    n = int(input())
    m = int(input())
    R = []
    for i in range(n):
           R.append(int(input()))
    p = math.ceil((sum(R)+m)/n)
    if p < max(R):
           p = max(R)
    print(p,max(R)+m)