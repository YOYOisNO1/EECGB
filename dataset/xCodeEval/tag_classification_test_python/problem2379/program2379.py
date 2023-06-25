def program2379():
    n=int(input())
    s=['+------------------------+']
    d='|'+'#O'[n>2]+'.'*23+'|'
    if n>2:n-=1
    for i in range(3):x=n//3+(n%3>i);s+=['|'+('.'.join('O'*x+'#'*(11-x)))]
    s.insert(3,d)
    s+=[s[0]]
    s[1]+='.|D|)'
    s[2]+='.|.|'
    s[4]+='.|.|)'
    print('\n'.join(s))