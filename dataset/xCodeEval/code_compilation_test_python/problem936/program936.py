def program936():
    input();print 'HARD' if any map(lambda x : [False,True][int(x)], input.split(' ')) else 'Easy'