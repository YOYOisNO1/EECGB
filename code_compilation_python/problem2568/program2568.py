def program2568():
    n = int(input())
    s = map(int,input().split())
    s = list(s)
    import math
    chet = 0
    nechet = 0
    posled = 0
    for i in range(len(s)):         #Определение заданных четных и нечетных
        if s[i] == 0:          # и формирование списка из 0,1,2 
            continue
        elif s[i] % 2 == 0:
            chet = chet + 1
            posled = 2
            s[i] = 2
        else:
            nechet = nechet + 1
            posled = 1
            s[i] = 1
    
    chet = len(s)/2 - chet                  #Количество оставшихся четных и нечетных 
    nechet = math.ceil(len(s)/2) - nechet
    
    s.append(posled)
    
    while chet + nechet > 0:
        for i in range(len(s)-1):
            if s[i] == 0:           #Формирование конечного списка из 1 и 2
                
                if s[i+1] == 2:
                    if chet > 0:
                        s[i] = 2
                        chet = chet - 1
                    else:
                        s[i] = 1
                        nechet = nechet - 1
                    
                elif s[i+1] == 1:
                    if nechet > 0:
                        s[i] = 1
                        nechet = nechet - 1
                    else:
                        s[i] = 2
                        chet = chet - 1
                
    
    s = s[:-1]
    otvet = 0                    # Определение ответа  
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            i = i + 1
        else:
            otvet = otvet + 1
            i = i + 1
        
    print(otvet)