def main():
        k=[]
        m=[]
        for i in xrange(1,100001):
            r=str(i)
            k.append(r+r[::-1])
        m.append(long(k[0]))
        for i in xrange(1,100000):
            m.append(m[i-1]+long(k[i]))
        n,l=map(long,input().split())
        print(m[n-1]%l)
        
    main() 