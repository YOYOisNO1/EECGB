def program2156():
    input()
    P=map(int,input().split())
    for a,b in sorted([[P.index(p),i%2]for i,p in enumerate(sorted(P))]):print b