def program456():
    |#WTF
    _=list(map(int,input().split()))
    __=list(map(int,input().split()))
    ___=[i+1 for i in range(_[0])]
    while(len(__)!=1):
        if(__[0]<=_[1]):
            __.remove(__[0])
            ___.remove(___[0])
        else:
            __.append(__[0]-_[1])
            __.remove(__[0])
            ___.append(___[0])
            ___.remove(___[0])
    print(___[0])
    #Lorenzo