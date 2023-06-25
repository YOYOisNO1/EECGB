def program2839():
    n=input()
    m=input()
    print ''.join([str(int(n[i]!=m[i]) for i in range len(n))])