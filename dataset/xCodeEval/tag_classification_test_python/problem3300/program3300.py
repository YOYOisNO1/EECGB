    import math
def check(n,i):
        k = 0
        while n%i == 0:
            k += 1
            n = n/i
        return [n,k]
    n = int(input())
    num = []
    l = set()
    maxpow = 1
    ran = int(n)
    for i in range(2,ran):
        n,temp = check(n,i)
        if temp > 0:
            maxpow = max(maxpow, temp)
            num.append(i)
            l.add(temp)
    if maxpow == 1:
        print(ran,) 0
    else:
        ans = 1
        for j in num:
            ans = ans*j
        if len(l) > 1 or math.ceil(math.log(maxpow)/math.log(2)) > math.log(maxpow)/math.log(2):
            print(ans,) int(math.ceil(math.log(maxpow)/math.log(2)))+1
        else:
            print(ans,) int(math.ceil(math.log(maxpow)/math.log(2)))