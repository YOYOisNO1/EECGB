    b,r = [input() for _ in xrange(6)],[]
def x(i,d,c='RL'): b[i]=b[i][-d:]+b[i][:-d];r.extend([c[d>3]+str(i+1)]*(d if d<3 else 6-d))
def y(i,d): global b;b=zip(*b);x(i,d,'DU');b=zip(*b)
def u(i,j): x(j,1);y(i,1);x(j,5);y(i,5)
def p(i,j): u(i,j);x((j+5)%6,1);u((i+1)%6,j);x((j+5)%6,5);u(i,j);u(i,j)
def l(i,j): p((i+1)%6,j);p((i+3)%6,j);x(j,1)
    for k,c in enumerate(sorted(''.join(b))):
        ii,jj=k%6,k/6
        z = filter(lambda x: c in x, b)[0]    
        i,j=z.index(c),b.index(z)
        while i!=ii: l(i,j); i=(i+5)%6
        while j>jj: u(ii,j); j-=1
    print len(r)
    print '\n'.join(r)