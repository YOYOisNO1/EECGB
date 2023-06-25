def sol(s):
        m=0
        m+=min(abs(ord(s[0])-ord('A')),ord('Z')-ord(s[0])+ord('A')-ord('A')+1,ord(s[0])-ord('A')+ord('Z')-ord('A')+1)
        #print(m)
        m+=min(abs(ord(s[1])-ord('C')),ord('Z')-ord(s[1])+ord('C')-ord('A')+1,ord(s[1])-ord('A')+ord('Z')-ord('C')+1)
        #print(m)
        m+=min(abs(ord(s[2])-ord('T')),ord('Z')-ord(s[2])+ord('T')-ord('A')+1,ord(s[2])-ord('A')+ord('Z')-ord('T')+1)
        #print(m)
        m+=min(abs(ord(s[3])-ord('G')),ord('Z')-ord(s[3])+ord('G')-ord('A')+1,ord(s[3])-ord('A')+ord('Z')-ord('G')+1)
        return(m)
    n=int(input())
    s=input()
    k=10**9
    for i in range(n-3):
       k=min(k,sol(s[i:i+4]))
    print(k)