def program2254():
    n, m = map(int, input().split())
    count = 0
    factorial = [1]
    for i in range(n-1):
        factorial.append((i+2)*factorial[i])
    
    for i in range(n):
        x = i+1
        count += (n-i)*factorial[i]*factorial[n-i-1]
    
    print(count%m)