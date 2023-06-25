def program1850():
    s = input()
    s = s.replace('e', '.');
    L = s.split('.');
    # print(L)
    b = int(L[2])
    w = L[0];
    d = L[1];
    if b<len(d):
    	w = w + d[:b] + '.' + d[b:]
    elif b==len(d):
        w = w + d	
    else:
    	w = w + d + (b-len(d)) * '0'
    if w[:-1]=='.':
    	w = w[:-1]
    if w[-2:]=='.0'
    	w = w[:-2]
    print(w)
    
    #s = input()