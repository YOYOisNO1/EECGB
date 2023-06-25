def program1703():
    a,w,b='',0,0
    for i in range(8):a+=input()
    w,b=9*a.count('Q')+5*a.count('R')+3*a.count('B')+3*a.count('N')+a.count('P'),9*a.count('q')+5*a.count('r')+3*a.count('b')+3*a.count('n')+a.count('p');print('White' if w>b else 'Black' if w<b else 'Draw')
    →Judgement Protocol