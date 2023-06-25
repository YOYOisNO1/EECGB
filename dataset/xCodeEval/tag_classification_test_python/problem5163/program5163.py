def getLength(num):
        if num <= 1:
            return 1
        return getLength(int(num/2)) * 2 + 1
    
def getOne(num, l ,r, L, R):
        if num == 0 or l > R or r < L:
            return 0
        if num == 1:
            return 1
        mid =  int(L + getLength(int(num / 2)))
        return getOne(int(num / 2), l, r, L, mid -1) + getOne(int(num % 2), l, r, mid, mid) + getOne(int(num / 2), l, r, mid + 1, R)
    ip = input()
    number = ip.split()
    num = int(number[0])
    l = int(number[1])
    r = int(number[2])
    length = getLength(num)
    res = getOne(num, l, r, 1, length)
    print(res)