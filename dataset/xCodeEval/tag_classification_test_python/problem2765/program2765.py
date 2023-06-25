def program2765():
    '''
    	Arpan Tarkas
    	IIITDM Jabalpur
    '''
     
    import sys,math
    from collections import Counter
    from bisect import bisect_left as bl
    input = lambda: sys.stdin.readline().rstrip()
    r_s = lambda: input().strip()                   #read str
    r_ss = lambda: input().split()          #read stringss
    r_i = lambda: int(input())              #read int
    r_is = lambda: map(int, input().split())#read ints
    r_f = lambda: float(input())            #read float
    r_fs = lambda: map(Decimal, input().split()) #read floats
     
    #for efficiently taking lot of space separated queries on each line, use this.
    r_qs = lambda: map(lambda s:map(int, s.split(' ')), sys.stdin.readlines())
    
    if __name__ == '__main__':
        #start here
        s=r_s()
        if s == s[::-1]:
            if len(set(s))==1:
                print(0)
            else:
                print(len(s)-1)
        else:
            print(len(s))
        