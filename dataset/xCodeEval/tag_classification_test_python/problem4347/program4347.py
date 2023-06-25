def program4347():
    k = int(input())
    
    lowest_ranked_competitor = max(list(map(int, input().split())))
    
    print(lowest_ranked_competitor - 25 if lowest_ranked_competitor - 25 > 0 else 0)