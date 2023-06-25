def program2152():
    p = input()
    if p == p[::-1] or len(p) == 1:
        print("YES")
    else:
        if p[0] != p[len(p) - 1] and '0' not in [p[0], p[len(p) - 1]]:
            print("NO")
        else:
            cl, cr = '', ''
            for i in p:
                if i == '0':
                    cl+='0'
                else:
                    break
            for i in p[::-1]:
                if i == '0':
                    cr+='0'
                else:
                    break
            if cl == cr and p != p[::-1]:
                print("NO)
            else:
                if len(cl) > len(cr):
                    p += ('0' * (len(cl) - len(cr)))
                    if p == p[::-1]:
                        print("YES")
                    else:
                        print("NO")
                else:    
                    p = ('0' * (len(cr) - len(cl))) + p
                    if p == p[::-1]:
                        print("YES")
                    else:
                        print("NO")