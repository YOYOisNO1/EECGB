def program4720():
    n = int(input())
    min1, max1 = [int(i) for i in input().split()]
    min2, max2 = [int(i) for i in input().split()]
    min3, max3 = [int(i) for i in input().split()]
    count1, count2, count3 = 0, 0, 0
    n -= (min1 + min2 + min3)
    count1 = min1
    count2 = min2
    count3 = min3
    max1 -= min1
    max2 -= min2
    max3 -= min3
    if n > 0 and n >= max1:
        count1 += max1
        n -= max1
        if n > 0 and n >= max2:
            count2 += max2
            n -= max2
            if n > 0:
                count3 += n
        elif n > 0 and n < max2:
            count2 += n
            n = 0
    elif n > 0 and n < max1:
        count1 += n
        n = 0
    print(count1, count2, count3, sep = ' ')