def program12():
    import sys,math
    gl,gr=map(int,sys.stdin.readline().strip().split(' '))
    bl,br=map(int,sys.stdin.readline().strip().split(' '))
    if abs(gl-br)<=1 or abs(bl-gr)<=1:
        print 'YES'
    else:
        print 'NO'
    