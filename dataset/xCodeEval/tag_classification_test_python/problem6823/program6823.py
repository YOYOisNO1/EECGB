def solve():
        k  =int(input())
        name = input()
        n=len(name)
        latinletters=[0]*k
        letters=[None]*n
        
        for i in range (n//2):
            if name[i]!='?' and name[n-1-i]!='?' and name[i]!=name[n-1-i]:
                return "IMPOSSIBLE"
            elif name[i]!='?':
                letters[i]=letters[n-1-i]=name[i]
                latinletters[int(ord(letters[i])-ord('a'))]+=1
            elif name[n-1-i]!='?':
                letters[i]=letters[n-1-i]=name[n-1-i]
                latinletters[int(ord(letters[i])-ord('a'))]+=1
                
        if n%2!=0:
            if name[n//2]!='?':
                letters[n//2]=name[n//2]
                latinletters[int(ord(name[n//2])-ord('a'))]+=1
            else:
                if 0 in latinletters:
                    j=(k-1)-list(reversed(latinletters)).index(0)
                    letters[n//2]=chr(j+ord('a'))
                    latinletters[int(ord(letters[n//2])-ord('a'))]+=1
                else:
                    letters[n//2]='a'
            
        
        for i in range (n//2-1,-1,-1):
            if name[i]=='?' and name[n-1-i]=='?':
                if 0 in latinletters:
                    j=(k-1)-list(reversed(latinletters)).index(0)
                    letters[i]=letters[n-1-i]=chr(j+ord('a'))
                    latinletters[int(ord(letters[i])-ord('a'))]+=1
                else:
                    letters[i]=letters[n-1-i]='a'
        
        if 0 in latinletters:
            return "IMPOSSIBLE"
        
        else:
            return "".join(letters)
        
    
    print(solve())