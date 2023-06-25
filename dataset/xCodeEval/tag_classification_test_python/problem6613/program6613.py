    #coding=utf-8
    
def test():
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
    
        total = n * 8
        place = 0
        sum = 0
        flag = 0
        for x in a:
            sum += x
            if x%2 is 1:
                place += 1
            else:
                flag += 1
        if sum == total:
            if place!=0 or (flag%4==0 and n*4==k):
                print("NO")
            else:
                print("YES")
        else:
            if (sum + place) > total or (n*4==k and (flag//4)==place ):
                print("NO")
            else:
                print("YES")
    
    
    test()