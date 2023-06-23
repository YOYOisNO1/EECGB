    import math
    
def num_digits(num):
        return len(str(num))
    
def nine_count(num):
        numstr = list(str(num))[::-1]
        count = 0
        for n in numstr:
            if n != '9':
                break
            count += 1
        return count
    
    p, d = map(int, input().split())
    
    reduce = int(math.pow(10, num_digits(d)-1))
    
    length = num_digits(d)
    while length > 0:
        last_digits = int(str("".join(list(str(p))[len(str(p))-length:])))
        temp = p - last_digits
        temp = temp - 1
        if temp >= p-d:
            if nine_count(p) >= nine_count(temp):
                ans = p
            else:
                ans = temp
            break
        length -= 1
    print ans