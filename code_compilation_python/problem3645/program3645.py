    import sys
    import math
    import string
    from collections import deque
    
    # Function #
def read_int() :
        temp = input().split();
        return map(int, temp);
    
def read_str() :
        temp = input().split();
        return temp;
    
def write(output) :
        sys.stdout.write(output);
        
def writeln(output) :
        sys.stdout.write(str(output)+'\n');
    # Class #
    
    
    INF = 9123456789123456789
    # Main Entry #
    
    # Inner Function #
def len_int(now) :
        temp = set();
        while now > 0 :
            temp.add(now%10);
            now /= 10;
        return len(temp);
        pass
        
    ans = 0;
def dfs(now, limit) :
        global ans;
        if now > limit :
            return;
        if now!=0 :
            #print "DEBUG", now;
            ans += 1;
        for ii in xrange(0, 10) :
            if (now*10+ii!=0) and len_int(now*10+ii) <= 2 :
                
                dfs(now*10+ii, limit);
            pass
        pass
    
    if __name__ == '__main__':
        
        tc = read_int()[0];
        dfs(0, tc);
        print ans;
        
        pass
    # End Here #
        