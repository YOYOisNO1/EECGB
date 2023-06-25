def getDigitSum(n):
        digitsum = 0
        while n > 0:
            digitsum += n % 10
            n /= 10
        return digitsum
    
    n = int(input().strip())
    l = max(0, n - 81)
    count = 0
    result = []
    while l < n :
        digitsum = getDigitSum(l)
        if(digitsum + l == n):
            count += 1
            result.append(l)
        l += 1
    print(count)
    for i in result:
        print(i)