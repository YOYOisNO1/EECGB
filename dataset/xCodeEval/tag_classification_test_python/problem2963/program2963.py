def program2963():
    L,R=map(int,input().split())
    pw=1
    while pw<=R: pw*=10
    
    if R<pw/2-1:
        print(R*(pw-R-1))
    else:
        if pw / L >= 10: L = pw / 10
        if L > pw/2:
            print(L*(pw - L - 1))
        else:
            print((pw//2)*(pw//2-1))