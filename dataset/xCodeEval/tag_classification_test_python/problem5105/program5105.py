    #25 75 00
    
def f(s):
        if len(s)==1:
            if s=="0" or s=="X" or s=="_":
                return 1
            return 0
        ans=0
        n=len(s)
        posX=set()
        posGood=set()
        for i in range(n):
            if s[i]=="X":
                posX.add(i)
            elif s[i]!="_":
                posGood.add(i)
        for i in range(10**(n-1),(10**(n))):
            if i%25==0:
                l=str(i)
                st=set()
                for pos in posX:
                    st.add(l[pos])
                if len(st)>1:
                    continue
                flag=False
                for pos in posGood:
                    if l[pos]!=s[pos]:
                        flag=True
                        break
                if not flag:
                    ans+=1
        return ans
    
    print(f(input()))