def maxPies(i):
        if i==n:
            return pies[n-1]
        else:
            sum = 0
            j=i-1
            while(j<n):
                sum = sum + pies[j]
                j+=1
    
            return max(maxPies(i+1), pies_sum[i-1]-maxPies(i+1))
    
    n = input()
    pies = [0]*n
    pies_sum = [0]*n
    pies= map(int, input().split())
    pies_sum[n-1] = pies[n-1]
    j=n-2
    while(j>=0):
        pies_sum[j] = pies_sum[j+1] + pies[j]
        j-=1
    
    answer = maxPies(1)
    print("{0} {1}".format(pies_sum[0] - answer, answer))