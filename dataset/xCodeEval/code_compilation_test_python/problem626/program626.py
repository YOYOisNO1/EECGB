def program626():
    stroka = input()
    k = int(input())
    n1 = stroka.count('*')
    n2 = stroka.count('?')
    t = 0
    p = ''
    if n1 > 0 and n2 > 0:
        for i in range(len(stroka)):
    
            if stroka[i+t]=='?'and (len(stroka)-stroka.count('?')-stroka.count('*')-stroka.count('!'))>k:
                stroka = stroka[:i+t-1]+'!!'+stroka[i+t+1:]
            elif  stroka[i+t]=='?'and (len(stroka)-stroka.count('?')-stroka.count('*')-stroka.count('!'))<=k:
                stroka = stroka[:i+t]+'!'+stroka[i+t+1:]
            elif stroka[i+t] =='*' and (len(stroka)-stroka.count('?')-stroka.count('*')-stroka.count('!'))>k:
                stroka = stroka[:i+t - 1] + '!!' + stroka[i+t + 1:]
            elif stroka[i+t] =='*' and (len(stroka)-stroka.count('?')-stroka.count('*')-stroka.count('!'))==k:
                stroka = stroka[:i +t] + '!'  + stroka[i +t+ 1:]
            elif stroka[i+t] =='*' and (len(stroka)-stroka.count('?')-stroka.count('*')-stroka.count('!'))<k:
                y = abs((len(stroka)-stroka.count('?')-stroka.count('*')-stroka.count('!'))-k)
                stroka = stroka[:i+t] + stroka[i+t-1]*y + stroka[i+t + 1:]
                t+=y-1
    elif n1 > 0 and n2 ==0:
        for i in range(len(stroka)):
            print(stroka)        if stroka[i+t] == '*' and (len(stroka) - stroka.count('*')-stroka.count('!')) > k:
                stroka = stroka[:i+t - 1] + '!!' + stroka[i+t + 1:]
            elif stroka[i+t] == '*' and (len(stroka)  - stroka.count('*')-stroka.count('!')) == k:
                stroka = stroka[:i+t] + '!' + stroka[i +t+ 1:]
            elif stroka[i+t] == '*' and (len(stroka)  - stroka.count('*')-stroka.count('!')) < k:
                y = abs((len(stroka)  - stroka.count('*')-stroka.count('!')) - k)
                stroka = stroka[:i + t] + stroka[i + t - 1] * y + stroka[i + t + 1:]
                t += y-1
    elif n1==0 and n2 > 0:
        for i in range(len(stroka)):
            if stroka[i] == '?' and (len(stroka) - stroka.count('?') -stroka.count('!')) > k:
                stroka = stroka[:i - 1] + '!!' + stroka[i + 1:]
            elif stroka[i] == '?' and (len(stroka) - stroka.count('?') -stroka.count('!')) <= k:
                stroka = stroka[:i] + '!' + stroka[i + 1:]
    for i in range(len(stroka)):
        if stroka[i]!='!':
            p += stroka[i]
    
    
    if len(p)==k:
        print(p)
    else:
        print('Impossible')