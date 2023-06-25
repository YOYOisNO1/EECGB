    import sys
    from time import time
    from itertools import chain,combinations
    
def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    
    colors={}
    colors['R']=0
    colors['G']=1
    colors['B']=2
    colors['Y']=3
    colors['W']=4
    
    line1=sys.stdin.readline()
    n=int(line1.split(' ')[0].strip('\n'))
    rows=set()
    columns=set()
    
    cards=[]
    for i in xrange(0,5):
        cards.append([0,0,0,0,0])
    
    line=sys.stdin.readline().strip('\n').split(' ')
    for x in line:
        cards[colors[x[0]]][int(x[1])-1]=1
        rows.add(colors[x[0]])
        columns.add(int(x[1])-1)
        
def checkHints(inp):
        for i in xrange(0,5):
            missed=0
            for j in xrange(0,5):
                if cards[i][j] and j+5 not in inp:
                    missed+=1
                    #print(i,j,) 'i'
            if missed>1:
                return False
        for j in xrange(0,5):
            missed=0
            for i in xrange(0,5):
                if cards[i][j] and i not in inp:
                    missed+=1
                    #print(i,j,) 'j'
            if missed>1:
                return False
        missed=0
        for i in xrange(0,5):
            for j in xrange(0,5):
                if cards[i][j] and not (i in inp or j+5 in inp):
                    missed+=1
        if missed>1:
            return False
        return True
    
def add5(inp):
        return inp+5
    
    possibleHints=list(rows)+map(add5,columns)
    hintSets=list(powerset(possibleHints))
    least=10
    for x in hintSets:
        if checkHints(x):
            least=min(least,len(x))
    
    print(least)
    