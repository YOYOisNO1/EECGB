def get_digit(digit):
        if digit.isdigit():
            return ord(digit) - ord('0')
        else:
            return ord(digit) - ord('A') + 10
    
def to_int(word, base):
        pow = 1
        res = 0
        for digit in reversed(word):
            res += get_digit(digit) * pow
            pow *= base
        return res
    
    hours, minutes = input().split(':')
    min_radix = max(max(hours), max(minutes))
    min_radix = get_digit(min_radix) + 1
    while hours.startswith('0'):
        hours = hours[1:]
    while minutes.startswith('0'):
        minutes = minutes[1:]
    
    if len(hours) < 1 and len(minutes) <= 1:
        print(-1)
    elif len(hours) == 1 and len(minutes) <= 1 and get_digit(hours) <= 23:
        print(-1)
    else:
        max_radix = min_radix
        while True:
            h, m = to_int(hours, max_radix), to_int(minutes, max_radix)
            if h > 23 or m > 59:
                break
            max_radix += 1
        if max_radix > min_radix:
            for rad in xrange(min_radix, max_radix):
                print(rad,)
        else:
            print(0)