    import string
    
def nok(t):
        ans = 1
        md = [1, 1, 1]
        minus = True
        i = 2
        j = 1
        d = [t[0] % i, t[1] % i, t[2] % i]
        while t[0] != 0 or t[1] != 0 or t[2] != 0:
            
            if d[0] == 0 and d[1] == 0 and d[2] == 0:
                ans *= i
                t[0] /= i
                t[1] /= i
                t[2] /= i
                d = [t[0] % i, t[1] % i, t[2] % i]
                md[0] *= i
                md[1] *= i
                md[2] *= i
            elif d[0] == 0 and d[1] == 0:
                ans *= i
                t[0] /= i
                t[1] /= i
                d[:2] = [t[0] % i, t[1] % i]
                md[0] /= i
                md[1] /= i
            elif d[0] == 0 and d[2] == 0:
                ans *= i
                t[0] /= i
                t[2] /= i
                d = [t[0] % i, d[1], t[2] % i]           
                md[0] *= i
                md[2] *= i
            elif d[2] == 0 and d[1] == 0:
                ans *= i
                t[2] /= i
                t[1] /= i
                d[1:] = [t[1] % i, t[2] % i]           
                md[2] *= i
                md[1] *= i
            elif d[0] == 0:
                ans *= i
                t[0] /=i
                d[0] = t[0] % i
                md[0] *= i               
            elif d[1] == 0:
                ans *= i
                t[1] /= i
                d[1] = t[1] % i
                md[1] *= i
            elif d[2] == 0:
                ans *= i
                t[2] /= i
                d[2] = t[2] % i
                md[2] *= i
            else:
                if t.count(1) == 3:
                    break
                elif t.count(1) == 2:
                    ans *= max(t[0], t[1], t[2])
                    break
                while d.count(0) < 1:
                    if i >= 3:
                        if minus:
                            i = j*6 - 1
                            minus = False
                        else:
                            i = j*6 + 1
                            j += 1
                            minus = True
                    else:
                        i += 1
                    ii = 2 * i
                    if t[0] < ii:
                        ans *= t[0]
                        if t[1] % t[0] == 0:
                            t[1] /= t[0]
                        if t[2] % t[0] == 0:
                            t[2] /= t[0]
                        t[0] = 1
                        if t.count(1) == 3:
                            break
                        elif t.count(1) == 2:
                            ans *= max(t[1], t[2])
                            break
                    if t[1] < ii:
                        ans *= t[1]
                        t[1] = 1
                        if t[0] % t[1] == 0:
                            t[0] /= t[1]
                        if t[2] % t[1] == 0:
                            t[2] /= t[1]
                        t[1] = 1
                        if t.count(1) == 3:
                            break
                        elif t.count(1) == 2:
                            ans *= max(t[0], t[2])
                            break
                    if t[2] < ii:
                        ans *= t[2]
                        t[2] = 1
                        if t[1] % t[2] == 0:
                            t[1] /= t[2]
                        if t[0] % t[2] == 0:
                            t[0] /= t[2]
                        t[2] = 1
                        if t.count(1) == 3:
                            break
                        elif t.count(1) == 2:
                            ans *= max(t[1], t[0])
                            break
                        
                    d = [t[0] % i, t[1] % i, t[2] % i]
                
                else:
                    continue
                break
                    
        return ans
    
    
    maxx = int(input().rstrip('\n'))
    
    if maxx == 2:
        print(2)
    elif maxx == 1:
        print(1)
    else :
        i = 2
        while maxx % i == 0:
            i += 1
        
        a = maxx
        b = maxx - 1
        c = maxx - 2
        ans = nok([a, b, c])
        
        c -= 1
        while c >= maxx - i:
            while b > c:
                while a > b:
                    ans2 = nok([a, b, c])
                    ans = max(ans, ans2)
                    a -= 1
                b -= 1
                a = maxx
            c -= 1
            b = maxx - 1
            
        print(ans)
            
    
            