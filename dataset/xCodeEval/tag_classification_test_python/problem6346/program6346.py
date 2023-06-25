def program6346():
    import math
    res = 0
    a,b,c = map(int,input().split())
    arr = [0]*1000001
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                num = i*j*k
                count = 0
                if arr[num]:
                    res += arr[num]
                else:
                    for l in range(1,math.floor((num)**(1/2))+1):
                        if num % l == 0:
                            if num // l != l:
                                count += 2
                            else:
                                count += 1
                    res += count
                    arr[num] = count
    print(res%(2**30))