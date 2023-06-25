def program2705():
    n = int(input())
    
    a = list(map(int, input().split()))
    print(max(max(b), sum(b)*2//n+1