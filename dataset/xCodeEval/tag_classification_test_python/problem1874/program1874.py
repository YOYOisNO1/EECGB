def ans(a,n):
        ans = 10**9
        for pos in range(n):
            tmp = 0
            for rest in range(n):
                tmp += ((abs(pos-rest)+rest+pos)*a[rest])*2
            if tmp < ans:
                ans = tmp
        return ans
    
    n = int(input())
    arr = [int(i) for i in input().split()]
    
    print(ans(arr,n))