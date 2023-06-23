def program530():
    from sys import stdin
    a = stdin.readline().strip().split()
    b = []
    for i in a:
     b.append(int(i))
    c = set(b)
    if len(c)>3:
     print "Alien"
    else if(len(c)==3):
     print "Bear"
    else:
     print "Elephant"