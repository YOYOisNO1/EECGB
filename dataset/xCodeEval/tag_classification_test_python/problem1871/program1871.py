def program1871():
    n = int(input())
    p = list(map(int, input().strip().split()))
    
    ans = []
    
    for k in range(n):
        sum = 0
        x = k + 1
    
        for i in range(1, len(p)):
            f = i + 1
            sum += p[i] * (abs(f-x)+abs(f-1)+abs(x-1)) * 2
    
        ans.append(sum)
    
    print(min(ans))