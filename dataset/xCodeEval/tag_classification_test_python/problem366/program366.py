    from __future__ import division;
    from bisect import *;
    from fractions import Fraction;
    import sys;
    import math;
    import io;
    
    INF = 987654321987654321987654321;
    
def readint(delimiter=' ') :
    	return map(int, input().split(delimiter));
    
def readstr() :
    	return input().split();
    
def readfloat() :
    	return map(float, input().split());
    
def index(a, x):
        'Locate the leftmost value exactly equal to x'
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        raise ValueError
    
def find_lt(a, x):
        'Find rightmost value less than x'
        i = bisect_left(a, x)
        if i:
            return a[i-1]
        raise ValueError
    
def find_le(a, x):
        'Find rightmost value less than or equal to x'
        i = bisect_right(a, x)
        if i:
            return a[i-1]
        raise ValueError
    
def find_gt(a, x):
        'Find leftmost value greater than x'
        i = bisect_right(a, x)
        if i != len(a):
            return a[i]
        raise ValueError
    
def find_ge(a, x):
        'Find leftmost item greater than or equal to x'
        i = bisect_left(a, x)
        if i != len(a):
            return a[i]
        raise ValueError
    
    
def bin_search(a, x, left, right) :
    
        while left<=right :
            mid = (left + right)//2;
            
            if a[mid] == x :
                return mid;
            elif a[mid] < x :
                left = mid + 1; 
            elif a[mid] > x :
                right = mid - 1;
                           
            pass
        
        return -1;
        pass
    
    if __name__ == '__main__':
    	
        mat = [[0 for _ in xrange(4)] for _ in xrange(4)];
        
        for ii in xrange(4) :
            now = input();
            for jj in xrange(4) :
                mat[ii][jj] = 1 if now[jj] == '#' else 0;
    
        
        # check #
        valid = False;
        for ii in xrange(3) :
            for jj in xrange(3) :            
                total = mat[ii][jj] + mat[ii+1][jj] + mat[ii][jj+1] + mat[ii+1][jj+1];
                #print(total,) ii, jj;
                if total >= 3 or total <= 1:
                    valid = True;
                    break;
            if valid :
                break;
        print("YES") if valid else "NO";
    
        pass