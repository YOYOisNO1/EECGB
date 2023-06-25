def program643():
    import sys
    n = int(input())
    
    if n % 25 == 0:
        print(0)
    else:
        tmp = n
        digits = [0]*10
        while (tmp):
            digits[tmp % 10] += 1
            tmp //= 10
    
        s = str(n)
        length = len(s)
        leading_zero_inc = 0
        for i in range(1, length):
            if s[i] != '0':
                leading_zero_inc = i
                break
        # print(leading_zero_inc)
        ans = sys.maxsize
    
        if digits[0] >= 2:
            i = s.rfind('0')
            j = s.rfind('0', 0, i)
            i = length-1-i
            j = length-2-j
            # print(i,j)
            ans = min(ans, i+j)
    
        if digits[2] >= 1 and digits[5] >= 1:
            i = s.rfind('2')
            j = s.rfind('5')
            inc = False
            if j < i: inc = True
            if i == 0:
                i = length-3+leading_zero_inc
            else:
                i = length-2-i
            if j == 0:
                j = length-2+leading_zero_inc
            else:
                j = length-1-j
            # print(i,j)
            ans = min(ans, i+j+inc)
    
        if digits[5] >= 1 and digits[0] >= 1:
            i = s.rfind('5')
            j = s.rfind('0')
            inc = False
            if j < i: inc = True
    
            if i == 0 and j != 1:
                i = length-3+leading_zero_inc
            else:
                i = length-2-i
            j = length-1-j
            # print(i,j)
            ans = min(ans, i+j+inc)
    
        if digits[7] >= 1 and digits[5] >= 1:
            i = s.rfind('7')
            j = s.rfind('5')
            inc = False
            if j < i: inc = True
    
            if i == 0:
                i = length-3+leading_zero_inc
            else:
                i = length-2-i
            if j == 0:
                j = length-2+leading_zero_inc
            else:
                j = length-1-j
            # print(i,j)
            ans = min(ans, i+j+inc)
    
        if ans == sys.maxsize:
            ans = -1
        print(ans)
    
    