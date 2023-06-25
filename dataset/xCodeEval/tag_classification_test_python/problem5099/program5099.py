def program5099():
    a ,b = input().split('|')
    c = input()
    maxx = max(len(a),len(b))
    minn = min(len(a),len(b))
    s = int(maxx - minn)
    if (len(c)<s):
        print('Impossible')
    elif ( (len(c)-s )%2 !=0):
        print('Impossible')
    else :
        i = 0
        if (len(a)==len(b)):
            while (i != len(c)):
                a += c[i];i += 1
                b += c[i];i += 1
        if (len(a)>len(b)):
            while(len(a)!=len(b)):
                b+=c[i];i+=1
            while(i!=len(c)):
                a+=c[i];i+=1
                b+=c[i];i+=1
        if (len(a)<len(b)):
            while (len(a) != len(b)):
                a += c[i];i += 1
            while (i != len(c)):
                a += c[i]; i += 1
                b += c[i]; i += 1
        print(a+'|'+b)