    #                               #
        # author : samars_diary #
        # 06-09-2020 │ 17:10:07 #
    #                               #
    
    import sys, os.path
    
    if(os.path.exists('input.txt')):
        sys.stdin = open('input.txt',"r")
        sys.stdout = open('output.txt',"w")
    
    sys.setrecursionlimit(10 ** 5)
    
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
    
    #print=sys.stdout.write
    
def solve():
        a,b=mi()
        c=list(input())
        for _ in range(b):
            j=0
            while j<=(a-2):
                if c[j]=='B' and c[j+1]=='G':
                    c[j],c[j+1]=c[j+1],c[j]
                    j+=2
                else:
                    j+=1
        s=''.join(c)
        print(s)
    
    # for _ in range(ii()):
    solve()