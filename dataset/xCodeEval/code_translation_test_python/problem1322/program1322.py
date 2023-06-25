    import sys
def device(n,m):
        if m < n :
            return n-m
        elif m == n :
            return 0
        else :
            dic = {n:0}
            level = 1
            frontier = [n]
            current = 1000000000
            while frontier :
                new = []
                l = len(frontier)
                for i in range(0,l) :
                    num = frontier.pop()
                    num1 = num - 1
                    if num1 == m :
                        return level
                    if num1 not in dic :
                        dic[num1] = 0
                        new.append(num1)
                    
                    
                    num2 = num*2
                    if num2 == m :
                        return level
                    elif num2 > m :
                        current = min(current, num2-m + level)
                    elif num2 not in dic :
                        dic[num2] = 0
                        new.append(num2)
                frontier = new
                level = level + 1
                if level >=current :
                    return current
    
    
        
    n,m = map(int,sys.stdin.readline().split())
    print(device(n,m))
    