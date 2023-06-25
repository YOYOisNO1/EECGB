    n = input()
    lengt = len(str(n))
    d = max ( int(n) - int(9*lengt), 0 )
    j = 0
    r = []
def sum_digits(a):
        return sum(list(map(int, str(a))))
    if ( n == 1 or n == 3 or n == 5 or n == 7 or n == 9):
        print ('0')
    else:    
        for i in range (d, n):
            if ( (i+ sum_digits(i)) == n):
                j += 1
                r.append(i)
        print j
        for k in r:
            print (k)