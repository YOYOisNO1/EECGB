def program347():
    s1=input()
    s1=input()
    ans="no"
    for i in range(4):
        for j in range(1,len(s1)/3):
            if len(s1)%j==1:
                b=1
            else:
                b=0
            s=s1[i:-1:j]+s1[-1]*b
            if '*****' in s:
                ans="yes"
    print ans