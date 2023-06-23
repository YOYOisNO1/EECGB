def s(a,b,c):
        l = []
        for i in range(1,82):
            v = b*i**a+c
            if v > 1000000000:
                break
            vcopy = v
            val = 0
            while v > 0:
                val += v%10
                v//=10
            if val == i:
                l.append(vcopy)
        print(len(l))
        for i in l:
            print(i,end=' ')
    
    a,b,c = map(int, input().spli