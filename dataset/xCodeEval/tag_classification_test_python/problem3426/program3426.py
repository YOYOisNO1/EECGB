def program3426():
    n,m=map(int,input().split())
    s=input()
    s1=input()
    if(s[0]=='>'):
        if(s[-1]=='<' and s1[0]=='^' and s1[-1]=='v'):
            print('YES')
        else:
            print('NO')
    else:
        if(s[-1]=='>' and s1[0]=='v' and s1[-1]=='^'):
            print('YES')
        else:
            print('NO')