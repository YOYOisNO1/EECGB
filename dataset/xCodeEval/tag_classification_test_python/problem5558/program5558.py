def program5558():
    
    
    if __name__=='__main__':
        inp = input()
        arr = inp.split(" ")
        a = int(arr[0])
        b = int(arr[1])
        inp = input()
        locs = set([])
        x = 0
        y = 0
        locs.add((x,y))
        for c in inp:
            if c=='U':
                y+=1
            if c=='D':
                y-=1
            if c=='L':
                x-=1
            if c=='R':
                x+=1
            locs.add((x,y))
        ans = "No"
        if (a,b) in locs:
            ans = "Yes"
        elif x == 0 and y==0:
            ans = "No"
        elif x==0:
            for t in locs:
                if t[0]==a:
                    ver = b - t[1]
                    if ver/abs(ver)==y/abs(y):
                        toC=ver//y
                        if toC*y==ver:
                            ans = "Yes"
                            break
        elif y==0:
            for t in locs:
                if t[1]==b:
                    hor = a - t[0]
                    if hor/abs(hor)==x/abs(x):
                        toC=abs(hor)//abs(x)
                        if toC*x==hor:
                            ans = "Yes"
                            break
        else:
            for t in locs:
                hor = a - t[0]
                ver = b - t[1]
                if hor!=0 and ver!=0 and hor/abs(hor)==x/abs(x) and ver/abs(ver)==y/abs(y):
                    up = abs(ver)//abs(y)
                    rt = abs(hor)//abs(x)
                    if up*y==ver and rt*x==hor and up==rt:
                        ans="Yes"
                        break
        print(ans)
                
        