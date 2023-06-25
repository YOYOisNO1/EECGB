    '''
    	Mudit Joshi
    	IIITDM Jabalpur
    '''
     
    import sys,math
    from collections import Counter
    from bisect import bisect_left as bl
    input = lambda: sys.stdin.readline().rstrip()
    r_s = lambda: input().strip()                   #read str
    r_ss = lambda: input().split()                  #read stringss
    r_i = lambda: int(input())                      #read int
    r_is = lambda: map(int, input().split())        #read ints
    r_f = lambda: float(input())                    #read float
    r_fs = lambda: map(Decimal, input().split())    #read floats
     
    #for efficiently taking lot of space separated queries on each line, use this.
    r_qs = lambda: map(lambda s:map(int, s.split(' ')), sys.stdin.readlines())
    
def next_permutation(s):
      for i in reversed(xrange(len(s))):
        if s[i] > s[i-1]:
          break
      else:
        return []
      i -= 1
      for j in reversed(xrange(i + 1, len(s))):
        if s[j] > s[i]: break
      t = s[i]
      s[i] = s[j]
      s[j] = t
      s[i + 1:] = reversed(s[i + 1:])
      return s
    
    if __name__ == '__main__':
        #start here
        g=[]
        for i in range(5):
            g.append(r_is())
        #print(g)
        p=[0,1,2,3,4]
        q=list(p);
        tmp,ans,f=0,0,1
        while True:
            tmp = g[p[0]][p[1]] + g[p[1]][p[0]];
            tmp += g[p[2]][p[3]] + g[p[3]][p[2]];
            #1234
            tmp += g[p[1]][p[2]] + g[p[2]][p[1]];
            tmp += g[p[3]][p[4]] + g[p[4]][p[3]];
            #234
            tmp += g[p[2]][p[3]] + g[p[3]][p[2]];
            #34
            tmp += g[p[3]][p[4]] + g[p[4]][p[3]];
            if tmp>ans:
                ans = tmp;
            p=next_permutation(p)
            if p==[1,0,2,3,4]:
                if f==0:
                    break
                else:
                    f=0
        print(ans)
        