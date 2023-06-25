    p = input()
    p = map(int, p.split(' '))
    k,m = p[0],p[1]
    s = input()
    
def main (k,m,s):
        p = [0]*(k+1)
    
        for i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            if i in s:
                #print(i,) s.index(i), s.rindex(i)
                p[s.index(i)]+=1
                p[s.rindex(i)+1]-=1
        #print(pos)
    
        b = 0
        for i in range(k):
            b+=p[i]
            if b>m: return 'YES'
        return 'NO'
    
    print(main(k,m,s))