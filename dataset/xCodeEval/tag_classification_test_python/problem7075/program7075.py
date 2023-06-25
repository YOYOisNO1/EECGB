def program7075():
    c, d = map(int, input().split())
    n, m = map(int, input().split())
    k = int(input())
    
    problems = 0
    people = n * m - k
    
    while people > 0:
        if (d < float(c) / n) or (d < float(c) / people):
            people -= 1
            problems += d
        else:
            people -= n
            problems += c
    print(problems)