    import math
def foo():
        n,t= map(int,input().split())
        s=input()
       
        for _ in range(t):
            d=""
            i=0
            while(i<n):         
                
                if(i+1<n):
                    if (s[i] =='B' and s[i+1] == 'G' ):
                        d+='GB'
                        i+=2
                        continue
                d+=s[i]
                i+=1
            
            s=d
        print(d)
    if __name__ == "__main__":
        foo()