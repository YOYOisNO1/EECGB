    from __future__ import division;
    from bisect import *;
    from fractions import Fraction;
    import sys;
    import math;
    import io;
    
    INF = 987654321987654321987654321;
    
def readint() :
    	return map(int, input().split());
    
def readstr() :
    	return input().split();
    
def readfloat() :
    	return map(float, input().split());
    
def bin_search(left, right, denominator, target) :
    	
    	minim_nominator = INF;
    	minim_now = INF;
    	while (left <= right) :
    		mid = (left + right)//2;
    		now = mid / denominator;
    		now = round(now, 8);
    		if abs(now - target) == minim_now and minim_now > now :
    			minim_now = abs(now - target);
    			minim_nominator = mid;
    		elif abs(now-target) < minim_now :
    			minim_now = abs(now - target);
    			minim_nominator = mid;
    
    		if (now < target) :
    			left = mid + 1;
    		elif (now > target) :
    			right = mid - 1;
    		else :
    			return mid;
    		pass
    	return minim_nominator;
    
    if __name__ == '__main__':
    	
    	x, y, n = readint();
    	'''
    	ori = x / y;
    	ori = round(ori, 8);
    	res = INF;
    	resx = -1;
    	resy = -1;
    	for ii in xrange(1, min(y, n)+1, 1) :
    		# binary search for the nominator #
    		now = bin_search(0, x, ii, ori);
    		nowdiv = now / ii;
    		nowdiv = round(nowdiv, 8);
    		nowdiff = abs(ori - nowdiv);
    		print(nowdiv,) nowdiff, now, ii;
    
    		if (nowdiff < res) :
    			res = nowdiff;
    			resx = now;
    			resy = ii;
    			
    	print("%d/%d")%(resx,resy);
    	'''
    	res = Fraction(x, y).limit_denominator(n);
    	print(res) if res % 1 != 0 else str(res)+"/1";
    
    	pass