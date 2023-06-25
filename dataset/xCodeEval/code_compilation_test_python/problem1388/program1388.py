def program1388():
    digits = input().strip()
    heads = {}
    for digit in digits:
        for (hundred, tens) in heads.iteritems():
             for ten in tens:
                if int(hundred + ten + digit) % 8 == 0:
                    print 'YES'
                    print hundred + ten + digit
                    exit(0)
            if digit not in tens:
                heads[hundred].append(digit)
        if digit != '0' and digit not in heads:
            heads[digit] = []
    print 'NO'