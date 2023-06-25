def program1415():
    a = list(map(int, input().split()))
    n = a[0]
    b = [[0 for i in range(2)] for j in range(n)]
    sum_total = a[1]
    
    for i in range(n):
        b[i] = list(map(int, input().split()))
    
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += b[i][0]
        sum2 += b[i][1]
    temp = []
    str = ''
    if sum_total > sum2 or sum_total < sum1:
        print('NO')
    elif sum1 == 0:
        print('YES')
        for i in range(n):
    
    
    else:
        print('YES')
        for i in range(n):
            if sum_total >= sum1 and sum_total >= b[i][1] and b[i][1] != 0:
                str += f'{b[i][1]}'
                str += ' '
                sum_total -= b[i][1]
                sum1 -= b[i][1]
            elif b[i][1] == 0:
                str += f'{0}'
                str += ' '
            elif sum_total >= sum1:
                str += f'{sum_total}'
                str += ' '
                sum_total -= sum_total
                sum1 -= sum_total
            else:
                str += f'{b[i][0]}'
                str += ' '
                sum_total -= b[i][0]
                sum1 -= b[i][0]
    
        print(str[:-1])
    
    