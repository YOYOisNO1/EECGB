    k = int(input())
    data = [int(x) for x in input().strip().split(' ')]
    
    
def calc(k, list):
        summ = 0
        i = 0
        while summ < k:
            if not list:
                i = -1
                break
            maks = max(list)
            summ += maks
            list.remove(maks)
            i += 1
        print(i)
    
    #calc(5, [1,1,1,1,2,2,3,2,2,1,1,1])
    #calc(23, [23])
    #calc(11, [1,1,4,1,1,5,1,1,4,1,1,1])
    calc(k, data)