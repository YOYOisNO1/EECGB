def can_be_weigthed(m, w, i):
        if i == 0:
            return m == 1
        else:
            if m == 1:
                return True
            if m%w in {0, 1, w-1}:
                return can_be_weigthed(m//w + (m%w == w-1), w, i-1)
            else:
                return False
    
    w, m = [int(x) for x in input().split()]
    answer = {True: 'YES', False: 'NO'}
    print(answer[can_be_weigthed(m, w, 100)])