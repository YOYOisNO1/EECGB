def program446():
    a,b=input(),input()
    c=''
    for i in xrange(len(a)):
         c+= '0' if a[i]==b[i] else '1'
    print('').join(c)