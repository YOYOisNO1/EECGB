def program2792():
    
     s = input()
    d = []
    k = -1
    for i in range(len(s)):
        d.append(ord(s[i])-97)    
    for i in range(len(s)-25):
        b = False
        for j in range(i,i+26):
            if d[j]>j-i:
                b = True
        if b==False:
            k=i
            break   
    if k>=0:
        for i in range(k):
            print(s[i],end = '')
        print('abcdefghijklmnopqrstuvwxyz')
        for i in range(k+26,len(s)):
            print(s[i],end = '')
    else:
        print(k)
                