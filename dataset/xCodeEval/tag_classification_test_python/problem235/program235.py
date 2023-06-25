def program235():
    n=input()
    x=len(n)
    import sys
    from itertools import permutations
    if len(n)%2==0:
        s='4'*(x//2)+'7'*(x//2)
    else:
        s='4'*(x//2+1)+'7'*(x//2+1)
    if len(n)%2!=0:
        sys.stdout.write(s+'\n')
    else:
        l1=[]
        for l in permutations(s,len(s)):
            a=int(''.join(l))
            if a>=int(n):
                sys.stdout.write(str(a)+'\n')
                sys.exit()
        sys.stdout.write('4'*(len(s)//2+1)+'7'*(len(s)//2+1))
                
            