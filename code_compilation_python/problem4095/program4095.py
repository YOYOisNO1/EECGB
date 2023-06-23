    import sys
    
def sum(i):
        if i%2 == 0:
            return (i+1)*(i/2)
        else:
            return (i+1)*((i-1)/2)+((i+1)/2)
    
def switched(i,m,k):
        if i <= min(m,k):
            return sum(i)
        elif i>min(m,k) and i<max(m,k):
            return sum(min(m,k)) + (min(m,k)*(i-min(m,k)))
        elif i>=max(m,k) and i < max(m,k)+min(m,k):
            tmp = i - max(m,k)+1
            return sum(min(m,k)) + (min(m,k)*(max(m,k)-min(m,k)-1)) + sum(min(m,k))-sum(min(m,k)-tmp)
        else:
            return m*k
            
    if __name__ == '__main__':
        n,x,y,c = map(int,input().split())
        if c == 1:
            print 0
        else:
            i=1
            num = 1
            while num < c:
                num = switched(i,x,y-1) + switched(i,n-x,y) + switched(i,n-x+1,n-y) + switched(i,x-1,n-y+1)
                i = i + 1
            print i - 1