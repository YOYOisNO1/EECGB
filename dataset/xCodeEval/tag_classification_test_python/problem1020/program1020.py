def find_min(min_wins, a1, a2, a3, b1, b2, b3):
        #print(min_wins,a1,a2,a3,b1,b2,b3)
        if a1 != 0 and b3 != 0 and b1 != 0:
            if a1 > b3 and a1 > b1:
                return min( find_min(min_wins-b3, a1-b3, a2, a3, b1, b2, 0), find_min(min_wins-b1, a1-b1, a2, a3, 0, b2, b3))
            elif a1 > b3 and a1 < b1:
                return min( find_min(min_wins-b3, a1-b3, a2, a3, b1, b2, 0), find_min(min_wins-a1, 0, a2, a3, b1-a1, b2, b3))
            elif a1 < b3 and a1 > b1:
                return min( find_min(min_wins-a1, 0, a2, a3, b1, b2, b3-a1), find_min(min_wins-b1, a1-b1, a2, a3, 0, b2, b3))
            else:
                return min( find_min(min_wins-a1, 0, a2, a3, b1, b2, b3-a1), find_min(min_wins-a1, 0, a2, a3, b1-a1, b2, b3))
        elif a1 != 0 and b1 != 0:
            if a1 > b1:
                return find_min(min_wins-b1, a1-b1, a2, a3, 0, b2, b3)
            else:
                return find_min(min_wins-a1, 0, a2, a3, b1-a1, b2, b3)
        elif a1 != 0 and b3 != 0:
            if a1 > b3:
                return find_min(min_wins-b3, a1-b3, a2, a3, b1, b2, 0)
            else:
                return find_min(min_wins-a1, 0, a2, a3, b1, b2, b3-a1)
        
        if a2 != 0 and b1 != 0 and b2 != 0:
            if a2 > b1 and a2 > b2:
                return min( find_min(min_wins-b1, a1, a2-b1, a3, 0, b2, b3), find_min(min_wins-b2, a1, a2-b2, a3, b1, 0, b3))
            elif a2 > b1 and a2 < b2:
                return min( find_min(min_wins-b1, a1, a2-b1, a3, 0, b2, b3), find_min(min_wins-a2, a1, 0, a3, b1, b2-a2, b3))
            elif a2 < b1 and a2 > b2:
                return min( find_min(min_wins-a2, a1, 0, a3, b1-a2, b2, b3), find_min(min_wins-b2, a1, a2-b2, a3, b1, 0, b3))
            else:
                return min( find_min(min_wins-a2, a1, 0, a3, b1-a2, b2, b3), find_min(min_wins-a2, a1, 0, a3, b1, b2-a2, b3))
        elif a2 != 0 and b2 != 0:
            if a2 > b2:
                return find_min(min_wins-b2, a1, a2-b2, a3, b1, 0, b3)
            else:
                return find_min(min_wins-a2, a1, 0, a3, b1, b2-a2, b3)
        elif a2 != 0 and b1 != 0:
            if a2 > b1:
                return find_min(min_wins-b1, a1, a2-b1, a3, 0, b2, b3)
            else:
                return find_min(min_wins-a2, a1, 0, a3, b1-a2, b2, b3)
        
        if a3 != 0 and b2 != 0 and b3 != 0:
            if a3 > b2 and a3 > b3:
                return min( find_min(min_wins-b2, a1, a2, a3-b2, b1, 0, b3), find_min(min_wins-b3, a1, a2, a3-b3, b1, b2, 0))
            elif a3 > b2 and a3 < b3:
                return min( find_min(min_wins-b2, a1, a2, a3-b2, b1, 0, b3), find_min(min_wins-a3, a1, a2, 0, b1, b2, b3-a3))
            elif a3 < b2 and a3 > b3:
                return min( find_min(min_wins-a3, a1, a2, 0, b1, b2-a3, b3), find_min(min_wins-b3, a1, a2, a3-b3, b1, b2, 0))
            else:
                return min( find_min(min_wins-a3, a1, a2, 0, b1, b2-a3, b3), find_min(min_wins-a3, a1, a2, 0, b1, b2, b3-a3))
        elif a3 != 0 and b3 != 0:
            if a3 > b3:
                return find_min(min_wins-b3, a1, a2, a3-b3, b1, b2, 0)
            else:
                return find_min(min_wins-a3, a1, a2, 0, b1, b2, b3-a3)
        elif a3 != 0 and b2 != 0:
            if a3 > b2:
                return find_min(min_wins-b2, a1, a2, a3-b2, b1, 0, b3)
            else:
                return find_min(min_wins-a3, a1, a2, 0, b1, 0, b3)
        
        return min_wins
    
    n = int(input())
    
    a1, a2, a3 = list(map(int, input().split()))
    b1, b2, b3 = list(map(int, input().split()))
    
    max_wins = min(a1, b2) + min(a2, b3) + min(a3, b1)
    min_wins = min( find_min(n, a1, a2, a3, b1, b2, b3), find_min(n, a2, a3, a1, b2, b3, b1), find_min(n, a3, a1, a2, b3, b1, b2) )
    
    
    print(min_wins, max_wins)