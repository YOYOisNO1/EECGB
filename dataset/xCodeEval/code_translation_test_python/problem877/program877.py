    #coding=utf-8
    #求素数p的原根个数，即是p-1的欧拉函数;
    
def euler(n):
        if n <= 2:
            return 1
        cnt = n
        for x in xrange(2, n):
            if n%x == 0:
                cnt -= cnt/x #给忘记了！
                while n%x == 0:
                    n /= x
        if n > 1:
            cnt -= cnt/n
        return cnt
    
    p = input()
    ret = euler(p-1)
    print(ret)