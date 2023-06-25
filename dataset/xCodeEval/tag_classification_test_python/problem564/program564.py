def program564():
    n = int(input())
    a = [int(x) for x in input().split()]
    init = sum(a)
    m = max(a)
    arr = [(m - x) for x in a]
    summa = sum(arr)
    while (summa <= init):
    	m += 1
    	summa += n
    print(m)