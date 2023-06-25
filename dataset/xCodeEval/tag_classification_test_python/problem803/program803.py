def program803():
    
    hh, mm = map(int, input().split(':'))
    x = int(input())
    mm += hh * 60
    
    mm += x
    mm %= 1440
    
    hh = mm // 60
    if hh < 10:
    	hh = '0' + str(hh)
    
    mm = mm % 60
    if mm < 10:
    	mm = '0' + str(mm)
    
    ans = [hh, ':', mm]
    print(*ans, sep = '')