    '''
    Created on 2013-4-16
    URL    : http://codeforces.com/contest/281/problem/B
    @author: yskj
    '''
    
    x,y,n = map(int, input().split())
    
def getValue(a,b):
        return [abs(b * x - a * y), b * y];
    
def cmpValue(a, b):
        return a[0] * b[1] > a[1] * b[0];
    
def cmpEqual(a, b):
        return a[0] * b[1] == a[1] * b[0];
    
    b = 1;
    ans = [1000000000, 1];
    ansMin = [1000000000, 1];
    while b <= n:
        left = max(x * b / y - 1, 0);
        right = x * b / y + 1;
        #print(b,) left, right;
        while left <= right:
            tmp = [abs(b * x - left * y), b * y];
            if cmpValue(ansMin, tmp):
                ansMin = tmp
                ans = [left, b];
            elif cmpEqual(ansMin, tmp):
                if (b < ans[1]) or (b == ans[1] and left < ans[0]):
                    ans = [left, b];
            left += 1;
        b += 1;
    
    print(str(ans[0])) + "/" + str(ans[1]);
            
                    
                    
                        
                
            
            