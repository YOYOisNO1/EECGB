    
 def Z(s):
       left=0
       right=0
       z=[ 0 for i in range(len(s))]
       for k in range(1,len(s)):
           if k > right:
               left=k
               right=k 
               while right <len(s) and s[right]==s[right-left]:
                   right=right+1
               z[k]=right-left
               right=right-1
           else:
    
               k1=k-left
               if z[k1]< right-k+1:
                   z[k]=z[k1]
               else:
                   left=k
                   while right <len(s) and s[right]==s[right-left]:
                       right=right+1
                   z[k]=right-left
                   right=right-1
       return z
    s=input()
    a=Z(s)
    a.reverse()
    p=0
    r=0
    for i in range(len(a)):
       if i+1==a[i]:
          if p==0:
             p=i+1
          else:
             r=p
             p=i+1
       elif a[i]>=p:
          r=p
    if r==0:
       print("Just a legend")
    else:
       print(s[0:r])
    
    