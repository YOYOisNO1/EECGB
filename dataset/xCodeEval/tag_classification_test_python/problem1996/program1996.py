def sums(n,k, d,  dic):
        count = 0
        limited_count = 0
        for i in range(1, k+1):
            if n - i == 0:
                count += 1
                if n >= d:
                    limited_count += 1
            elif n - i < 0:
                pass
            else:
                count += dic[n-i][0]
                if i >= d:
                    limited_count += dic[n-i][0]
                else:
                    limited_count += dic[n-i][1]
        return (count%(10**9+7), limited_count%(10**9+7))
    
def tree(n,k,d):
        dic = {}
        for i in range(1,n+1):
            dic[i] = sums(i,k,d, dic)
        return dic[n][1]
    
    
    lst = list(map(lambda elem: int(elem), input().split(" ")))
    print(tree(lst[0], lst[1], lst[2]))