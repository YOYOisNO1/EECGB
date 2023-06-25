def program404():
    s = ['']*3
    s[0] = input()
    s[1] = input()
    s[2] = input()
    for i in range(3):
        if s[i] == 'B>A':
            s[i] = 'A<B'
        if s[i] == 'B<A':
            s[i] = 'A>B'
        if s[i] == 'C<A':
            s[i] = 'A>C'
        if s[i] == 'C>A':
            s[i] = 'A<C'
        if s[i] == 'C<B':
            s[i] = 'B>C'
        if s[i] == 'C>B':
            s[i] = 'B<C'
    s.sort()
    if s[0][1] == '<' and s[1][1]=='<' and s[2][1]=='<':
        print 'ABC'
    elif s[0][1] == '>' and s[1][1]=='<' and s[2][1]=='<':
        print 'BAC'
    elif s[0][1] == '>' and s[1][1]=='>' and s[2][1]=='>':
        print 'CBA'
    elif s[0][1] == '<' and s[1][1]=='>' and s[2][1]=='>':
        print 'CAB'
    elif s[0][1] == '<' and s[1][1]=='<' and s[2][1]=='>':
        print 'ACB'
    elif s[0][1] == '>' and s[1][1]=='>' and s[2][1]=='<':
        print 'BCA'
    else:
        print 'Impossible'
        