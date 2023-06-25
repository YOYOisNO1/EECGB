    '''
    Created on 01-Jul-2017
    
    @author: kandarp
    '''
    import sys
def check(x,a):
        b =[]
        ans = True;
        for i in xrange(0,x):
            b.append([]);
        for i in xrange(0,len(a)):
            b[i%x].append(a[i])
        for i in xrange(0,x):
            for j in xrange(0,len(b[i])):
                if b[i][j] < (len(b[i]) - (j+1)):
                    ans = False;
                    return ans;    
        return ans;
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    if n==1:
        print(1)
        sys.exit(0);
    current_watch = 0;
    l=0;
    r=len(a);
    ans =1;
    while(r - l >1):
        mid = int((l + r)/2);
        if(check(mid, a)):
            r = mid;
        else:
            l = mid;
            
    if(check(l,a)):
        print(l);
    else:        
        print(r);